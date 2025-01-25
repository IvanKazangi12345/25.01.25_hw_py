meters = int(input("Введите кол-во метров: "))
choise = int(input("Выберите: 1 - дюймы, 2 - мили, 3 - ярды: "))

if choise == 1:
    print(meters * 39.37)
elif choise == 2:
    print(meters * 0.000621371)
elif choise == 3:
    print(meters * 1.09)
else:
    print("Error")


num = input("Введите шестизначное число: ")

if (len(num) != 6 or not num.isdigit()):
    print("Error")
else:
    firstHalf = num[:3]
    secondHalf = num[3:]
    sumFirst = sum(int(digit) for digit in firstHalf)
    sumSecond = sum(int(digit) for digit in secondHalf)
    if (sumFirst == sumSecond):
        print(f"{num} - счастливое число")
    elif (sumFirst != sumSecond):
        print(f"{num} - не счастливое число")
    