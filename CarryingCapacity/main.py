from nature import *
import matplotlib.pyplot as plt
from math import *

to_append = 0
FOOD = 10**6
cells = list()
cells.append(Cell(500,1000,False,0))
average_ages = list()
days = list()
populations = list()
lifespans = list()

for i in range(500):
    food = FOOD
    lifespan = (26+6*sin(i)+i**(1/6))
    lifespans.append(lifespan)
    for cell in cells:
        if cell.age > lifespan:
            cells.remove(cell)
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
        cells.append(Cell(500,1000,False,0))
    age_sum = 0
    for cell in cells:
        age_sum += cell.age
    days.append(i)
    average_ages.append(age_sum/len(cells))
    populations.append(len(cells))

plt.plot(days,populations)
plt.title('Days vs Cell Population')
plt.xlabel('Day Number')
plt.ylabel('Population')
plt.savefig('graph1.png')
plt.clf()

plt.plot(days,average_ages)
plt.title('Days vs Cells\' Average Age')
plt.xlabel('Day Number')
plt.ylabel('Average Age')
plt.savefig('graph2.png')
plt.clf()

plt.plot(days,lifespans)
plt.title('Days vs Lifespan')
plt.xlabel('Day Number')
plt.ylabel('Lifespan')
plt.savefig('graph3.png')