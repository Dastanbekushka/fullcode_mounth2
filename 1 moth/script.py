money = 5000
password = 123

number = int(input("Введите пароль! "))

if number == password:
    question = int(input("1. Взять деньги! 2. Посмотреть счет! "))
    if question == 1:
        numberMoney = int(input("Какую сумму хотяте взять? "))
        if numberMoney > money:
            print("Недостаточно средст!")
        else:
            money = money - numberMoney
            print("Вы сняли! ", numberMoney)
            print( "Остаток средст:",  money)
    elif question == 2:
        print("У вас на счету: ", money)
    else:
        print("Такой команды нет!")

else:
    print("Пароль неправильный!")