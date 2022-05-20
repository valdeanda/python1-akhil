Limit = 0
try:
    Limit = int(input("How many fibonacci numbers do you want? "))
except ValueError:
    print("Enter an integer next time")
    exit()
FN = [0, 1]
if Limit > 2:
    for i in range(2, Limit):
        FN.append(FN[len(FN) - 1] + FN[len(FN) - 2])
    print(FN)
elif Limit == 2:
    print(FN)
elif Limit == 1:
    print(FN[0])
else:
    print("That's not a good number, please try again")
