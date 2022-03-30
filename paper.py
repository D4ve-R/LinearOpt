from pulp import *
import numpy as np

# Verkaufspreis pro Papiersorte
price=[128, 50, 38, 69, 54, 112, 38, 40, 62, 49]

# Maximale Absatzmenge pro Papiersorte
maxTons=[600, 1250, 890, 440, 810, 500, 1150, 789, 500, 700]

# Maximale Verfügbarkeit pro Maschine
machineCapacity=[130, 200, 375, 100, 208, 305]

# Kosten für die Produktion von Papiersorte i auf Maschine j (pro Stunde)
cost=[
	[14, 18, 13, 20, 13, 11],
	[31, 20, 10, 21, 22, 15],
	[11, 8, 41, 50, 21, 13],
	[11, 8, 41, 19, 21, 11],
	[21, 17, 24, 18, 31, 20],
	[14, 18, 13, 20, 13, 11],
	[31, 20, 10, 21, 22, 15],
	[11, 8, 41, 50, 21, 13],
	[11, 8, 41, 19, 21, 11],
	[21, 17, 24, 18, 31, 20]
]

# Produzierte Tonnen von Papiersorte i bei Produktion auf Maschine j (pro Stunde) 
productivity=[
	[3, 4, 2, 5, 2, 1],
	[4, 3, 1, 5, 4, 3],
	[2, 7, 3, 5, 1, 3],
	[1, 2, 4, 7, 6, 4],
	[2, 5, 8, 3, 5, 2],
	[3, 4, 2, 5, 2, 1],
	[4, 3, 1, 5, 4, 3],
	[2, 7, 3, 5, 1, 3],
	[1, 2, 4, 7, 6, 4],
	[2, 5, 8, 3, 5, 2]
]

mCount = len(machineCapacity)
machines = range(mCount)
papers = range(len(price))
npProd = np.array(productivity)
npCost = np.array(cost)
npProfit = np.empty((len(price), mCount))

for i in papers:
    npProfit[i] = npProd[i] * price[i]
c = npProfit - npCost

prob = LpProblem('Paper', LpMaximize)
xDict = LpVariable.dicts('x',range(mCount * len(price)), 0)

# x is a vector converted from matrix of dim 10x6 = 1x60
# x[i][j] => x[j + (i * len(x[i]))]
x = list(xDict.values())
prob.setObjective(lpSum([[c[row][val] * x[row * mCount + val] for val in machines] for row in papers]))

tmp = None
for i in papers:
    for j in machines:
        tmp += productivity[i][j] * x[j + (i * mCount)]
    prob += tmp <= maxTons[i]
    tmp = None

for i in machines:
    for j in papers:
        tmp += x[i + (j * mCount)]
    prob += tmp <= machineCapacity[i]
    tmp = None

#print(prob)
prob.solve()
print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    print("max Profit: ", value(prob.objective))
    print(20*"-")
    print(6*' ', end='')
    [print(f"  m_{i}", end='  ') for i in machines]
    print()
    for i in papers:
        print(f"p_{i}:[", end='')
        for j in machines:
            print(f"{value(x[j+i*mCount]):6.2f}", end=' ')
        print(']')

    print(20*"#")

