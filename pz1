import json
import urllib.request

# Запит на курс євро за період 17–21 березня 2025 року
url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        data = json.loads(content)

        print("Дата\t\tКурс EUR")
        print("-" * 25)

        # Знаходимо максимальний курс для масштабування графіка
        max_rate = max(item["rate"] for item in data)

        for item in data:
            date = item["exchangedate"]
            rate = item["rate"]
            print(f"{date}\t{rate:.2f}")

        print("\nТекстовий графік зміни курсу:")

        for item in data:
            date = item["exchangedate"]
            rate = item["rate"]
            bar = "*" * int((rate / max_rate) * 50)  # Масштаб до 50 символів
            print(f"{date}: {bar} ({rate:.2f})")

except Exception as e:
    print("Помилка отримання даних:", e)
