import speech_recognition as sr
import pyttsx3
import wikipediaapi
import datetime
import requests
import cv2
import sys
import difflib
import attendance_manager
import face_recognition


# Konuşma motorunu başlatan komut buymuş
engine = pyttsx3.init()

def speak(text):
    
    print(f"🗣️ Asena: {text}") 
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Mikrofon ile konuşmayı alır ve metne çevirir."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Nasıl yardımcı olayım... (Çıkış için 'Q' tuşuna basabilirsiniz.)")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=20)
            command = recognizer.recognize_google(audio, language="tr-TR")  # Türkçe dil desteği
            print(f"📢 Algılanan Komut: {command}")

            # Eğer "Q" tuşuna basıldıysa sistemi anında kapatmak için bu kod
            if cv2.waitKey(1) & 0xFF == ord('q'):
                speak("Şimdilik gidiyorum daha sonra tekrar Görüşmek üzere!")
                sys.exit()

            return command.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            speak("Ses algılama servisine ulaşılamıyor, internet bağlantınızı kontrol edin.")
            return None
        except sr.WaitTimeoutError:
            return None

# Kullanıcının şehir bilgisini sorması için buraya bir şehir yazarsam eğer sadece o şehri gösterir.
user_city = None

def get_weather():
    
    global user_city

    if user_city is None:
        speak("Hangi şehir için hava durumunu öğrenmek istersin?")
        user_city = recognize_speech()
        if not user_city:
            speak("Şehir ismini anlayamadım, lütfen tekrar söyler misin.")
            return "Şehir bilgisini alamadım."

    api_key = "bd5e378503939ddaee76f12ad7a97608"  # Buraya OpenWeather API anahtarını ekle
    url = f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric&lang=tr"

    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{user_city} için hava durumu: {desc}, sıcaklık {temp} derece."
        else:
            return f"{user_city} için hava durumu bilgisini alamadım."
    except:
        return "Hava durumu bilgisini getiremiyorum."

def get_current_time():
    
    now = datetime.datetime.now().strftime("%H:%M")
    return f"Şu an saat {now}"

def search_wikipedia(query):
    
    wiki = wikipediaapi.Wikipedia(user_agent="YoklamaAsistani/1.0 (info@example.com)", language="tr")  # Türkçe Wikipedia
    page = wiki.page(query)

    if page.exists():
        return page.summary[:500]  # İlk 500 karakteri getir
    else:
        return "Üzgünüm, bu konu hakkında bir bilgi bulamadım."
    

    # 📌 **MENÜ KOMUTLARI** - Birden fazla söyleme seçeneği için bu kısım var
menu_commands = {
          "1": ["öğrenci kaydı yap", "öğrenci ekle", "yeni öğrenci ekle", "1 öğrenci ekleyelim", "bir numarayı çalıştır"],
          "2": ["gerçek zamanlı yoklama al", "yoklama al", "şimdi yoklama alalım", "2 numarayı çalıştır", "sınıfı kontrol et"],
          "3": ["mevcut yoklama tablolarını listele", "hangi yoklamalar alındı", "3 numarayı çalıştır", "yoklama listesi göster"],
          "4": ["belirli bir yoklama tablosunu görüntüle", "4 numarayı çalıştır", "yoklama tablosunu aç"],
          "5": ["belirli bir yoklama tablosuna elle öğrenci ekle", "5 numarayı çalıştır", "yoklamaya öğrenci ekle"],
          "6": ["belirli bir yoklama tablosundan öğrenci sil", "6 numarayı çalıştır", "yoklamadan öğrenci çıkar"],
          "7": ["belirli bir yoklama tablosunu sil", "7 numarayı çalıştır", "yoklama tablosunu kaldır"],
          "8": ["belirli bir yoklama tablosunu excel'e aktar", "8 numarayı çalıştır", "yoklamayı excel'e kaydet"],
          "9": ["tüm öğrencileri listele", "9 numarayı çalıştır", "kayıtlı öğrencileri göster"],
          "10": ["öğrenciyi veritabanından sil", "10 numarayı çalıştır", "öğrenci kaydını sil"],
          "11": ["tüm veritabanı tablolarını sil ve yeniden başlat", "11 numarayı çalıştır", "veritabanını sıfırla"],
          "12": ["sesli komut modunu başlat", "12 numarayı çalıştır", "sesli kontrolü başlat"],
          "0": ["çık", "sistemi kapat", "programı kapat", "çıkış yap"]
}

def find_best_match(command):
   
    best_match = None
    highest_ratio = 0

    for key, phrases in menu_commands.items():
        for phrase in phrases:
            ratio = difflib.SequenceMatcher(None, command, phrase).ratio()
            if ratio > highest_ratio and ratio > 0.5:  # %60 eşleşme üzeri kabul edilir
                highest_ratio = ratio
                best_match = key

    return best_match


