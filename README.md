# **Gerçek Zamanlı Yüz Tanıma ile Yoklama Sistemi**

- **📌 Yapay zeka destekli yüz tanıma & SQLite veritabanı ile gelişmiş yoklama sistemi!**  
- **📸 Kameradan otomatik öğrenci tanıma & yoklama kaydetme, manuel ekleme & Excel'e aktarma özellikleri!** 
- **🎙️ Tamamen SES ile kontrol edilebilir!** 
- **🔥 Tüm yoklamalar ayrı tablolar halinde kaydedilir & geriye dönük sorgulanabilir!**  

---

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="100">
</div>
<br><br>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="100">
</div>
<br><br>    


---

## 🚀 **Özellikler**

- ✅ **Gerçek Zamanlı Yüz Tanıma** – Kamera ile öğrenci yüzlerini algılar ve **otomatik yoklama alır!**  
- ✅ **Sesli Komut Sistemi** – **Tamamen sesle yönetilebilen bir asistan entegre edildi!**  
- ✅ **Tam Veritabanı Desteği** – **Öğrenciler ve yoklamalar SQLite'de saklanır, geçmiş yoklamalara erişilebilir.**  
- ✅ **Dinamik Yoklama Tabloları** – **Her ders için yeni yoklama tablosu otomatik oluşturulur.**  
- ✅ **Manuel Yoklama Ekleme & Düzeltme** – **Öğrencileri yoklamaya elle ekleyebilir/silebiliriz!**  
- ✅ **Tüm Yoklamaları Listeleme** – **Bugüne kadar alınan tüm yoklamalar tek bir komutla listelenebilir.**  
- ✅ **Excel’e Aktarma** – **Yoklama tabloları Excel formatında dışa aktarılabilir!**  
- ✅ **Vikipedi & Hava Durumu Desteği** – **Sistem, hava durumu bilgisini verebilir & Wikipedia'dan özet bilgiler çekebilir!**  

<br><br> 

---

## 🔊 **YENİ ÖZELLİK: Sesli Asistan Entegrasyonu!** 🎤

Projeye tamamen **sesli asistan entegrasyonu** eklendi! Artık sistemle konuşarak işlem yapabilirsiniz!  

### 🎙 **Örnek Komutlar:**

✅ **Gerçek zamanlı yoklama al →** "Şimdi yoklama al", "Sınıfta yoklama yap", "Yüz tanıma ile yoklama başlat"  
✅ **Öğrenci kaydı yap →** "Yeni öğrenci ekle", "Öğrenci kaydet", "Sisteme öğrenci ekleyelim"  
✅ **Saat kaç? →** "Bana saati söyler misin?", "Şu an saat kaç?"  
✅ **Bugün hava nasıl? →** "Bugün hava nasıl?", "İstanbul’da hava kaç derece?", "Hava durumu nedir?"  
✅ **Vikipedi’den bilgi ver →** "Yapay zeka hakkında bilgi ver", "Vikipedi’de kuantum mekaniği ara"  
✅ **Menüyü yönet →** "Bir numaralı işlemi çalıştır", "5. seçeneği seç", "Tüm yoklama tablolarını göster"  
✅ **Q tuşuna basarak anında çıkabilirsiniz!**  

---

## 📌 **Kullanılan Teknolojiler ve Kütüphaneler**

- **Python 3.9+** – Projenin ana dili  
- **OpenCV** – Görüntü işleme ve kamera desteği için  
- **Dlib** – **Yüz tanıma modeli** (HOG & CNN tabanlı)  
- **NumPy** – Matematiksel işlemler için  
- **SQLite** – **Hafif & entegre veritabanı yönetimi**  
- **Pandas** – **Verileri analiz etmek & Excel'e aktarmak için**  
- **OpenPyXL** – **Excel dosyaları oluşturmak için**  
- **SpeechRecognition** – **Sesli komutları algılamak için**  
- **pyttsx3** – **Asistanın konuşmasını sağlamak için**  
- **Wikipedia-API** – **Vikipedi’den veri çekmek için**  
- **Requests** – **Hava durumu verisi almak için**  

---
<br><br>
<div align="center">
   <img src="https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/3b4607a1-1cc6-41f1-926f-892ae880e7a5" width="500">
</div>
<br><br>

## 🔧 **Kurulum & Çalıştırma**

### 1️⃣ **Gerekli Kütüphaneleri Kur**

Aşağıdaki komutları çalıştırarak eksik kütüphaneleri yükleyin:

