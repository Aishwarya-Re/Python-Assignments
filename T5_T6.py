
# T5.1
try:
    eval('print 3')
except SyntaxError as e:
    print('There is a syntax error in the code block.')

# T5.2 
from re import L, sub
import sys
from wsgiref import validate
file_name = sys.argv[1]
try:
    f = open(file_name, 'r')
except Exception as e:
    file_name = input("Enter correct file name: ")
    f = open(file_name, 'r')

# T5.3
num = int(input('Enter a number: '))
while True:
    if not 999 < num <= 9999:
        print('The length is too short/long !!! Please provide only four digits')
    else:
        print('Your number is perfect. Bye!')
        break
    num = int(input('Enter a new number: '))



# T5.4

import random
def dummy_validate(username, password):
    num = random.randint(1,100)
    return num %2 == 0

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    tries = 0
    while tries < 3:
        tries += 1
        if dummy_validate(username, password):
            print('Login Successful')
            break
        else:
            password = input("Incorrect pasword, try again: ")
    else:
        print("3 Wrong passowrds tried, account suspended.")

# T5.5
"""
Done
"""

# T5.6
def return_even_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        res_lines = []
        for line in lines:
            if len(line) % 2 ==0:
                res_lines.append(line)
        return res_lines
        
lines = return_even_lines('doc.txt')


# T6.1
s = 'abcdEfGHijkL'
print([i for i in s if 65 <= ord(i) <= 90])


# T6.2
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']

print(dict(zip(students, subjects)))


# T6.3
"""
Done
"""

# T6.4
s = "Consultadd Training"
def reverse(s):
    l = len(s) - 1
    while l >= 0:
        yield s[l]
        l -= 1
reverse_s = ''
for i in reverse(s):
    reverse_s += i

print(reverse_s)

# T6.5

def decorator_func(func):
    def additional_steps_func(*args, **kwargs):
        print("About to start function: {func_name}".format(func_name=func.__name__))
        func(*args, **kwargs)
        print("Finished running function: {func_name}".format(func_name=func.__name__))
    return additional_steps_func

@decorator_func
def add_nums(a, b):
    print(a+b)

add_nums(2,3)
