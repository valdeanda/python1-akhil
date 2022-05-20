import math
import random

w = True  # Boolean
x = 56  # Integer (int)
y = "Hola"  # String
z = 37.89  # Float

print("Hello World")
print(w)
print(x)
print(y)
print(z)

# Concatenation is joining two strings together
print("Variable z is: " + str(z))

# i = input("Give me an input: ")
print(float(x))

print("String Functions: ")
print(y.lower())
print(y.upper())
print(y.islower())
print(y.isupper())
print(len(y))
print(y.index("l"))
print(y[0:2])
print(y[1:])
print(y[:3])

print("\nNumber Functions: ")
print(str(abs(x)) + " " + str(abs(z)))
print(pow(x, 4))
print(min(x, z))
print(max(x, z))
print(round(z))
print(math.floor(z))
print(math.ceil(z))
print(math.sqrt(x))

print("\nTry and Except Blocks")
# try:
#     x = int(input("Give me a number: "))
# except:
#     print("You did not enter an integer value")

print("\nLists:")
List = ["Thing 1", 2, 3.0]
List2 = [4, False, 6]
List.extend(List2)
print(List)
List.append(5)
print(List)
List.insert(1, 6)
print(List)
List.remove(6)
print(List)
List.pop()
print(List)
print(List.index(False))
# List.sort()
# List.reverse()

print("\n2DLists: ")
TwoDList = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print(TwoDList[1])

print("\nTuples: ")
Tuple = ("Thing 1", 2)

print("\nDictionaries: ")
# No duplicates
Dictionary = {"Key 1": "Value 1",
              "Key 2": "Value 2"}
Dictionary["Key 3"] = "Value 3"
Dictionary["Key 1"] = "Another Value"
print(Dictionary.get("Key 1"))

print("\nIf Statements: ")
if 3 == 3.0 and 5 / 2 >= 3:
    print("If statement was a success")
elif pow(5, 2) == 25 or 7 / 3 != 2:
    print("Elif statement was a success")
else:
    print("None of the other statements were a success")

print("\nFor Loops: ")
for element in List:
    if element == 6:
        break
    elif element == "Thing 1":
        continue
    print(type(element))
for i in range(len(List)):
    print("Element " + str(i) + " of the list is " + str(List[i]))
for j in range(1, 47, 4):
    print(j)

print("\nWhile Loops: ")
n = 1
while n <= 10:
    print(n)
    n += 1

print("After While Loop: " + str(n))

print("\nFunctions: ")


def HelloWorld():
    print("Hello World")


HelloWorld()


def subtract(one, two):
    return one - two


print(subtract(25, 12))

print("\nClasses:")


class NewClass:
    # Instance Variables
    Var1 = 0
    Var2 = 0

    # Constructor
    def __init__(self, Var1, Var2):
        self.Var1 = Var1
        self.Var2 = Var2

    # A regular function within the class
    def Function(self):
        return self.Var1 - self.Var2


c = NewClass(25, 12)
print(str(c.Var1) + " " + str(c.Var2))
print(c.Function())


class Person:
    name = ""
    age = 0
    HasACar = False
    Spouse = "None"

    def __init__(self, name, age, HasACar):
        self.name = name
        self.age = age
        self.HasACar = HasACar

    def HasASpouse(self, spouse):
        self.Spouse = spouse

    def NameChange(self, newName):
        self.name = newName

    def Birthday(self):
        print("Happy Birthday " + self.name + "!")
        self.age += 1

    def Married(self, newSpouse):
        print(self.name + " got married to " + newSpouse)
        self.Spouse = newSpouse


Bob = Person("Bob", 46, False)
print(Bob.name + " " + str(Bob.age) + " " + str(Bob.HasACar))
Bob.Birthday()
print(Bob.age)

Larry = Person("Larry", 23, True)
print(Larry.name + " " + str(Larry.age) + " " + str(Larry.HasACar))

print("\nInherited Classes:")


class Worker(Person):
    money = 0

    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def Work(self, hoursWorked):
        self.money += hoursWorked * 15

    def Birthday(self, moneyGiven):
        print("Happy Birthday " + self.name + "!")
        self.age += 1
        self.money += moneyGiven


Sarrah = Worker("Sarrah", 12, 0)
print(Sarrah.age)
print(Sarrah.name)
print(Sarrah.HasACar)
Sarrah.Work(15)
print(Sarrah.money)
Sarrah.NameChange("Ren")
print(Sarrah.name)
Sarrah.Birthday(100)
print(Sarrah.money)

print("\nVariable Scope:")


def doesNothing():
    global q
    q = 34
    print(q)


q = 54
doesNothing()
print(q)

print("\nFile-Reading:")
# Read Mode:
File = open("Test.txt", "r")
if File.readable():
    # print(File.read())
    # print(File.readline())
    # print(File.read())
    # print(File.readlines())
    print(File.readlines()[0])

# Append Mode:
File2 = open("Test2.txt", "a")
File2.write("Hello World\n")

# Write Mode:
File3 = open("Test3.txt", "w")
File3.write("Hola World")

# Read+ Mode: r+

# Closing Files:
File.close()
File2.close()
File3.close()

print("\nRandom Module:")

Die = random.randint(1, 6)
print(Die)

rand = random.random()  # random.uniform(a, b)
print(rand)

random.shuffle(List)
print(List)
print(random.choice(List))
