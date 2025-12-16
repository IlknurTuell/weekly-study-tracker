import matplotlib.pyplot as plt  # Grafik çizmek için matplotlib'in pyplot modülünü aldık.

days = [
    "Pazartesi", "Salı", "Çarşamba", 
    "Perşembe", "Cuma", "Cumartesi", "Pazar"
]

study_data = {} # Tüm çalışma verilerinin saklanacağı sözlük.

print("\n*****HAFTALIK ÇALIŞMA TAKİP UYGULAMASI*****")

while True:
    print("\nGün seçiniz: ")
    for i, day in enumerate(days, 1):
        print(f"{i}. {day}")
    print("0.Çık ve grafiği göster") # Günleri numaralandırarak ekrana yazdırdık.

    choice = input("Seçimin: ")
    if choice == "0":
        break
    if not choice.isdigit() or not (1 <= int(choice) <= 7):
        print("Geçersiz işlem.")
        continue

    day = days[int(choice) - 1] 

    if day not in study_data:
        study_data[day] = {}

    lesson = input("Ders adı: ").strip() # strip: baştaki ve sondaki boşlukları temizler.
    minutes = int(input("Kaç dakika çalıştın: "))

    if lesson in study_data[day]:
        study_data[day][lesson] += minutes
    else:
        study_data[day][lesson] = minutes

daily_totals = []
for day in days:
    if day in study_data:
        total = sum(study_data[day].values())
    else:
        total = 0
    daily_totals.append(total)

weekly_totals = {}

for day in study_data:
    for lesson, minutes in study_data[day].items():
        if lesson in weekly_totals:
            weekly_totals[lesson] += minutes
        else:
            weekly_totals[lesson] = minutes

lessons = list(weekly_totals.keys())
minutes = list(weekly_totals.values())

plt.figure(figsize=(12,14))

plt.subplot(3, 1, 1)
plt.plot(days, daily_totals, marker="o")
plt.title("GÜNLÜK TOPLAM ÇALIŞMA SÜRESİ")
plt.ylabel("Dakika")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.bar(weekly_totals.keys(), weekly_totals.values())
plt.title("---HAFTALIK DERSLERE GÖRE ÇALIŞMA SÜRESİ---")
plt.ylabel("Dakika")
plt.xticks(rotation=45)

plt.subplot(3, 1, 3)
plt.pie(weekly_totals.values(), labels=weekly_totals.keys(), autopct="%1.1f%%" ,startangle=90) # %: float başlatır, 1: minimum karakter, .1: virgülden sonra bir basamak, f: float sayı, %%: ekrana % yazdırır.
plt.title("---HAFTALIK ÇALIŞMA SÜRESİ DAĞILIMI---")

plt.tight_layout()
plt.show()
