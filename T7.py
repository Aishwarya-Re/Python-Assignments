
# T7.1
from lib2to3.pgen2.token import MINUS
import math
from sre_constants import MIN_UNTIL
li = list(map(int, input("Please enter comma separaerd numbers").split(',')))

def formula(D):
    C = 50
    H = 30
    return math.sqrt(
        (2*C*D)/H
    )

res_li = list(map(formula, li))


# T7.2
class Shape(object):

    def area(self):
        print(0)

class Square(Shape):
    
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(self.length * self.length)

s = Square(10)
s.area()

# T7.3
class Numbers(object):
    def __init__(self, li):
        self.list = li
    def find_triplets(self, total=0):
        res = []
        l = len(self.list)
        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    if (self.list[i] + self.list[j] + self.list[k]) == total:
                        res.append([self.list[i], self.list[j], self.list[k]])
        return res

a = Numbers([-25,-10,-7,-3,2,4,8,10])
print(a.find_triplets())

# T7.4

class Time(object):
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    @staticmethod
    def addTime(time1, time2 ):
        hours = time1.hours + time2.hours
        minutes = time1.minutes + time2.minutes
        hours += minutes//60
        minutes %= 60
        return Time(hours=hours, minutes=minutes)

    def displayTime(self):
        print("{hour} hour and {minutes} minutes".format(
            hour=self.hours, minutes=self.minutes))

    def displayMinute(self):
        print("{minutes} minutes".format(
            minutes= (self.hours * 60 + self.minutes)))

t1 = Time(hours=2, minutes=50)
t2 = Time(hours=1, minutes=20)

t = Time.addTime(t1, t2)
t.displayTime()
t.displayMinute()


# T7.5
class Person(object):
    def __init__(self, age=0):
        self.age = 0
        if age < 0:
            print("Age is not valid, setting age to 0")
        else:
            self.age = age
    def yearPasses(self, years=0):
        self.age += years
        return self.age
    def amIOld(self, age):
        if age < 0:
            print("Age is not valid, setting age to 0")
        elif 0 <= age < 13:
            print("You are young")
        elif 12 < age < 20:
            print("You are a teenager")
        else:
            print("You are old")

p = Person()
p.amIOld(-1)
p.amIOld(4)
p.amIOld(10)
p.amIOld(16)
p.amIOld(18)
p.amIOld(64)
p.amIOld(38)

p2 = Person(38)
print(p2.yearPasses(4))

