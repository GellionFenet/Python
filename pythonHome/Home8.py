text = input("Введите текст:\n").lower()
word = input("Введите слово, которое нужно найти:\n").lower()
if text.find(word) != -1:
    poz = text.find(word)
    print(f"Это слово есть в тексте. Оно находится на позиции:", poz + 1)
else: 
    print("Такого слова нет в тексте.")