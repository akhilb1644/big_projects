from nature import *
import matplotlib.pyplot as plt
from math import *
from random import randint

to_append = 0
FOOD = 10**6
cells = list()
cells.append(Cell(500,100000,False,0))
average_ages = list()
days = list()
populations = list()
lifespans = list()
pandemics = list()

for i in range(5000):
    food = FOOD
    lifespan = (18+6*sin(i)+i**(1/2))
    lifespans.append(lifespan)
    for cell in cells:
        if cell.age > lifespan:
            cells.remove(cell)
    for cell in cells:
        if (i-10) % 499 == 0:
            coeff = (lifespan / 2) / 10
            chance = int(abs(cell.age-(lifespan/2)) * coeff) + 90
            num = randint(0,100)
            if num < chance:
                cells.remove(cell)
            pandemics.append(i)
            pandemics = list(set(pandemics))
    for cell in cells:
        if food >= cell.req_energy:
            food -= cell.req_energy
            cell.eat_state = True
        else:
            cells.remove(cell)
    for cell in cells:
        if food >= cell.rep_energy:
            food -= cell.rep_energy
            to_append += 1
        cell.age += 1
    for _ in range(to_append):
        cells.append(Cell(500,100000,False,0))
    age_sum = 0
    for cell in cells:
        age_sum += cell.age
    days.append(i)
    average_ages.append(age_sum/len(cells))
    populations.append(len(cells))

plt.plot(days,populations)
for pandemic in pandemics:
    plt.axvline(x=pandemic,color='r',linestyle='dotted')
plt.title('Days vs Cell Population')
plt.xlabel('Day Number(Pandemics in red)')
plt.ylabel('Population')
plt.savefig('graph1.png')
plt.clf()

plt.plot(days,average_ages)
for pandemic in pandemics:
    plt.axvline(x=pandemic,color='r',linestyle='dotted')
plt.title('Days vs Cells\' Average Age')
plt.xlabel('Day Number(Pandemics in Red)')
plt.ylabel('Average Age')
plt.savefig('graph2.png')
plt.clf()

plt.plot(days,lifespans)
for pandemic in pandemics:
    plt.axvline(x=pandemic,color='r',linestyle='dotted')
plt.title('Days vs Lifespan')
plt.xlabel('Day Number(Pandemics in red)')
plt.ylabel('Lifespan')
plt.savefig('graph3.png')