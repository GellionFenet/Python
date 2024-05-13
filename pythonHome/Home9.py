studentList = ["Вася", "Петя"]
markList = ["2", "5", "3", "4"]

while True:
    print("----------")
    answer = int(input("Выберите действие\n"
                    "1-добавить студента\n"
                    "2-удалить студента\n"
                    "3-удалить студента\n"
                    "4-посмотреть весь список студентов\n"
                    "5-посмотреть оценки\n"
                    "0-выйти из программы\n"))
    if answer not in [1, 2, 3, 4, 5, 0]:
        print("Такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("Введите имя студента ")
        studentList.append(newStudent)
    elif answer == 2:
        delNumber = int(input("Введите номер студента для удаления "))
        studentList.pop(delNumber)
    elif answer == 3:
        delName = input("Введите имя студента для удаления ")
        studentList.remove(delName)
    elif answer == 4:
        print(studentList)
    elif answer == 5:
        markName = input("Введите имя студента для вывода оценок ")
        indexStud = studentList.index(markName)
        Mark = markList[indexStud]
        print(Mark)
    elif answer == 0:
        break
    print("\n")