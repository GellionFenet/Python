counter = 0
#Первый вопрос
answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Второй вопрос
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Пайтон":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Третий вопрос
answer = input("2 * 2?\n")
if answer == "4" or answer == "Четыре":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
 #Четвертый вопрос
answer = input("Как звали отца Пушкина?\n")
if answer == "Сергей" or answer == "сергей":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
print(f"вы набрали баллов {counter}")