def showEmployee(name, salary = 9000):
    print("Имя сотрудника: ", name, "его зарплата: ", salary)

name = input("Введите имя сотрудника: ")
salary = input("Введите зарплату сотрудника: ")

try:
    salary = int(salary)
    showEmployee(name, salary)
except:
    showEmployee(name)

