from datetime import datetime

Деньрождения = input("Введите дату рождения(день...месяц...год): ")
конв = datetime.strptime(Деньрождения, "%d_%m_%Y")
сегодня = datetime.now()
день = сегодня - конв

print("Вы живете " + str(день.сегодня) + " дней.")