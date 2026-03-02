"""
json, txt, cvv
"""
"""
r --> reading --> read(Читает все и берет все), readline(Берет первую строку полностью), readlines(Берет все и делает список)
w --> writing(Открывает навый файл и добавляет значение нписанный нами), writelines()
x --> 

"""

import csv

with open('Книга1.csv', 'r') as file:
    reader = csv.reader(file)
    print(next(reader))

# with open('students.txt', 'w') as file:
#     file = file.writelines('dastan')
#     print(file)

# def add_student(name, age, grade):
#     with open('db/students.txt', 'a') as file:
#         return file.write(name + '|' + age + '|' + grade + '\n')
#
#
# def delete_student(name):
#     with open('db/students.txt', 'r') as file:
#         lines = file.readlines()
#         print(lines)
#         with open('db/students.txt', 'w') as f:
#             for i in lines:
#                 if name in i.strip("\n"):
#                     ...
#                 else:
#                     f.write(i)
#
#
# def info_file():
#     with open('db/students.txt', 'r') as file:
#         name = file.name
#         students_count = 0
#         for i in list(file.readlines()):
#             if i.strip("\n"):
#                 students_count += 1
#         return f"{name}|{students_count}"
#
#
# print(info_file())





