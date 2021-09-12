import random

def lol(*args):
    i = 0
    for a in args:
        print("Аргумент: {}, индекс аргумента {}".format(a, i))
        i += 1

lol(5, 3, "arg1", "arg2", 3.4)

