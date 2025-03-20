import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
import pickle
import attendance_manager
from sklearn.utils.class_weight import compute_class_weight

def ensure_directories():
    if not os.path.exists("data/train"):
        os.makedirs("data/train")
        print("📁 Klasör oluşturuldu: data/train")

def train_model():
    ensure_directories()
    
    img_width, img_height = 96, 96  # Daha fazla detay için 96x96
    batch_size = 32
    epochs = 20

    train_data_dir = 'data/train'
    
    # Training verisinin %20'sini validation için ayırıyoruz.
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.3,
        height_shift_range=0.3,
        horizontal_flip=True,
        validation_split=0.2
    )

    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )
    
    # Sınıf ağırlıklarını hesaplayarak veri dengesizliğini azaltıyoruz.
    labels = train_generator.classes
    class_weights = compute_class_weight('balanced', classes=np.unique(labels), y=labels)
    class_weights_dict = {i: class_weights[i] for i in range(len(class_weights))}
    print("📊 Sınıf ağırlıkları:", class_weights_dict)

    base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(img_width, img_height, 3))
    
    model = Sequential([
        base_model,
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(train_generator.num_classes, activation='softmax')
    ])
    
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    print("📌 Model eğitilmeye başladı...")
    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        class_weight=class_weights_dict
    )
    
    model.save('eye_recognition_model.h5')
    print("✅ Model eğitildi ve 'eye_recognition_model.h5' dosyası kaydedildi.")
    
    mapping = train_generator.class_indices
    with open("class_indices.pkl", "wb") as f:
        pickle.dump(mapping, f)
    print("📁 Sınıf eşlemesi kaydedildi:", mapping)

def predict_from_camera():
    if not os.path.exists('eye_recognition_model.h5'):
        print("⚠️ Model dosyası bulunamadı. Lütfen önce modeli eğitmek için train_model() fonksiyonunu çalıştırın.")
        return

    model = tf.keras.models.load_model('eye_recognition_model.h5')
    
    if os.path.exists("class_indices.pkl"):
        with open("class_indices.pkl", "rb") as f:
            mapping = pickle.load(f)
        rev_mapping = {v: k for k, v in mapping.items()}
    else:
        rev_mapping = {}

    cap = cv2.VideoCapture(0)
    print("🔍 Gerçek zamanlı tanıma başladı. Çıkmak için 'q' tuşuna basın.")
    
    threshold = 0.95  # Güven eşiği

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            eye_region = frame[ey:ey+eh, ex:ex+ew]
            eye_region = cv2.resize(eye_region, (96, 96))
            eye_region = img_to_array(eye_region) / 255.0
            eye_region = np.expand_dims(eye_region, axis=0)

            predictions = model.predict(eye_region)
            confidence = np.max(predictions)
            if confidence < threshold:
                student_id = "unknown"
            else:
                predicted_class = np.argmax(predictions)
                student_id = rev_mapping.get(predicted_class, "unknown")

            cv2.putText(frame, f"Prediction: {student_id} ({confidence:.2f})", (ex, ey-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            if student_id == "unknown":
                cv2.putText(frame, "Kayıt bulunamadı, lütfen kaydedin.", (ex, ey+eh+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
            else:
                attendance_manager.add_attendance_record(student_id)

        cv2.imshow("Real-Time Eye Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Aşağıdaki satırlardan ihtiyacınıza göre birini aktif edin.
    # Modeli eğitmek için:
    # train_model()
    
    # Gerçek zamanlı tanıma için:
    predict_from_camera()