import os
import cv2
import dlib
import numpy as np
import pickle

# Dlib yüz tespit ve tanıma modelleri
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Öğrenci kayıt veritabanı dosya adı (embedding'ler burada saklanacak)
STUDENT_DB = "student_encodings.pkl"

def get_face_embedding(image, face):
    """
    Yüz bölgesinin embedding'ini hesaplamak için
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    shape = predictor(gray, face)
    return np.array(face_rec_model.compute_face_descriptor(image, shape))

def register_student(student_id, num_images=20):
    """
    Öğrenci kaydı yaparken, kameradan alınan görüntülerdeki yüzleri tespit eder,
    her yüzün embedding'ini hesaplar, ve bu embedding'lerin ortalamasını kaydeder.
    Aynı zamanda, öğrenciye ait görüntüler "data/train/<student_id>" altına kaydedilir.
    """
    # Öğrenciye özel klasörü oluşturmak için kod
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
            # İlk tespit edilen yüzü kullanıyoruz
            face = faces[0]
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
        print(f"✅ {student_id} kaydı tamamlandı, ortalama embedding kaydedildi.")
    else:
        print("❌ Hiçbir yüz tespit edilemedi, öğrenci kaydı başarısız oldu.")

if __name__ == "__main__":
    register_student("stu001", num_images=40)