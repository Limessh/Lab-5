import re
import csv

# Задание №1
with open("task1-ru.txt", "r", encoding="utf-8") as file:
    text = file.read()

words_dot = re.findall(r"\b[а-яА-ЯёЁa-zA-Z]+\b(?=\.)", text)

numbers = re.findall(r"\b\d+\,\d+\b", text)

print("Слова, после которых стоит точка:")
print(words_dot)
print("Дробные числа:")
print(numbers)


# Задание №2
with open("task2.html", "r", encoding="utf-8") as file:
    text = file.read()

pixel = re.findall(r"\b\d+px\b", text)

print("Значения в пикселях:")
print(pixel)


# Задание №3
with open("task3.txt", "r", encoding="utf-8") as file:
    text = file.read()

id = re.findall(r"\s\d+\s", text)
surname = re.findall(r"[A-ZА-ЯЁ][a-zа-яё-]*", text)
email = re.findall(r"[\w._+-]+@[\w._+-]", text)
date = re.findall(r"\d{4}\-\d{2}\-\d{2}", text)
site = re.findall(r"https?://[a-zA-Z0-9.-]+/", text)

new_id = []
for j in range(len(id)):

    if len(id[j]) > 8:
        k = len(id[j]) // 2
        new_id.append(id[j][:k])
        new_id.append(id[j][k:])
    elif (len(id[j]) - len(id[j - 1])) > 1 or (len(id[j]) - len(id[j + 1])) > 1:
        k = len(id[j]) // 2
        new_id.append(id[j][:k])
        new_id.append(id[j][k:])
    else:
        new_id.append(id[j])

new_file = []
for i in range(len(new_id)):
    record = [new_id[i], surname[i], email[i], date[i], site[i]]
    new_file.append(record)

with open("task3.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Surname", "Email", "Registration Date", "Site"])
    writer.writerows(new_file)

print("Данные успешно сохранены в файл task3.csv.")


# Дополнительное задание
with open("task_add.txt", "r", encoding="utf-8") as file:
    text = file.read()

dates = re.findall(r"\s(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})", text)
emails = re.findall(r"\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})", text)
sites = re.findall(r'\s(https?://[a-zA-Z0-9.-]+)', text)

print("Найденные даты:")
for date in dates:
    print(date)
print("Найденные адреса электронной почты:")
for email in emails:
    print(email)
print("Найденные адреса сайтов:")
for site in sites:
    print(site)
