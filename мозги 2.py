import random
for i in range(int(input("Введите количество сдающих: "))):
    dictator = {}
    with open("Вопросы.txt", "r", encoding="UTF-8") as file:
        lines = [line.rstrip() for line in file]
    for i in lines:
        a = i.split("? ")
        wopros = a[0] + "?"
        otvet = a[1]
        dictator.update({wopros : otvet})
    wors = random.choice(list(dictator))
    print(wors)
    if input("Нажмите Enter  ").lower() == str(dictator[wors]).lower():
        print("Молодец")
    else:
        print("Вы тупой!!!")
        print(dictator[wors])