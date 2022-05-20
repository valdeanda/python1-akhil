import random

passwordChars = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# Adding Letters
for i in range(random.randint(6, 10)):
    if random.random() < 0.5:
        passwordChars.append(random.choice(alphabet).upper())
    else:
        passwordChars.append(random.choice(alphabet))

# Adding numbers
for i in range(random.randint(2, 4)):
    passwordChars.append(random.randint(0, 9))

# Adding Characters
for i in range(random.randint(1, 2)):
    passwordChars.append(random.choice(symbols))

# Shuffling and putting them together
random.shuffle(passwordChars)
finalPassword = ""
for char in passwordChars:
    finalPassword += str(char)
print(finalPassword)
