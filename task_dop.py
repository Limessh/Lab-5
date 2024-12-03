import re

with open('task_add.txt', 'r', encoding='utf-8') as file:
    text = file.read()

dates = re.findall(r'\s(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})',text)
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', text)
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