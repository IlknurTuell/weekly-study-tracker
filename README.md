# weekly-study-tracker

# 📊 Haftalık Çalışma Takip Uygulaması

Bu proje, kullanıcıların hafta boyunca yaptıkları çalışmaları **gün** ve **ders bazında** takip etmelerini sağlayan, Python ile geliştirilmiş basit ama etkili bir konsol uygulamasıdır.

Girilen veriler analiz edilerek farklı grafikler yardımıyla görselleştirilir. Proje, özellikle **Python temellerini**, **sözlük yapısını** ve **veri görselleştirmeyi** öğrenmek amacıyla hazırlanmıştır.

---

## 🚀 Özellikler

* Haftanın günlerinden seçim yapabilme
* Ders adı ve çalışma süresi girme
* Aynı gün ve ders için tekrar girilen süreleri otomatik toplama
* Çalışma verilerini grafiklerle analiz etme:

  * 📈 Günlük toplam çalışma süresi (çizgi grafik)
  * 📊 Derslere göre haftalık toplam süre (çubuk grafik)
  * 🥧 Haftalık çalışma süresi dağılımı (pasta grafik)

---

## 🛠 Kullanılan Teknolojiler

* Python
* Matplotlib

---

## 📂 Kullanılan Veri Yapısı

Çalışma verileri iç içe sözlük (nested dictionary) yapısı ile saklanmaktadır:

```python
{
  "Pazartesi": {
      "Matematik": 60,
      "Fizik": 30
  },
  "Salı": {
      "Matematik": 45
  }
}
```

---

## ▶️ Programı Çalıştırma

1. Gerekli kütüphaneyi yükleyin:

```bash
pip install matplotlib
```

2. Programı çalıştırın:

```bash
python study_tracker.py
```

3. Gün, ders ve dakika bilgilerini girin.
4. `0` seçeneği ile çıkış yaparak grafiklerin oluşmasını sağlayın.

---

## 🎯 Projenin Amacı

Bu proje ile:

* Python döngüleri ve koşullu yapılar pekiştirilmiştir
* Sözlük (dictionary) kullanımı pratiği yapılmıştır
* Kullanıcı girdisi kontrolü öğrenilmiştir
* Matplotlib ile temel veri görselleştirme uygulanmıştır

Proje, **Python öğrenme sürecinde yapılan bir alıştırma ve mini analiz uygulamasıdır**.

## 📊 Aşağıda uygulamanın çalıştırılması sonucu elde edilen bir ekran çıktısı gösterilmiştir.
<img width="1536" height="754" alt="Example-1" src="https://github.com/user-attachments/assets/4ebc2bb5-e41b-43c7-a0bf-0a08f38b1782" />



