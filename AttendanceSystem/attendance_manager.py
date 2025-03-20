import sqlite3
import time
from datetime import datetime
import os
import pandas as pd

DB_NAME = "attendance.db"

def get_current_timestamp():
    return int(time.time())

def create_tables():
    """Öğrenciler tablosu ve temel veritabanı yapılarını oluşturur."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance_tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_name TEXT UNIQUE,
        created_at TEXT
    )
    ''')

    conn.commit()
    conn.close()
    print("📁 Veritabanı tabloları oluşturuldu.")

def add_student(student_id, name):
    """Yeni bir öğrenciyi ekler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Öğrenciyi kaydet
    cursor.execute("INSERT OR IGNORE INTO students (student_id, name) VALUES (?, ?)", 
                   (student_id, name))
    
    conn.commit()
    conn.close()
    print(f"✅ Öğrenci eklendi: {student_id} - {name}")

    # Öğrencinin yüz verilerini saklamak için klasör oluştur
    student_train_dir = os.path.join("data", "train", student_id)
    if not os.path.exists(student_train_dir):
        os.makedirs(student_train_dir)
        print(f"📂 Klasör oluşturuldu: {student_train_dir}")

def list_all_students():
    """📌 Kayıtlı tüm öğrencileri listeler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT student_id, name FROM students ORDER BY student_id")
    records = cursor.fetchall()
    conn.close()

    if records:
        print("\n📌 Kayıtlı Öğrenciler:")
        print("Öğrenci ID\tİsim")
        for rec in records:
            print(f"{rec[0]}\t{rec[1]}")
    else:
        print("📌 Henüz kayıtlı öğrenci bulunmuyor.")

def create_new_attendance_table():
    """Yeni bir yoklama tablosu oluşturur ve attendance_tables'e kaydeder."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    table_id = datetime.today().strftime("%Y%m%d_%H%M%S")  # Örneğin: 20250317_121530
    table_name = f"attendance_{table_id}"

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        student_id TEXT PRIMARY KEY,
        timestamp INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    )
    ''')

    cursor.execute("INSERT INTO attendance_tables (table_name, created_at) VALUES (?, ?)", 
                   (table_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    conn.commit()
    conn.close()
    print(f"✅ Yeni yoklama tablosu oluşturuldu: {table_name}")

def list_attendance_tables():
    """Mevcut tüm yoklama tablolarını listeler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, table_name, created_at FROM attendance_tables ORDER BY id DESC")
    records = cursor.fetchall()
    conn.close()

    if records:
        print("\n📊 Mevcut Yoklama Tabloları:")
        print("ID\tTablo Adı\t\tTarih")
        for rec in records:
            print(f"{rec[0]}\t{rec[1]}\t{rec[2]}")
    else:
        print("❌ Henüz hiçbir yoklama tablosu oluşturulmamış.")

def add_attendance_record(student_id):
    """Bir öğrenciyi en son oluşturulan yoklama tablosuna ekler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT table_name FROM attendance_tables ORDER BY id DESC LIMIT 1")
    latest_table = cursor.fetchone()

    if latest_table is None:
        print("⚠️ Önce yeni bir yoklama tablosu oluşturmalısınız.")
        conn.close()
        return
    
    table_name = latest_table[0]

    cursor.execute(f"SELECT * FROM {table_name} WHERE student_id = ?", (student_id,))
    existing = cursor.fetchone()

    if existing:
        print(f"⚠️ Öğrenci {student_id} zaten yoklamaya dahil edildi.")
    else:
        timestamp = get_current_timestamp()
        cursor.execute(f"INSERT INTO {table_name} (student_id, timestamp) VALUES (?, ?)", 
                       (student_id, timestamp))
        conn.commit()
        print(f"✅ {student_id} öğrenci yoklamaya eklendi.")

    conn.close()

def view_attendance(table_id):
    """Belirli bir yoklama tablosunu görüntüler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    table_name = f"attendance_{table_id}"

    try:
        cursor.execute(f'''
            SELECT a.student_id, s.name, a.timestamp
            FROM {table_name} AS a
            LEFT JOIN students AS s ON a.student_id = s.student_id
        ''')
        records = cursor.fetchall()
    except sqlite3.OperationalError:
        print(f"❌ '{table_name}' yoklama tablosu bulunamadı.")
        conn.close()
        return
    
    conn.close()

    if records:
        print("\n📊 Yoklama Kaydı:")
        print("Öğrenci ID\tÖğrenci Adı\tTimestamp")
        for rec in records:
            print(f"{rec[0]}\t{rec[1]}\t{rec[2]}")
    else:
        print("📌 Bu yoklama tablosu boş.")

def export_attendance_to_excel(table_id):
    """Belirli bir yoklama tablosunu Excel'e aktarır."""
    conn = sqlite3.connect(DB_NAME)
    table_name = f"attendance_{table_id}"

    try:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        excel_filename = f"{table_name}.xlsx"
        df.to_excel(excel_filename, index=False)
        print(f"📂 Yoklama tablosu Excel olarak kaydedildi: {excel_filename}")
    except Exception as e:
        print(f"❌ Excel aktarımında hata oluştu: {e}")
    
    conn.close()

def delete_student(student_id):
    """Öğrenciyi tamamen veritabanından siler."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    print(f"✅ Öğrenci {student_id} tamamen silindi.")

def reset_database():
    """Tüm veritabanını sıfırlar."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("DROP TABLE IF EXISTS attendance_tables")
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'attendance_%'")
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")

    conn.commit()
    conn.close()
    print("⚠️ Tüm veriler silindi ve veritabanı sıfırlandı.")

if __name__ == "__main__":
    create_tables()