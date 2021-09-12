#1
def calculation(a, b):
    sum = a + b
    subt = a - b

    return (sum, subt)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print(calculation(num1, num2))
print("Число {} результат сложения, а число {} результат вычитания".format(calculation(num1, num2)[0], calculation(num1, num2)[1]))

#2





#3
import random

def func(*args):
    i = 0
    for a in args:
        print("Аргумент: {}, индекс аргумента {}".format(a, i))
        i += 1

func(5, 3, "arg1", "arg2", 3.4)


#4

