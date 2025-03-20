import os
import shutil

def organize_data():
    detected_eyes_dir = "detected_eyes"
    train_data_dir = "data/train/unknown"  # Tespit edilen öğrenciler için bilinmeyen klasörü

    # Eğer eğitim verisi klasörü yoksa oluştur
    if not os.path.exists(train_data_dir):
        os.makedirs(train_data_dir)

    # Kayıtlı göz görüntülerini eğitim verisi klasörüne taşı
    for file in os.listdir(detected_eyes_dir):
        if file.endswith(".jpg"):  # Sadece görüntüleri al
            src_path = os.path.join(detected_eyes_dir, file)
            dest_path = os.path.join(train_data_dir, file)
            shutil.move(src_path, dest_path)

    print(f"Tüm kayıtlar {train_data_dir} içine taşındı.")

if __name__ == "__main__":
    organize_data()