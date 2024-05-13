import random
print("добро пожаловать в игру камень ножницы бумага!")
playerScore = 0
botScore = 0
print("Введи количество раундов - ", end='')
rounds = int(input())
answer = input("Начать игру").lower()
for i in range(rounds):
    while True:
        print("1. Камень")
        print("2. Ножницы")
        print("3. Бумага")
        print("4. Змея")
        print("5. Спок")
        cmd = input("Выбери своего бойца: ").lower()

        if cmd == "1":
            answer = "к"
            break
        elif cmd == "2":
            answer = "н"
            break
        elif cmd == "3":
            answer = "б"
            break
        elif cmd == "4":
            answer = "з"
            break
        elif cmd == "5":
            answer = "с"
            break
        elif cmd == "0":    
            break
        else:
            print("Вы ввели не правильное значение")

    botAnswer = random.choice(["камень", "ножницы", "бумагу", "змею", "спок"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]

    if answer == botAnswer:
        print("Ничья")
    elif (answer == "к" and botAnswer == "н" or botAnswer == "з" ) or\
         (answer == "н" and botAnswer == "б" or botAnswer == "з") or \
         (answer == "б" and botAnswer == "к" or botAnswer == "с") or \
         (answer == "з" and botAnswer == "б" or botAnswer == "с") or \
         (answer == "c" and botAnswer == "к" or botAnswer == "н"):
        print("Ты победил!")
        playerScore += 1
    else: 
        print("Я победил!")
        botScore += 1
    print("Игрок ",playerScore," : ",botScore, "Бот")

if playerScore == botScore:
    print("Ничья по итогу ",rounds," раундов !")
elif playerScore > botScore:
    print("Ты победил по итогу",rounds,"раундов")     
else:
    print("Я победил по итогу ",rounds," раундов")
   