```bash
pip install opencv-python dlib numpy pandas openpyxl
```

---

### 2️⃣ **Veritabanını & Dosya Yapısını Hazırla**

📂 İlk çalıştırmada, **otomatik olarak gerekli klasörler ve veritabanı oluşturulacaktır.**  

```bash
python main.py
```

---

## 📸 **Nasıl Kullanılır?**

### **📝 Öğrenci Kaydı Yap**

📌 **Yeni bir öğrenci eklemek için:**

```bash
1 - Öğrenci Kaydı Yap
```

1️⃣ **Öğrenci ID ve adını gir.**  
2️⃣ **Öğrenci yüz kaydını almak için 'e' seçeneğini seç.**  
3️⃣ **Kamera açılacak ve öğrencinin yüz görüntüleri kaydedilecek.**  
4️⃣ **Kayıt tamamlandığında öğrenci sistemde saklanır.**  

---

### **📌 Gerçek Zamanlı Yoklama Al (Yeni Tablo Oluşturur!)**

📌 **Gerçek zamanlı yoklama almak için:**

```bash
2 - Gerçek Zamanlı Yoklama Al
```

- Sistem **otomatik olarak yeni bir yoklama tablosu oluşturur.**  
- Kamera açılır ve kayıtlı öğrencileri tanır.  
- Tanınan öğrenciler yoklama listesine eklenir.  

---

### **📊 Yoklama Tablolarını Yönet**

📌 **Tüm yoklama tablolarını listele:**

```bash
3 - Mevcut Yoklama Tablolarını Listele
```

📌 **Belirli bir yoklama tablosunu görüntüle:**

```bash
4 - Belirli Bir Yoklama Tablosunu Görüntüle
```

📌 **Belirli bir yoklama tablosuna elle öğrenci ekle:**

```bash
5 - Belirli Bir Yoklama Tablosuna Elle Öğrenci Ekle
```

📌 **Belirli bir yoklama tablosundan öğrenci sil:**

```bash
6 - Belirli Bir Yoklama Tablosundan Öğrenci Sil
```

📌 **Belirli bir yoklama tablosunu sil:**

```bash
7 - Belirli Bir Yoklama Tablosunu Sil
```

📌 **Belirli bir yoklama tablosunu Excel'e aktar:**

```bash
8 - Belirli Bir Yoklama Tablosunu Excel'e Aktar
```

📌 **Tüm öğrencileri listele:**

```bash
9 - Tüm Öğrencileri Listele
```

📌 **Öğrenciyi veritabanından sil:**

```bash
10 - Öğrenciyi Veritabanından Sil
```

📌 **Tüm verileri sıfırla:**

```bash
11 - Tüm Veritabanı Tablolarını Sil ve Yeniden Başlat
```

📌 **Çıkış yap:**

```bash
0 - Çıkış
```

<br><br>
<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212751818-13da6fd2-27ca-45c4-9c64-3940ccfa6fd3.gif" width="300">
</div>
<br><br>

## 📂 **Proje Dosya Yapısı**

```
📂 AttendanceSystem
 ┣ 📜 main.py                # Ana program (menü arayüzü)
 ┣ 📜 attendance_manager.py   # Yoklama işlemleri (Veritabanı Yönetimi)
 ┣ 📜 face_recognition.py     # Gerçek zamanlı yüz tanıma & öğrenci kaydı
 ┣ 📜 prepare_data.py         # Verilerin düzenlenmesi
 ┣ 📜 requirements.txt        # Gerekli kütüphaneler
 ┗ 📂 data
    ┗ 📂 train                # Kayıtlı öğrenci yüz verileri
```

---

## 📌 **Demo & Önizleme**

![Demo](https://user-images.githubusercontent.com/demo.gif)

---

## 🛠️ **Sorun Giderme**

📌 **Eksik Kütüphane Hatası:**

```bash
ModuleNotFoundError: No module named 'dlib'
```

Çözüm:

```bash
pip install dlib
```

📌 **Excel Kaydetme Hatası:**

```bash
No module named 'openpyxl'
```

Çözüm:

```bash
pip install openpyxl
```

📌 **Dlib Model Hatası:**

Dlib model dosyalarının eksik olup olmadığını kontrol et!  

---

## 🤝 **Benimle İletişime Geçerek Katkıda Bulun**

🎯 **Projeyi beğendiysen yıldız bırakmayı unutma!** ⭐  

---

🚀💡🔥
