# 🎭 **Gerçek Zamanlı Yüz Tanıma ile Yoklama Sistemi**

> **📌 Yapay zeka destekli yüz tanıma & SQLite veritabanı ile gelişmiş yoklama sistemi!**  
> **📸 Kameradan otomatik öğrenci tanıma & yoklama kaydetme, manuel ekleme & Excel'e aktarma özellikleri!**  
> **🔥 Tüm yoklamalar ayrı tablolar halinde kaydedilir & geriye dönük sorgulanabilir!**  

---
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fideas%2Fface-recognition%2F956526599412%2F&psig=AOvVaw2qF2op58TitoAt28VhTSB_&ust=1742301506162000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCKD1uYaRkYwDFQAAAAAdAAAAABAJ

## 🚀 **Özellikler**

✅ **Gerçek Zamanlı Yüz Tanıma** – Kamera ile öğrenci yüzlerini algılar ve **otomatik yoklama alır!**  
✅ **Tam Veritabanı Desteği** – **Öğrenciler ve yoklamalar SQLite'de saklanır, geçmiş yoklamalara erişilebilir.**  
✅ **Dinamik Yoklama Tabloları** – **Her ders için yeni yoklama tablosu otomatik oluşturulur.**  
✅ **Manuel Yoklama Ekleme & Düzeltme** – **Öğrencileri yoklamaya elle ekleyebilir/silebiliriz!**  
✅ **Tüm Yoklamaları Listeleme** – **Bugüne kadar alınan tüm yoklamalar tek bir komutla listelenebilir.**  
✅ **Excel’e Aktarma** – **Yoklama tabloları Excel formatında dışa aktarılabilir!**  

---

## 📌 **Kullanılan Teknolojiler ve Kütüphaneler**

- **Python 3.9+** – Projenin ana dili  
- **OpenCV** – Görüntü işleme ve kamera desteği için  
- **Dlib** – **Yüz tanıma modeli** (HOG & CNN tabanlı)  
- **NumPy** – Matematiksel işlemler için  
- **SQLite** – **Hafif & entegre veritabanı yönetimi**  
- **Pandas** – **Verileri analiz etmek & Excel'e aktarmak için**  
- **OpenPyXL** – **Excel dosyaları oluşturmak için**  

---

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

---

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