def voice_control():
    
    speak("Merhaba! ben Asena. Size nasıl yardımcı olabilirim?")
    print("🔊 Sesli asistan başlatıldı. Q tuşuna basarak çıkabilirsiniz.")

    while True:
        #Eğer "Q" tuşuna basıldıysa çıkış yapmak için bu kod
        if cv2.waitKey(1) & 0xFF == ord('q'):
            speak("Şimdilik gidiyorum daha sonra tekrar Görüşmek üzere!")
            sys.exit()

        command = recognize_speech()
        if command is None:
            continue

        # **Ana komutlar**

        if "1" in command:
            speak("Öğrencinin ID'sini ve ismini gir.")
            student_id = input("Öğrenci ID girin: ")
            name = input("Öğrenci ismini girin: ")
            attendance_manager.add_student(student_id, name)
            speak(f"{name} isimli öğrenci sisteme kaydedildi. Yüz verilerini kaydetmek ister misiniz?")
            reg = input("Yüz verisi kaydetmek ister misiniz? (e/h): ")
            if reg.lower() == "e":
                face_recognition.register_student(student_id, num_images=200)
                speak(f"{name} isimli öğrencinin yüzü sisteme kaydedildi.")
            else:
                speak(f"{name} isimli öğrenci kaydedildi ancak yüz verisi eklenmedi.")

        elif "2" in command:
            speak("Yeni bir yoklama tablosu oluşturuluyor... Yoklama başlatılıyor...")
            attendance_manager.create_new_attendance_table()
            face_recognition.predict_from_camera()

        elif "3" in command:
            speak("Mevcut yoklama tablolarını listeliyorum.")
            attendance_manager.list_attendance_tables()

        elif "4" in command or "yoklama tablosu göster" in command:
            speak("Hangi yoklama tablosunu görmek istiyorsun?")
            table_id = input("Görüntülemek istediğiniz yoklama tablosunun ID'sini girin: ")
            attendance_manager.view_attendance(table_id)
            speak(f"{table_id} numaralı yoklama tablosunu buldum. Bakabilirsiniz")

        elif "5" in command:
            speak("Hangi yoklama tablosuna öğrenci eklemek istiyorsun?")
            table_id = input("Tablo ID girin: ")
            speak("Eklemek istediğiniz öğrenci ID'sini söyleyin.")
            student_id = input("Öğrenci ID girin: ")
            attendance_manager.add_student_to_attendance(table_id, student_id)
            speak(f"{student_id} numaralı öğrenciyi yoklamaya eklendim.")

        elif "6" in command:
            speak("Silmek istediğiniz öğrenci ID'sini söyleyin.")
            student_id = input("Öğrenci ID girin: ")
            attendance_manager.delete_student(student_id)
            speak(f"{student_id} numaralı öğrenciyi sistemden sildim.")

        elif "7" in command:
            speak("Silmek istediğiniz yoklama tablosunun ID'sini söyleyin.")
            table_id = input("Tablo ID girin: ")
            attendance_manager.delete_attendance_table(table_id)
            speak(f"{table_id} numaralı yoklama tablosunu sildim.")

        elif "8" in command or "excel'e aktar" in command:
            table_id = input("Excel'e aktarmak istediğiniz yoklama tablosunun ID'sini girin: ")
            attendance_manager.export_attendance_to_excel(table_id)
            speak(f"{table_id} numaralı yoklama tablosunu Excel şeklinde kaydettim.")

        elif "9" in command or "tüm öğrencileri listele" in command:
            attendance_manager.list_all_students()
            speak("Tüm öğrenciler listelendi.")

        elif "10" in command or "öğrenciyi veritabanından sil" in command:
            student_id = input("Silmek istediğiniz öğrenci ID'sini girin: ")
            attendance_manager.delete_student(student_id)
            speak(f"{student_id} numaralı öğrenciyi sistemden sildim.")

        elif "11" in command or "veritabanını sıfırla" in command:
            speak("Tüm verileri silmek istediğinize emin misiniz?")
            confirm = recognize_speech()
            if "evet" in confirm:
                attendance_manager.reset_database()
                speak("Tüm veritabanı tabloları silindi ve yeniden başlatıldı.")
            else:
                speak("Veritabanı sıfırlama işlemi iptal edildi.")

        elif "12" in command or "sesli komut modu" in command:
            speak("hey! zaten ben buradayım. Sesli komut modu zaten açık!")


        elif "hava nasıl" in command:
            weather_info = get_weather()
            speak(weather_info)

        elif "saat kaç" in command:
            time_info = get_current_time()
            speak(time_info)

        elif "vikipedi" in command or "wikipedia" in command:
            speak("Ne hakkında bilgi almak istiyorsun?")
            topic = recognize_speech()
            if topic:
                result = search_wikipedia(topic)
                speak(result)

        elif "0" in command or "sistemi kapat" in command:
            speak("Şimdilik gidiyorum daha sonra tekrar Görüşmek üzere!")
            sys.exit()

        else:
            speak("Bu komutu anlayamadım. Menülerden birini seçebilirsiniz.")

if __name__ == "__main__":
    voice_control()