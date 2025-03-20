import os
import cv2
import dlib
import numpy as np
import pickle
from scipy.spatial import distance
import attendance_manager

# Dlib yüz tespit ve tanıma modelleri
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Kayıtlı öğrenci embedding'lerinin bulunduğu dosya
STUDENT_DB = "student_encodings.pkl"

# Tanıma için eşik değeri: Euclidean mesafe THRESHOLD'un altındaysa eşleşme var demektir.
THRESHOLD = 0.6  # İhtiyaca göre ayarlayın

def get_face_embedding(image, face):
    """
    Verilen yüz bölgesinin embedding'ini hesaplar.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    shape = predictor(gray, face)
    return np.array(face_rec_model.compute_face_descriptor(image, shape))

def register_student(student_id, num_images=20):
    """
    Öğrenci kaydı yaparken, kameradan alınan görüntülerdeki yüzleri tespit eder,
    her yüzün embedding'lerini hesaplar ve bunların ortalamasını kaydeder.
    Ayrıca, kaydedilen yüz görüntüleri "data/train/<student_id>" klasörüne kaydedilir.
    """
    save_dir = os.path.join("data", "train", student_id)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"📁 Oluşturuldu: {save_dir}")

    cap = cv2.VideoCapture(0)
    count = 0
    embeddings = []
    print(f"📸 {student_id} için kayıt başlatıldı. {num_images} adet görüntü alınacak. Çıkmak için 'q' tuşuna basın.")

    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        if len(faces) > 0:
            face = faces[0]  # İlk tespit edilen yüzü kullan
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            embedding = get_face_embedding(frame, face)
            if embedding is not None:
                embeddings.append(embedding)
                filename = os.path.join(save_dir, f"{student_id}_{count}.jpg")
                face_img = frame[y:y+h, x:x+w]
                cv2.imwrite(filename, face_img)
                count += 1
                print(f"{count}. görüntü kaydedildi: {filename}")
        cv2.imshow("Öğrenci Kaydı", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if embeddings:
        avg_embedding = np.mean(embeddings, axis=0)
        # Mevcut öğrenci embedding'lerini yükle veya yeni bir sözlük oluştur
        if os.path.exists(STUDENT_DB):
            with open(STUDENT_DB, "rb") as f:
                student_encodings = pickle.load(f)
        else:
            student_encodings = {}
        student_encodings[student_id] = avg_embedding
        with open(STUDENT_DB, "wb") as f:
            pickle.dump(student_encodings, f)
        print(f"✅ Öğrenci {student_id} kaydı tamamlandı, ortalama embedding kaydedildi.")
    else:
        print("❌ Hiçbir yüz tespit edilemedi, öğrenci kaydı başarısız oldu.")

def predict_from_camera():
    """
    Kamera üzerinden gerçek zamanlı yüz tanıması yapar.
    Kayıtlı öğrenci embedding'leri ile karşılaştırma yaparak en yakın eşleşmeyi bulur.
    Eğer mesafe THRESHOLD'un altındaysa eşleşme var demektir; aksi halde 'unknown' olarak atanır.
    Tanınan öğrenci için attendance_manager.add_attendance_record() çağrılır.
    """
    if not os.path.exists(STUDENT_DB):
        print("⚠️ Öğrenci kayıt veritabanı bulunamadı. Lütfen önce öğrenci kaydı yapın!")
        return

    with open(STUDENT_DB, "rb") as f:
        students = pickle.load(f)

    cap = cv2.VideoCapture(0)
    print("🔍 Gerçek zamanlı yüz tanıma başladı. Çıkmak için 'q' tuşuna basın.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            embedding = get_face_embedding(frame, face)
            if embedding is None:
                continue

            min_dist = float("inf")
            best_match = "unknown"
            for student_id, saved_embedding in students.items():
                dist = distance.euclidean(saved_embedding, embedding)
                if dist < THRESHOLD and dist < min_dist:
                    min_dist = dist
                    best_match = student_id

            cv2.putText(frame, f"{best_match} ({min_dist:.2f})", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            if best_match == "unknown":
                cv2.putText(frame, "Kayıt bulunamadı", (x, y+h+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
            else:
                attendance_manager.add_attendance_record(best_match)

        cv2.imshow("Real-Time Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Örneğin, test için:
    # register_student("stu001", num_images=20)
    predict_from_camera()