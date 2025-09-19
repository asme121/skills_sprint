# def hello(name):
#     return 'Hello ' + name
#
# name1 = hello('Ausura')
# print(name1)
#
# def func(num):
#     return num * num
#
# print(func(5))
#
# def func2(new, old):
#     return ((new-old)/old*100)
# print(func2(12,5))

# def first_func(string):
#     return f'I love {string}'
#
# print(first_func('United'))
#
# def tripler(num):
#     return num * 3
# print(tripler(5))
# print(tripler(10))
# print(tripler(30))
#
# def greet(name):
#     return f'Hello {name}'
# print(greet('Ausura'))
#
# def is_even(num):
#     return num % 2 == 0
# print(is_even(9))
#
# def repeat_word(word, n):
#     return word * n
# print(repeat_word('yes', 3))
#
# def def_par(base, exp = 2):
#     return base ** exp
# print(def_par(5,5))

# def fact(n):
#     return

#Lambda functions
import math

def sum(a,b):
    return a + b

sum_lambda = lambda a, b: a + b
print(sum_lambda(1, 2))

subtract = lambda a,b,c: a+b-c

cube = lambda x: x**3

perimeter = lambda r: 2 * r * math.pi

area = lambda r: math.pi * r ** 2
print(area(100))

triangle = lambda a, b, c : math.sqrt((a + b + c)/2 * ((a + b + c)/2 - a) * ((a + b + c)/2 - b) * ((a + b + c)/2 - c))
print(triangle(100, 100, 100))

def multiplier(n):
    return lambda x: x * n

doubler = multiplier(2)
tripler = multiplier(3)

#lambda functions with map and filter
#map - apply a function to each element
#filter - apply a condition to each element to filter them
# numbers = [2,3,4]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)
#
# #filter - apply a condition to each element to filter them
# number1 = range(1,10)
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# odds = list(filter(lambda x: x % 2 != 0, numbers))
#
#
#
# # sort
# numbers = [5, 1, 8, 3]
# numbers.sort(reverse=True)
# print(numbers)   # [8, 5, 3, 1]

import csv
rows = []

header = ['name', 'age']
data = [['Alex', 25], ['Bob', 35], ['Cathy', 55]]

with open('employees.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

#csv.DictReader()
with open('employees.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'])
        print(row)

#csv.DictWriter()
header = ['Name', 'Age']
data = [['Alex', 25], ['Bob', 35], ['Carol', 45], ['David', 55]]

with open('student_info.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)

    writer.writeheader()
    for student in data:
        writer.writerow({'Name': student[0], 'Age': student[1]})
