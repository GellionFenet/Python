#rightCounter = 0
#questionsCounter = 0
#uestions = ["сколько цветов у радуги? ", "какой язык мы изучаем? ", "сколько букв в русском алфавите? ", "команда для вывода в python: ", "сколько месяцев в году? "]
#ightAnswers = ["7", "python", "33", "print", "12"]
#while questionsCounter < len(questions):
#   answer = input(questions[questionsCounter])
#   if answer.lower() == rightAnswers[questionsCounter]:
#       rightCounter += 1
#      print('Вы ответили верно.')
#    else:
#       print('Вы ответили неверно.')
#   questionsCounter += 1
#print(f"вы набрали баллов: {rightCounter}") 

#import random
#zz = ["овен", "телец", "близнецы", "рак","лев", "дева","весы", "скорпион","стрелец", "козерог","водолей", "рыбы",]
#sovpad = 0
#timeList = ["Сегодня", "Завтра", "Очень скоро"]
#eventList = ["вы встретите", "с вами случится", "вы найдёте"]
#objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]
#while True:
#    while sovpad == 0:
#        otvet = input("введите знак Зодиака ")
#        for i in range(len(zz)):
#            if otvet == zz[i]:
#                sovpad+=1
#                continue
#        if sovpad < 1: 
#            print("Введите настоящий ЗЗ. ")
#    time = timeList[random.randint(0, len(timeList) - 1)]
#    event = eventList[random.randint(0, len(eventList) - 1)]
#    object = objectList[random.randint(0, len(objectList) -1)]
#    print(time + " " + event + " " + object)
#    next = input("хотите попробовать ещё раз? ")
#    if next.lower() == "да" or next.lower() == "yes":
#        sovpad = 0
#        continue
#    else:
#        print("Приходите ещё за новыми предсказаниями!")
#        break