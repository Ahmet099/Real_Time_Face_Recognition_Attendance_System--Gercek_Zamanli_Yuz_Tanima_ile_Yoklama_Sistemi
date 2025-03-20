import sqlite3
import os
import time

def add_images_to_database():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eye_detections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        detection_time TIMESTAMP
    )
    ''')
    conn.commit()

    detected_eyes_dir = "detected_eyes"
    if not os.path.exists(detected_eyes_dir):
        print("Henüz kayıtlı göz görüntüsü bulunmuyor.")
        return

    for file in os.listdir(detected_eyes_dir):
        if file.endswith(".jpg"):
            file_path = os.path.join(detected_eyes_dir, file)
            timestamp = int(time.time())
            cursor.execute("INSERT INTO eye_detections (filename, detection_time) VALUES (?, ?)", (file_path, timestamp))
            conn.commit()
            print(f"Veritabanına eklendi: {file_path}")

    conn.close()
    print("Tüm kayıtlar veritabanına aktarıldı!")

if __name__ == "__main__":
    add_images_to_database()