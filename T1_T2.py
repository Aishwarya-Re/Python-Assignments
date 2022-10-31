# T1.1

a, b, c = 1, 2.01, 'string'
print("Sol. T1.1:", a, b, c)

# T1.2
a, b = complex(1,2), 5
a, b = b, a
print("Sol. T1.1:", a, b)

# T1.3
# swap with third variable
a, b = 1, 2
c = a
a = b
b = c

# swap without third variable
a, b = 1, 2
a, b = b, a


# T1.4
a = input("hello")
# python 2 print
print a
# python 3 print
print(a)


# T1.5
num1 = int(input("Enter number a number between 1-10: "))
num2 = int(input("Enter number a number between 1-10: "))
z = num1 + num2
result = z + 30
print(result)

# T1.6
inp = input("Enter anything ")
print(type(inp))

# T1.7
UpperCamelCase = "Work is Worship"
lowerCamelCase = "Work is Worship"
snake_case = "Work is Worship"
UPPER_CASE = "Work is Worship"

# T1.8
a = 10
a = 'Hello World!!!'
# Yes the value will be changed for variable 'a'. Internally, variable 'a' is pointing to value 10 stored in the memory.
# The very next statement simply updates the pointer to point to value 'Hello World!!!' stored in the memory


# T2.1
def print_msg(a):
    if a%3 == 0 and a%5==0:
        print("Consultadd - Python Training")
    elif a%3 == 0:
        print("Consultadd")
    elif a%5 == 0:
        print("Python Training")

a = int(input("Enter any number: "))
print_msg(a)

# T2.2

def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return a/b
def avg(a, b, c, d): return (a+b+c+d)/4

actions = {
    1: add,
    2: sub,
    3: div,
    4: mul,
    5: avg
}

option = int(input(
    """
    Please enter appropriate option to perform below action:
    1. Addition
    2. Substraction
    3. Division
    4. Multiplication
    5. Average
    """
))
if not 1 <= option <= 5:
    print("Invalid option entered!!!")
else:
    res = 0
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    if option == 5:
        first = int(input("Enter num3: "))
        second = int(input("Enter num4: "))
        res = actions[option](num1, num2, first, second)
    else:
        res = actions[option](num1, num2)
    
    if res < 0:
        print("NEGATIVE")
    else:
        print(res)



# T2.3
a, b, c = 10, 20, 30
avg = (a+b+c)/3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, c")
elif avg > a and avg > b:
    print("avg is higher than a, b")
elif avg > a and avg > c:
    print("avg is higher than a, c")
elif avg > b and avg > c:
    print("avg is higher than b, c")
elif avg > a:
    print("avg is higher than a")
elif avg > b:
    print("avg is higher than b")
elif avg > c:
    print("avg is higher than c")
else:
    print("___(-.-)___")


# T2.4

while(True):
    num = int(input())
    if num < 0:
        print("It's Over")
        break
    print("Good Going")


# T2.5

# Get the first number divisible by 7, this is done to shorten our list with for loop
start = 2000
while(True):
    if start % 7 == 0:
        break
    start += 1

# Since we have starting number then we can hop seven numbers at once rather than 1 number at a time
for i in range(start, 3200, 7):
    if i % 5 != 0 and i%7 ==0:
        print (i)

# T2.6.1
"""
 Error
 explanation: Intergers are not iterabl, thus cannot used in loops to loop over
"""

# T2.6.2
"""
0
error
1
error
2
"""

# T2.6.3
"""
0
1
2
3
4
"""

# T2.7 
for i in range(7):
    if i % 3 == 0 and i//3:
        continue
    print(i, end=" ")

# T2.8
s = input("Enter any alphanumberic string: ")
letters, digits = 0, 0 
for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        letters += 1
    elif 48 <= ord(i) <= 57:
        digits += 1
print('Letters:', letters, " Digits: ", digits)


# T2.9.1
from itertools import count
import random
lucky_number = random.randint(0, 99)

num = int(input("Guess the lucky number: "))
while num != lucky_number:
    num = int(input("Wrong Guess, try a new number: "))
else:
    print("Wow! Lucky number found.")


# T2.9.2
import random
lucky_number = random.randint(0, 99)
number = int(input("Guess the lucky number: "))
while number != lucky_number:
    answer = input("Wrong Guess, wanna continue? (yes/no): ")
    if answer == 'no':
        break
    number = int(input("Try a new number:"))
else:
    print("Wow! Lucky number found.")

# T2.10
import random
lucky_number = random.randint(0, 99)
counter = 1
while counter <= 5:
    number = int(input("Guess the lucky number: "))
    if number == lucky_number:
        print('Good guess!')
    else:
        print('Try again!')
    counter += 1
else:
    print('Game Over!')

# T2.11
import random
lucky_number = random.randint(0, 99)
counter = 1
while counter <= 5:
    number = int(input("Guess the lucky number: "))
    if number == lucky_number:
        print('Good guess!')
        break
    else:
        print('Try again!')
    counter += 1
else:
    print('Sorry but that was not very successful')
