import random

def createRandomList(length):
    l = list()
    for _ in range(length):
        l.append(random.randint(0, 20))
    return l

def sumList(l):
    sum = 0
    for i in l:
        sum += i
    return sum

newList = createRandomList(5)

print("List:", newList)
print("List sum:", sumList(newList))

