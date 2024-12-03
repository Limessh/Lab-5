import re

with open('task2.html', 'r', encoding='utf-8') as file:
    text = file.read()

pixel = re.findall(r'\b\d+px\b', text)

print("Значения в пикселях:")
print(pixel)