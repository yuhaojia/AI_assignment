from planning_agent import *
import random


letterOut = []
letters = 'ABCDE'

for i in range(5):
    line = []
    for i in range(8):
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
#iter = [0,0,0,0,0]
#x = ord(Widget[0][0])
#print(x)

#Widget = ["AEDCA", "AEDCA", "BABCE", "BABCE", "BECBD"]
#Widgets = [['A', 'E', 'D', 'C', 'A', '*'],['B', 'E', 'A', 'C', 'D', '*'],['B', 'A', 'B', 'C', 'E', '*'],['D', 'A', 'D', 'B', 'D', '*'],['B', 'E', 'C', 'B', 'D', '*']]
#Widgets = [['E', 'D', 'E', 'B', 'E', 'B', 'C', '*'], ['A', 'B', 'D', 'E', 'B', 'E', 'C', '*'], ['E', 'C', 'A', 'C', 'A', 'D', 'C', '*'], ['E', 'C', 'B', 'A', 'C', 'D', 'B', '*'], ['D', 'A', 'C', 'A', 'E', 'A', 'D', '*']]

Widgets = deepcopy(letterOut)

#Widget[0].pop(1)

def allStep(Widgets):
    elementsAlways = ['A', 'B', 'C', 'D', 'E']
    listHAAHA = []
    if listHAAHA:
        listHAAHA.pop()
    for wigfget in Widgets:
        listHAAHA.append(wigfget[0])
    for element in elementsAlways:
        if element in listHAAHA:
            path = step(element, Widgets)
            print(path)
            path.pop()


#path = miles('A', Widgets)
#print(path)
#path.pop()

def allmiles(Widgets):
    elementsAlways = ['A', 'B', 'C', 'D', 'E']
    listHAAHA = []
    if listHAAHA:
        listHAAHA.pop()
    for wigfget in Widgets:
        listHAAHA.append(wigfget[0])
    for element in elementsAlways:
        if element in listHAAHA:
            path = miles(element, Widgets)
            print(path)
            path.pop()

allStep(Widgets)
#allmiles(Widgets)