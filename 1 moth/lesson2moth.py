users = [
    {"name": "Dastan", "age": 22, "score": 85},
    {"name": "Aibek", "age": 19, "score": 90},
    {"name": "Nursultan", "age": 25, "score": 70}
]

def is_everyone_allowed(user):
    return all(i['age'] > 18 and i['score'] > 75  for i in user)
print(is_everyone_allowed(users))

