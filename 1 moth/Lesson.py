"""
SUM
"""

# number = {1,2,3,4,5}
#
# def summ123(n):
#     x = 0
#     for i in n:
#         x += i
#     return x
# print(summ123(number))


"""
MIN
"""
# number = {1,2,3,4,5}

# def min123(n):
#     x = tuple(n)
#     c = x[0]
#     for i in n:
#         if i < c:
#             c = i
#     return c
#
# print(min123(number))


"""
MAX
"""
# number = {1,2,3,4,5}

# def min123(n):
#     x = list(n)
#     c = x[0]
#     for i in n:
#         if i > c:
#             c = i
#     return c
#
# print(min123(number))


"""
LEN
"""
# number = [5,3,2,6,8,4,5,9]

# def len123(n):
#     x = 0
#     for i in n:
#         x += 1
#     return x
#
# print(len123(number))

"""
ABS
"""

# x = -1000
# def abs123(n):
#     num = 0
#     if n < 0:
#         num = n - n - n
#     else:
#         num = n
#     return num
# print(abs123(x))


"""
TUPLE
"""


# number = {5,3,2,6,8,4,5,9}
#
# def tuple123(n):
#     x = ()
#     for i in n:
#         x = x + (i,)
#     return x
#
# print(tuple123(number))



# n = [
#     {'dastan' : 100},
#     {'kanimet' : 55},
#     {'zhuma' : 11},
#     {'kelsinai': 20}
# ]
#
# def average(k: list[dict]):
#     sun = 0
#     for i in k:
#         for key, value in i.items():
#             sun += value
#     return sun/len(k)
# print(average(n))



# a = 4
# b = 80
# c = 44
#
# def search(n):
#     attems = 0
#     total = 50
#     while True:
#         attems += 1
#         if n
#
#
#
# print(search(a))
# print(search(b))
# print(search(c))



# x = lambda a, b: a + b
# k = lambda a, b: a - b
# n = lambda a, b: a * b
# m = lambda a, b: a / b
#
# print(x(2,3))
# print(k(2,3))
# print(n(2,3))
# print(m(2,3))
# import random
#
# def ran(n):
#     c = []
#     print(type(c))
#     for i in range(n):
#         x = random.randint(0, 10)
#         c.append(x)
#     return c
#
# print(ran(30)

# x = lambda a: a * 2 if a % 2 == 0 else a * 3
# print(x(5))


a = [1,2,3,4,5,6,7,8,9,10]

"""
Бинарный алгоритм
Линейный алгоритм
"""


#
# def get_middle(s):
#     length = len(s) // 2
#     if len(s) % 2 == 0:
#         return s[length - 1] + s[length]
#     else:
#         return s[length]
# print(get_middle('dasta'))




# def process_args(*n):
#     total = 0
#     st = []
#     for i in n:
#         if isinstance(i, int) and i > 0:
#             total += i
#         elif isinstance(i, str) and len(i) > 3:
#             st.append(i)
#
#     return (total, st)
#
# print(process_args(10, -5, "hi", "hello", 3, "world", 0))



# def run(k, *n):
#     for i in n:
#         print(k, i)
#
# print(run('hello', 'dastan', 'alym', 'darika'))


# def my_function(**myvar):
#     print(myvar)
#     print('type: ', type(myvar) )
#     print('name: ', myvar['name'])
#     print('age: ', myvar['age'])
#     print('city: ', myvar['city'])
#
#
# my_function(name = "Tobias", age = 30, city = "Bergen")