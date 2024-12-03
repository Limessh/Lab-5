import re
import csv

with open('task3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

id = re.findall(r'\s\d+\s', text)
surname = re.findall(r'[A-ZА-ЯЁ][a-zа-яё-]*', text)
email = re.findall(r'[\w._+-]+@[\w._+-]', text)
date = re.findall(r'\d{4}\-\d{2}\-\d{2}', text)
site = re.findall(r'https?://[a-zA-Z0-9.-]+/', text)

new_id=[]
for j in range (len(id)):
    if len(id[j])>8:
        k=len(id[j])//2
        new_id.append(id[j][:k])
        new_id.append(id[j][k:])
    elif (len(id[j])-len(id[j-1]))>1 or (len(id[j])-len(id[j+1]))>1:
        k=len(id[j])//2
        new_id.append(id[j][:k])
        new_id.append(id[j][k:])
    else:
        new_id.append(id[j])

new_file = []
for i in range (len(new_id)):
    record = [new_id[i],surname[i], email[i], date[i], site[i]]
    new_file.append(record)


with open('task3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Surname', 'Email', 'Registration Date', 'Site'])
    writer.writerows(new_file)

print("Данные успешно сохранены в файл task3.csv.")