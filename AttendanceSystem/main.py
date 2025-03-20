import attendance_manager
import face_recognition  # Yüz tanıma işlemleri için
attendance_manager.create_tables()

def menu():
    print("\n------ MENÜ ------")
    print("1 - Öğrenci Kaydı Yap")
    print("2 - Gerçek Zamanlı Yoklama Al (Yeni Yoklama Tablosu Oluşturur)")
    print("3 - Mevcut Yoklama Tablolarını Listele")
    print("4 - Belirli Bir Yoklama Tablosunu Görüntüle")
    print("5 - Belirli Bir Yoklama Tablosuna Elle Öğrenci Ekle")
    print("6 - Belirli Bir Yoklama Tablosundan Öğrenci Sil")
    print("7 - Belirli Bir Yoklama Tablosunu Sil")
    print("8 - Belirli Bir Yoklama Tablosunu Excel'e Aktar")
    print("9 - Tüm Öğrencileri Listele")
    print("10 - Öğrenciyi Veritabanından Sil")
    print("11 - Tüm Veritabanı Tablolarını Sil ve Yeniden Başlat")
    print("12 - Sesli Komut Modunu Başlat")
    print("0 - Çıkış")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Seçiminizi yapın (0-11): ")
        
        if choice == "1":
            student_id = input("Öğrenci ID girin: ")
            name = input("Öğrenci ismini girin: ")
            attendance_manager.add_student(student_id, name)
            reg = input("Öğrenci yüz kaydı yapmak ister misiniz? (e/h): ")
            if reg.lower() == "e":
                face_recognition.register_student(student_id, num_images=200)
        
        elif choice == "2":
            print("📷 Kamera açılıyor, yeni bir yoklama tablosu oluşturulacak...")
            attendance_manager.create_new_attendance_table()
            face_recognition.predict_from_camera()  # Yeni yoklama başlat
        
        elif choice == "3":
            attendance_manager.list_attendance_tables()  # Tüm yoklama tablolarını listele
        
        elif choice == "4":
            table_id = input("Görüntülemek istediğiniz yoklama tablosunun ID'sini girin: ")
            attendance_manager.view_attendance(table_id)  # Belirli bir tabloyu görüntüle
        
        elif choice == "5":
            table_id = input("Elle öğrenci eklemek istediğiniz yoklama tablosunun ID'sini girin: ")
            student_id = input("Eklemek istediğiniz öğrenci ID'sini girin: ")
            attendance_manager.add_student_to_attendance(table_id, student_id)
        
        elif choice == "6":
            table_id = input("Öğrenci silmek istediğiniz yoklama tablosunun ID'sini girin: ")
            student_id = input("Silmek istediğiniz öğrenci ID'sini girin: ")
            attendance_manager.delete_student_from_attendance(table_id, student_id)
        
        elif choice == "7":
            table_id = input("Silmek istediğiniz yoklama tablosunun ID'sini girin: ")
            attendance_manager.delete_attendance_table(table_id)  # Belirli tabloyu sil
        
        elif choice == "8":
            table_id = input("Excel'e aktarmak istediğiniz yoklama tablosunun ID'sini girin: ")
            attendance_manager.export_attendance_to_excel(table_id)
        
        elif choice == "9":
             attendance_manager.list_all_students()  # ✅ Burada çağırılıyor
        
        elif choice == "10":
            student_id = input("Silmek istediğiniz öğrenci ID'sini girin: ")
            attendance_manager.delete_student(student_id)  # Öğrenciyi tamamen sil
        
        elif choice == "11":
            confirm = input("⚠️ Tüm verileri silmek istediğinize emin misiniz? (e/h): ")
            if confirm.lower() == "e":
                attendance_manager.reset_database()  # Tüm veritabanı tablolarını sil

        elif choice == "12":
             import voice_control_main
             voice_control_main.voice_control()
        
        elif choice == "0":
            print("Çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçenek, tekrar deneyin.")