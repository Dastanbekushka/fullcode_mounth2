# """func 1"""
# from itertools import count
# from math import factorial
#
#
# def hello_world():
#     return 'hello world'
# print(hello_world())
#
# """func 2"""
# def hello_name():
#     world = 'world'
#     return f'hello {world}'
# print(hello_name())
#
# """func 3"""
# def sum1(a,b):
#     return a + b
# print(sum1(5,5))
#
# """func 4"""
# def sum2(a,b):
#     if a > b:
#         return a
# print(sum2(5,4))
#
# """func 5"""
# def func5(n):
#     if n % 2 == 0:
#         return n
# print(func5(6))
#
# """func 6"""
# def func6(n):
#     return n**2
# print(func6(6))
#
# """func 7"""
# def func7(a,b,c):
#     return max(a,b,c)
# print(func7(7,5,9))
#
# """func 8"""
# def func8(*args):
#     return sum(args) / 3
# print(func8(7,5,9))
#
# """func 9"""
# def func9(c):
#     return c * 9 / 5 + 32
# print(func9(25))
#
# """func 10"""
# def func10(a):
#     return True if a % 3 ==0 else False
# print(func10(9))
#
# """func 11"""
# def func11(a):
#     return factorial(a)
# print(func11(3))

# """func 12"""
# def func12(a):
#     return len(a)
# print(func12('dastanbek'))

# """func 13"""
# def func13(a):
#     return str(a)
# print(func13(121354))

# """func 14"""
# def func14(a):
#     return True if a == a[::-1] else False
# print(func14('dastan'))

# """func 15"""
# def func15(a):
#     return True if a.count('a') else False
# print(func15('dastan'))

# """func16"""
# def func16(a, b):
#     return sum(1 for i in a if i in b)
# print(func16('dastan', 'aeiou'))

"""func17"""
from itertools import count

# def func17(a):
#     return [i ** 2 for i in range(1, a + 1)]
# print(func17(5))

# """func18"""
# def func18(a):
#     return True if a > 0 else False
# print(func18(3))

"""func19"""
# def func19(a):
#     return a ** a
# print(func19(5))

""""func20"""
# def func20(a):
#     if a < 2:
#         return False
#     for i in range(2, a):
#         if a % i == 0:
#             return False
#     return True
# print(func20(7))

"""func21"""

"""func22"""

"""func23"""
# def func23(a):
#     return len(a)
# print(func23('dastanbek'))


"""func24"""
# def func24(yyyy, mm, dd):
#     return f'{dd}:{mm}:{yyyy}'
# print(func24(yyyy='2003', mm='08', dd='04'))


"""func25"""
# def func25(numbers):
#     return sum(numbers)
# print(func25([1,2,3,4,5,6]))

"""func26"""
# def func26(numbers):
#     return [i for i in numbers if i % 2 == 0]
# print(func26([1,2,3,4,5,6,7,8,9]))

"""func27"""
# def func28(numbers):
#     return set(numbers)
# print(func28([1,2,3,4,3,6,1,8,2]))

"""func28"""
# import random
# def func28(num):
#     return [random.randint(1,5) for i in range(num)]
# print(func28(3))

"""func29"""
# def func29(n):
#     return sum(int(i) for i in str(n))
# print(func29(123))

"""func30"""
# def func30(year):
#     return True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False
# print(func30(2024))

"""func31"""
# def func31(num):
#     count = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count.append(i)
#     return count
# print(func31(10))

"""func32"""
# def func32(email):
#     parts = email.split("@")
#     return True if len(parts) == 2 and parts[0] != '' and '.' in parts[1] else False
# print(func32('dastan@gmail.com'))

"""func33"""
# def func33(name, symbol):
#     return name.replace(' ', symbol)
# print(func33('dastan arina arika', '+'))

"""func34"""
# def func34(a, b):
#     return a + b
# print(func34([1,2,3],[4,5,6]))

"""func35"""
# def func35(a,b):
#     count = []
#     for i in a:
#         if i in b:
#             count.append(i)
#     return count
# print(func35([1,2,3,4], [3,4,5]))

"""func36"""
# def func36(a,b):
#     count = []
#     for i in a:
#         if i not in b:
#             count.append(i)
#     return count
# print(func36([1,2,3,4], [3,4,5]))

"""func37"""
# def func37(name):
#     return ' '.join(name)
# print(func37(['dastan', 'arina', 'darika']))

"""func38"""
# def func38(name):
#     return [i for i in name if i != '']
# print(func38(['dastan', '', 'arina', '', 'darika']))

"""func39"""
# def func39(number):
#     a = 0
#     b = 1
#     count = []
#     for i in range(2, number + 1):
#         a,b = b,a+b
#         count.append(b)
#     return count
# print(func39(8))

"""func40"""
# def func40(a,b):
#     return sorted(a) == sorted(b)
# print(func40('dastan', 'tadasn'))

"""func41"""
# def func41(n):
#     count = {}
#     for i in n:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#             print(count)
#     return count
# print(func41('dastan'))

# """func42"""
# def func42(name):
#     return name.capitalize()
# print(func42('dastan'))

"""func43"""
# def func43(name):
#     return name[0].isupper()
# print(func43('dastan'))


"""func44"""
# def func44(name):
#     return name[::-1]
# print(func44(['dastan', 'darika', 'arina']))

"""func45"""
# def func45(numbers):
#     return len(set(numbers))
# print(func45([1, 2, 2, 3, 3, 3, 4]))

"""func46"""
# def func46(numbers):
#     return sorted(numbers, reverse=True)
# print(func46([4,3,6,8,2,1]))


"""func47"""
# def func47(numbers):
#     return max(numbers)
# print(func47([2,3,1,6,4,7,8,4]))


"""func48"""
# def func48(numbers):
#     return min(numbers)
# print(func48([2,3,1,6,4,7,8,4]))


"""func49"""
# def func49(numbers):
#     return all(i > 0 for i in numbers)
# print(func49([2,3,5,6]))

"""func50"""
# def func50(numbers):
#     return numbers.isnumeric()
# print(func50('123456'))

"""func51"""
# def func51(numbers):
#     n = 0
#     m = 0
#     for i in numbers:
#         if i % 2 == 0:
#             n += 1
#         if i % 3 == 0:
#             m += 1
#     return n, m
# print(func51([1,2,3,4,5,6,7,8]))

"""func52"""
# def func52(a, b):
#     return [i for i in a if len(i) > len(b)]
# print(func52(['dastan', 'arina', 'darika'], 'dasta'))

"""func53"""
# def func53(a,b):
#     result = ''
#     for i in b:
#         if i in a:
#             result += '*'
#         else:
#             result += i
#     return result
# print(func53('aeiou', 'dastanbek'))


"""func54"""
# def func54(number):
#     return sum(i for i in range(1,number+1) if i % 3 == 0 or i % 5 == 0)
# print(func54(10))

"""func55"""
# def func55(a,b):
#     result = ''
#     for i in a:
#         if i in b:
#             result += ''
#         else:
#             result += i
#     return result
# print(func55("Hello, world! How are you?", '!?,.*'))

"""func56"""
# def func56(a,b):
#     return b in a
# print(func56([1,2,3,4,5, 4))

"""func57"""
# def func57(numbers):
#     return numbers == sorted(numbers)
# print(func57([2,3,1,4,5,2]))