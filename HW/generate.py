import csv
import random
import os
import sys

COLUMNS = ["ФИО", "Спортивное звание", "Жим лежа, кг", "Становая тяга, кг", "Присед, кг"]

LAST_NAMES = ["Смирнов", "Сафонов", "Щербаков", "Кондратенко", "Иванов", "Попов", "Орлов", "Королёв", "Баженов", "Тетерин"]

FIRST_NAMES = ["Родион", "Павел", "Михаил", "Александр", "Артём", "Владимир", "Сергей", "Роман", "Григорий", "Василий"]

MIDDLE_NAMES = ["Дмитриевич", "Константинович", "Игоревич", "Сергеевич", "Максимович", "Андреевич", "Никитич", "Михайлович", "Артемович", "Егорович"]

SPORT_RANKS = ["Без разряда", "III разряд", "II разряд", "I разряд", "КМС", "МС", "МСМК"]


def generate_row():

    return {
        "ФИО": str(random.choice(LAST_NAMES)) + " " + str(random.choice(FIRST_NAMES)) + " " + str(random.choice(MIDDLE_NAMES)), #https://docs.python.org/3/library/random.html
        "Спортивное звание": random.choice(SPORT_RANKS), #https://docs.python.org/3/library/random.html
        "Жим лежа, кг": random.randint(60, 200),
        "Становая тяга, кг": random.randint(80, 300),
        "Присед, кг": random.randint(70, 250),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(67)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

