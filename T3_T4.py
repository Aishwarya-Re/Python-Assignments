

# T3.1
# integers
a = 20
# string
b = 'Word is Worship'
# complex
c = complex(2,1)
#
d = 3.2

# T3.2
li = [1, 2, 3, 4, 5]
sl1 = li[::-1]
sl2 = li[:3:-1]
sl3 = li[2:]
sl4 = li[:2]

# T3.3
li = [1, 2, 3, 4, 5]
def _sum(li):
    li_sum = 0
    for i in li:
        li_sum += i
    
def _mul(li):
    li_sum = 1
    for i in li:
        li_sum *= i
    
# sum
li_sum = _sum(li)
# or using internal method, 
li_sum = sum(li)

# multiply
li_mul = _mul(li)

# T3.4
li = [1, 2, 3, 4, 5]
_min_num = min(li)
_max_num = max(li)
# or alternatively we can write our own methods

def _min(li):
    if li:
        li_min = li[0]
        for i in li[1:]:
            if i < li_min:
                li_min = i
    else:
        raise ValueError("Empty list")
    return li_min

def _max(li):
    if li:
        li_max = li[0]
        for i in li[1:]:
            if i > li_max:
                li_max = i
    else:
        raise ValueError("Empty list")
    return li_max

li_min = _min(li)
li_max = _max(li)

# or we can also use reduce
from functools import reduce
from sys import flags
print(reduce(lambda a,b: a+b, li))
print(reduce(lambda a,b: a*b, li))

# T3.5
from http.cookiejar import LoadError
import random
no_of_elem = 100
li = []
for i in range(no_of_elem):
    li.append(random.randint(0, 1000))
    
res_li = [i for i in li if i  %2 != 0]

# T3.6
import random
no_of_elem = 30
li = []
for i in range(no_of_elem):
    li.append(random.randint(0, 1000))
res_li = [j*j for i, j in enumerate(li) if i <5 or i>24]

# T3.7
li1, li2 = [1,3,5,7,9,10], [2,4,6,8]

_ = li1.pop()
li1.extend(li2)

# T3.8
a={1:10,2:20}
b={3:30,4:40}
res = {}
res.update(a)
res.update(b)

# T3.9
n = int(input("Enter a number: "))
res = {i: i*i for i in range(1, n+1)}

# T3.10
nums = input("Enter comma separated number: ")
nums_li = [int(i) for i in  nums.split(',')]
num_tup = tuple(nums_li)



# T4.1
a = str(input("Enter a string: "))
a = a[::-1]

# T4.2
a = str(input("Enter a string: "))
upper, lower = 0, 0
for i in a:
    if 65 <= ord(i) <= 90:
        upper += 1
    elif 97 <= ord(i) <= 122:
        lower += 1
    else:
        continue
print("No. of Uppercase characters : {upper} No. of Lower case Characters : {lower}".format(upper=upper, lower=lower))

# T4.3
def unique(li):
    res = [] 
    for i in li:
        if i not in res:
            res.append(i)
    return li

nums = input("Enter comma separated number: ")
nums_li = [int(i) for i in  nums.split(',')]

print(unique(nums_li))

# T4.4
hyphen_str = input("Enter hyphen seprated words e.g. red-blue-orange: ")
hyphen_list = hyphen_str.split('-')
hyphen_list.sort()
print('-'.join(hyphen_list))

# T4.5
print("Program  will ask for 5 lines and print them in upper case. ")
for _ in range(5):
    a = input("Enter text line: ")
    print(a.upper())


# T4.6
def sum_integral(num1, num2):
    print(int(num1) + int(num2))

num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

sum_integral(num1, num2)

# T4.7
def bigger_str(str1, str2):
    if len(str1) == len(str2):
        print(str1)
        print(str2)
    elif len(str1)> len(str2):
        print(str1)
    else:
        print(str2)

# T4.8
def tuple_of_squares():
    li = []
    for i in range(1, 21):
        li.append(i*i)
    print(tuple(li))
    
tuple_of_squares()

# T4.9
def showNumbers(limit):
    for i in range(limit+1):
        if i % 2 == 0:
            label = 'EVEN'
        else:
            label = 'ODD'
        print(i, label)

limit = int(input("Enter limit number: "))
showNumbers(limit)

# T4.10
li = [i for i in range(1,21)]
filter_li = list(filter(lambda x: x%2==0, li))
print(filter_li)

# T4.11
li = [1,2,3,4,5,6,7,8,9,10]
res_li = list(map(lambda x: x*x, filter(lambda x: x%2==0, li)))

# T4.12
try:
    print(5/0)
except Exception as e:
    print(e)

# T4.13
from functools import reduce 
li = [1,2,3,4,5,6,7]
flatten_num =int(reduce(lambda a,b: str(a) + str(b), li))
print(flatten_num)

# T4.14
import random
def check(x):
    if x % 3 != 0 and x %7 ==0:
        return x

divisible_by_7_not_3 = check
for _ in range(30):
    num = random.randint(1, 1000)
    res_num = divisible_by_7_not_3(num)
    if res_num:
        print(res_num)

# T4.15
def square(x):
    return x*x
li = [1,2,3,4,5,6,7,8,9]
res_li = list(map(square, li))

# T4.16.i
"""
2
"""

# T4.16.ii
"""
after f
after f?
error
"""
# Since there is an exception with unknown function f, post finally, that error will be raised.