from pulp import *

cities = { 'ALB', 'CIN', 'CHI', 'GAR', 'HOU', 'KAN', 'PIT', 'TEM', 'YOU' }

# Nachfrage der Lager (in Tonnen pro Monat)
demand = {
	'ALB': 3000,
	'CIN': 0,
	'CHI': 0,
	'GAR': 6000,
	'HOU': 7000,
	'KAN': 0,
	'PIT': 0,
	'TEM': 4000,
	'YOU': 0
}


# Produktionskapazitäten der Stahlwerke (in Tonnen pro Monat)
capacities = {
	'ALB': 0,
	'CIN': 0,
	'CHI': 0,
	'GAR': 0,
	'HOU': 0,
	'KAN': 0,
	'PIT': 15000,
	'TEM': 0,
	'YOU': 15000
}


# Mindestmenge, die entlang einer Kante verschickt werden muss (in Tonnen pro Monat)
minFlow = {}
for i in cities:
	for j in cities:
		minFlow[(i,j)]=0

minFlow[('CIN', 'ALB')]=1000
minFlow[('PIT', 'KAN')]=2000
minFlow[('YOU', 'KAN')]=1000


# Maximalmenge, die entlang einer Kante verschickt werden kann (in Tonnen pro Monat)
maxFlow = {}
for i in cities:
	for j in cities:
		maxFlow[(i,j)]=0
		
maxFlow[('CIN', 'ALB')]=5000
maxFlow[('CIN', 'HOU')]=6000
maxFlow[('CHI', 'GAR')]=4000
maxFlow[('CHI', 'TEM')]=2000
maxFlow[('KAN', 'HOU')]=4000
maxFlow[('KAN', 'TEM')]=4000
maxFlow[('PIT', 'CIN')]=2000
maxFlow[('PIT', 'CHI')]=4000
maxFlow[('PIT', 'GAR')]=2000
maxFlow[('PIT', 'KAN')]=3000
maxFlow[('YOU', 'ALB')]=1000
maxFlow[('YOU', 'CIN')]=3000
maxFlow[('YOU', 'CHI')]=5000
maxFlow[('YOU', 'KAN')]=5000


# Kosten für den Transport (in Dollar pro Tonne)
costs = {}
for i in cities:
	for j in cities:
		costs[(i,j)]=0
		
costs[('CIN', 'ALB')]=350
costs[('CIN', 'HOU')]=550
costs[('CHI', 'GAR')]=120
costs[('CHI', 'TEM')]=600
costs[('KAN', 'HOU')]=375
costs[('KAN', 'TEM')]=650
costs[('PIT', 'CIN')]=350
costs[('PIT', 'CHI')]=375
costs[('PIT', 'GAR')]=450
costs[('PIT', 'KAN')]=450
costs[('YOU', 'ALB')]=500
costs[('YOU', 'CIN')]=350
costs[('YOU', 'CHI')]=375
costs[('YOU', 'KAN')]=450

prob = LpProblem("dist", LpMinimize)
routes = LpVariable.dicts("route_", costs, 0)
#print(routes)
prob.setObjective(lpSum([routes[(i, j)] * costs[(i, j)] for i in cities for j in cities]))

for i in cities:
    prob += lpSum([ routes[(j,i)] for j in cities ]) >= demand[i]
    for j in cities:
        prob += routes[(i,j)] <= maxFlow[(i,j)]
        prob += routes[(i,j)] >= minFlow[(i,j)]

for factory in ['YOU','PIT']:
    prob += lpSum([routes[(factory,i)] for i in cities]) <= capacities[factory]

for store in ['CIN','KAN','CHI']:
    prob += (lpSum([routes[(i,store)] for i in cities]) - lpSum([routes[(store, i)] for i in cities ]) == 0)

prob.solve()

print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    for i in cities:
        for j in cities:
            if value(routes[(i,j)]) > 0:
                print(f"Route ({i}, {j})",value(routes[(i,j)]))          
    #[print(f"Route ({i}, {j})",value(routes[(i,j)])) for i in cities for j in cities]
    print(20*"-")
    print("max Cost:", value(prob.objective))
    print(20*"-")
    print(20*"#")
