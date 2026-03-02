# en_to_ru = {
#     'q':'й', 'w':'ц', 'e':'у', 'r':'к', 't':'е', 'y':'н', 'u':'г', 'i':'ш', 'o':'щ', 'p':'з',
#     '[':'х', ']':'ъ','a':'ф', 's':'ы', 'd':'в', 'f':'а', 'g':'п', 'h':'р','j':'о', 'k':'л',
#     'l':'д',';':'ж', "'":'э', 'z':'я', 'x':'ч', 'c':'с', 'v':'м', 'b':'и','n':'т', 'm':'ь',
#     ',':'б', '.':'ю',
#
#     'й':'q', 'ц':'w', 'у':'e', 'к':'r', 'е':'t', 'н':'y','г':'u', 'ш':'i', 'щ':'o', 'з':'p',
#     'х':'[', 'ъ':']','ф':'a', 'ы':'s', 'в':'d', 'а':'f', 'п':'g', 'р':'h','о':'j', 'л':'k',
#     'д':'l', 'ж':';', 'э':"'",'я':'z', 'ч':'x', 'с':'c', 'м':'v', 'и':'b','т':'n', 'ь':'m',
#     'б':',', 'ю':'.'
# }
# x = input('Введите слово: ')
# result = ''
#
# for i in x:
#     if i in en_to_ru:
#         result += en_to_ru[i]
#     else:
#         print('Невозможно перевести!')
#         break
# print(result)
#
# balance = 10000
# n = 0
#
# while n != 4:
#     print('1 - Проверить баланс')
#     print('2 - Снять деньги')
#     print('3 - Пополнить счет')
#     print('4 - Выход')
#
#     n = int(input('Введите номер действия: '))
#     money = 0
#
#     if n == 1:
#         print(f'Ваш баланс: {balance}')
#     elif n == 2:
#         money = int(input('Сколько хотите снять? '))
#         balance = balance - money
#         print(f'Ваш баланс: {balance}')
#         money = 0
#     elif n == 3:
#         money = int(input('Кукаю сумму хотите пополнить? '))
#         balance += money
#         print(f'Ваш баланс: {balance}')
#         money = 0
#     else:
#         print('Спасибо за использование банкомата!')
#         break


#
# my_students = ('math', '666', '%%%%%%', 'lkgahjhgjae32534645634')
# number_c = 0
# abc_c = 0
# symbol_c = 0
#
# for i in my_students:
#     for j in i:
#         if j.isdigit():
#             number_c += 1
#         elif j.isalpha():
#             abc_c += 1
#         elif j.isprintable():
#             symbol_c += 1
# else:
#     print(f'''
# abc_c = {abc_c}
# symbol_c = {symbol_c}
# number_c = {number_c}
# ''')



# tpl = (1,2,3,4,5,6,7,8,9)
# x = tpl[0]
# n = tpl[0]
#
# for i in tpl:
#     if i < n:
#         n = i
#     if x < i:
#         x = i
#
# print(x)
# print(n)
#
# print(tpl[0:9:2])
#
# shop = ["apple", "banana", "milk", "bread"]
#
# shop.append("eggs")
# print(shop)
# shop.insert(1, "cheese")
# print(shop)
# shop.extend(["juice", "rice"])
# print(shop)
# print(shop.count("apple"))
# print(shop.index('milk'))
# new_shop = shop.copy()
# print(new_shop)
# new_shop.remove("banana")
# print(new_shop)
# new_shop.pop(0)
# print(new_shop)
# new_shop.reverse()
# print(new_shop)
# new_shop.clear()
# print(new_shop)


# my_profile = {
#
#     "username":"@islam",
#     "phone_number":"+9962216326731",
#     "email":"sasakdjk@gmail.com"
# }
#
# my_profile['age'] = 1000
# my_profile['email'] = 'robot@gmail.com'
# print(f"""
# username: {my_profile["username"]}
# phone_number: {my_profile["phone_number"]}
# email: {my_profile["email"]}
# age: {my_profile["age"]}
# """)


