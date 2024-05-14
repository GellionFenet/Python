counter = 0
#Первый вопрос
answer = input("В каком мы городе?\n")
if answer == "Таганрог" or answer == "таганрог":
 counter = counter + 1
 print("Вы ответили верно!")
else:
 print("вы ответили не верно!")
#Второй вопрос
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Питон":
 counter = counter + 1
 print("Вы ответили верно!")
else:
 print("Вы ответили не верно!")
#Третий вопрос
answer = input("Вы человек?\n")
if answer == "Да" or answer == "да":
 counter = counter + 1
 print("Вы ответили верно!")
else:
 print("Вы ответили не верно!")
 #Четвертый вопрос
answer = input("Hello, ???\n")
if answer == "World" or answer == "world":
 counter = counter + 1
 print("Вы ответили верно!")
else:
 print("Вы ответили не верно!")
print(f"Вы набрали {counter} баллов")