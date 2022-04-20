from pulp import *

products = ['P1', 'P2', 'P3']
subs = ['A', 'B', 'C', 'D', 'E', 'Kal', 'Cal', 'Mag']

prices = {
        'P1': 2.0,
        'P2': 3.0,
        'P3': 2.5,
        }

demand = {
        'A'  : 2.5,
        'B'  : 3.0,
        'C'  : 500.0,
        'D'  : 600.0,
        'E'  : 0.1,
        'Kal': 20.0,
        'Cal': 3000.0,
        'Mag': 3000.0
        }

contains = {}

for i in products:
    for j in subs:
        contains[(i,j)] = 0

contains[('P1','C')] = 400
contains[('P1','E')] = 1
contains[('P1','Kal')] = 30
contains[('P1','Cal')] = 3000
contains[('P1','Mag')] = 2500

contains[('P2','A')] = 2
contains[('P2','B')] = 2
contains[('P2','C')] = 400
contains[('P2','D')] = 300
contains[('P2','E')] = 0.2
contains[('P2','Kal')] = 20
contains[('P2','Cal')] = 500

contains[('P3','A')] = 3
contains[('P3','B')] = 5
contains[('P3','C')]= 750
contains[('P3','D')]= 750
contains[('P3','E')]= 0.2

prob = LpProblem('Lp', LpMinimize)
x = LpVariable.dicts('product_', products, 0)
#print(x)
prob.setObjective(lpSum([prices[p] * x[p] for p in products]))

for s in subs:
    prob += lpSum([contains[p,s] * x[p] for p in products]) >= demand[s]

prob.solve()

print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    [print(f"{p}", value(x[p])) for p in products]
    print(20*"-")
    print("obj val: ", value(prob.objective))
    print(20*"#")

print(30*'$')
# dual lp
# add padding
slack = ['S1','S2','S3','S4','S5','S6','S7','S8']
i = 0
for p in slack:
    prices[p] = 0
    for s in subs:
        if subs[i] == s:
            contains[(p,s)] = -1
        else:
            contains[(p,s)] = 0
    i += 1

products += slack

dlp = LpProblem('Dlp', LpMinimize)
y = LpVariable.dicts('y_', subs, 0)

dlp.setObjective(lpSum([demand[s] * y[s] for s in subs]))

for p in products:
    dlp += lpSum([contains[(p,s)] * y[s] for s in subs]) == -1*prices[p]

dlp.solve()
print("Status: ", LpStatus[dlp.status], "\n")
if(dlp.status):
    print(20*"#")
    [print(f"{s}", value(y[s])) for s in subs]
    print(20*"-")
    print("obj val: ", value(dlp.objective))
    print(20*"#")

