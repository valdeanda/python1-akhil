fnumber = int(input("What is the first number? "))
operator = input("Operator: ")
snumber = int(input("What is the second number? "))
if operator == "+":
    print(fnumber + snumber)
elif operator == "-":
    print(fnumber - snumber)
elif operator == "*":
    print(fnumber * snumber)
else:
    print(fnumber / snumber)