# bank_account = {
#     "name":"dastan",
#     "password":"123",
#     "balance":1000
# }
# credit = 0
# attems = 3
# while attems != 0:
#     if attems == 0:
#         print("Вы полностью исчерпали попытки!")
#         break
#     name = input("Напишите имя: ")
#     password = input("Напишите пароль: ")
#     if name == bank_account["name"] and password == bank_account["password"]:
#         number_code = 0
#         while number_code != 5:
#             print('1. Показать баланс')
#             print('2. Пополнить баланс')
#             print('3. Снять деньги')
#             print('4. Взять кредит')
#             print('5. Выход')
#             number_code = int(input("Выберите пункт: "))
#
#             if number_code == 1:
#                 print(f"""Имя: {bank_account['name']}\nПароль: {bank_account['password']}\nБаланс: {bank_account['balance']}""")
#             elif number_code == 2:
#                 summa = int(input("Напишите сумму для пополнения: "))
#                 if summa <= 0:
#                     print('Неностаточно средств!')
#                 else:
#                     bank_account["balance"] += summa
#                     print(f'Ваша сумма пополнилась: {bank_account["balance"]}')
#             elif number_code == 3:
#                 if bank_account["balance"] > 0:
#                     minus = int(input("Какую сумму хотите снять: "))
#                     if  minus > bank_account["balance"] or minus < 0:
#                         print("Неностаточно средств")
#                     else:
#                         bank_account["balance"] -= minus
#                         print(f'Остаток на счету: {bank_account["balance"]}')
#                 else:
#                     print(f'На вашем счету {bank_account["balance"]}')
#             elif number_code == 4:
#                 print(f'Кредит дается от 5000 до 20000. Добавляется 15%')
#                 credit = int(input('Какую сумму хотите взять; '))
#                 if credit < 5000 or credit > 20000:
#                     print('Сумма дожна быть от 5000 до 20000')
#                 elif (credit >= 5000) and credit <= 20000:
#                     bank_account["Credit"] = credit
#                     bank_account["balance"] += credit
#                     print(f'Вы взяли кредит в размере {bank_account["Credit"]}.\nВаш баланс {bank_account["balance"]}')
#                     m = credit * 0.15
#                     print(f'К вашей сумме добавится {int(m)}. Итого: {int(bank_account["Credit"] + m)} будете оплачивать')
#         else:
#             print(f"Вы вышли!")
#             break
#     else:
#         attems -= 1
#         if attems != 0:
#             print(f'''У вас осталось {attems} попытки. Попробуйте еще раз!''')
#


# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]
#
# x = set(a)
# c = set(b)
#
# print(x & c)



# students = {
#     "Ali": 85,
#     "Vika": 90,
#     "John": 78
# }
#
# name = input("Enter student name: ")
# balance = int(input("Enter balance: "))
#
# students[name] = balance
#
# print(students)
#
# best_student = ''
# max_balance = 0
#
# for key, value in students.items():
#     if value > max_balance:
#         best_student = key
#         max_balance = value
#
# total = 0
# for i in students:
#     total += students[i]
#
# print(f'Лучший ученик: {best_student}. Балл студента: {max_balance}.')
# print('Средний балл студента: ', int(total / len(students)))






"""
1.id()
2.sum(int, tuple, list, set)
3.min(tuple, list, set)
4.max(tuple, list, set)
5.len(str, list, set, dict)
6.round(float, int)
7.sorted(list, tuple, set)
8. abc()
"""

"""
reverse=True
"""

# def minus(a, b):
#     return a - b
# def plus(a, b):
#     return a + b
# def multi(a, b):
#     return a * b
# def div(a, b):
#     return a / b
#
# print(minus(2, 1))
# print(plus(2, 1))
# print(multi(2, 1))
# print(div(2, 1))

#
# i = [1,2,3]
# print(list(i))

# def s(a,b):
#     return a*b
#
# x = int(input())
# z = int(input())
#
# print(s(x,z))
