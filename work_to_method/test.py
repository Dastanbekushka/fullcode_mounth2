import random

def numbers(num):
    result = []
    for i in range(num):
        result.append(random.randint(1,10))
    return result
