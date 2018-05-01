
import random


letterOut = []
letters = 'ABCDE'

for i in range(5):
    line = []
    for i in range(7):
        if i ==0:
            x = random.choice(letters)
            line.append(x)
        else:
            x = random.choice(letters)
            while x==line[-1]:
                x = random.choice(letters)
            line.append(x)
    line.append('*')
    letterOut.append(line)
print(letterOut)