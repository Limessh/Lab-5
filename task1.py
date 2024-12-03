import re

with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words_dot = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b(?=\.)', text)

numbers = re.findall(r'\b\d+\,\d+\b', text)

print("Слова, после которых стоит точка:")
print(words_dot)

print("Дробные числа:")
print(numbers)