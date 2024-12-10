import random
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
print("Нажмите Enter")
while input() == "":
    print(dictator[wors])