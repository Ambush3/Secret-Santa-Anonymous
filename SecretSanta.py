import copy
import random
import smtplib

names = ['Gramma', 'Grandpa Jim', 'Grandma Pam', 'Brittany', 'Robert', 'Sierra', 'Mark', 'Katie',
         'Mamma', 'Sydney', 'Aaron', 'Josh']
emails = ['12334@gmail.com', '234556@gmail.com', '4444@gmail.com']


def secret_santa(names):
    list = names
    choose = copy.copy(list)
    result = []
    for i in list:
        names = copy.copy(list)
        names.pop(names.index(i))
        chosen = random.choice(list(set(choose)&set(names)))
        result.append((i, chosen))
        choose.pop(choose.index(chosen))
    return result

