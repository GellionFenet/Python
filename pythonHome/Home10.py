import random
zz = ["как дела", "что делаешь", "ты где"]
sovpad = 0
KD = ["хорошо", "плохо"]
CHD = ["сплю", "учусь"]
TG = ["дома", "в колледже"]
while True:
    while sovpad == 0:
        vopr = input("Введите вопрос: ")
        for i in range(len(zz)):
            if vopr == zz[i]:
                sovpad+=1
                continue
        if sovpad < 1: 
            print("Введите другой вопрос. (как дела, что делаешь, ты где)")
    if vopr == zz[0]:
        otv = "У меня все " + KD[random.randint(0, len(KD) - 1)]
    elif vopr == zz[1]:
        otv = "Я сейчас " + CHD[random.randint(0, len(CHD) - 1)]
    elif vopr == zz[2]:
        otv = "В данный момент я " + TG[random.randint(0, len(TG) -1)]
    
    print(otv)
    next = input("поговорим ещё? ")
    if next.lower() == "да" or next.lower() == "yes":
        sovpad = 0
        continue
    else:
        print("Пока!")
        break