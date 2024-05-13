student = ["Вася", "Петя"]
while True:
    print("\n----------")
    answer = int(input("выберите действие\n"
                    "1-добавить студента\n"
                    "2-удалить студента по номеру\n"
                    "3-удалить студента по имени\n"
                    "4-посмотреть весь список студентов\n"
                    "0-выйти из программы\n"))
    if answer not in [1, 2, 3, 4, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента ")
        student.append(newStudent)
    elif answer == 2:
        delNumber = int(input("введите номер студента для удаления "))
        student.pop(delNumber)
    elif answer == 3:
        delName = input("введите имя студента для удаления ")
        student.remove(delName)
    elif answer == 4:
        print(student)
    elif answer == 0:
        break
    print("\n")