from pulp import * 
nutrition = { 'calories', 'protein', 'fat', 'sodium' }

maxNutrition = { 
    'calories': 2200,   
    'protein':  200, 
    'fat': 65, 
    'sodium':  1779 
}

minNutrition = { 
    'calories': 1800, 
    'protein':  75, 
    'fat': 0, 
    'sodium':  0 
}

nutritionValues = {
    ('hamburger', 'calories'): 410,
    ('hamburger', 'protein'):  24,
    ('hamburger', 'fat'):      26,
    ('hamburger', 'sodium'):   730,
    ('chicken',   'calories'): 420,
    ('chicken',   'protein'):  32,
    ('chicken',   'fat'):      10,
    ('chicken',   'sodium'):   1190,
    ('hot dog',   'calories'): 560,
    ('hot dog',   'protein'):  20,
    ('hot dog',   'fat'):      32,
    ('hot dog',   'sodium'):   1800,
    ('fries',     'calories'): 380,
    ('fries',     'protein'):  4,
    ('fries',     'fat'):      19,
    ('fries',     'sodium'):   270,
    ('macaroni',  'calories'): 320,
    ('macaroni',  'protein'):  12,
    ('macaroni',  'fat'):      10,
    ('macaroni',  'sodium'):   930,
    ('pizza',     'calories'): 320,
    ('pizza',     'protein'):  15,
    ('pizza',     'fat'):      12,
    ('pizza',     'sodium'):   820,
    ('salad',     'calories'): 320,
    ('salad',     'protein'):  31,
    ('salad',     'fat'):      12,
    ('salad',     'sodium'):   1230,
    ('milk',      'calories'): 100,
    ('milk',      'protein'):  8,
    ('milk',      'fat'):      2.5,
    ('milk',      'sodium'):   125,
    ('ice cream', 'calories'): 330,
    ('ice cream', 'protein'):  8,
    ('ice cream', 'fat'):      10,
    ('ice cream', 'sodium'):   180 
}
cost = {
    'hamburger': 2.49,
    'chicken':   2.89,
    'hot dog':   1.50,
    'fries':     1.89,
    'macaroni':  2.09,
    'pizza':     1.99,
    'salad':     2.49,
    'milk':      0.89,
    'ice cream': 1.59 
}
foods = [ 'hamburger', 'chicken', 'hot dog', 'fries', 'macaroni', 'salad', 'milk', 'ice cream' ]

prob = LpProblem("diet", LpMinimize)
lpVars = LpVariable.dicts('', foods, 0)

# min Sum( c^f * x)
# s.t.
#   Sum( a^f,n * x <= maxN )
#   Sum( a^f,n * x >= minN)

prob.setObjective(lpSum([cost[food] * lpVars[food] for food in foods]))

for nut in nutrition: 
    tmp = lpSum([nutritionValues[(food, nut)] * lpVars[food] for food in foods])
    prob += tmp <= maxNutrition[nut]
    prob += tmp >= minNutrition[nut]

prob.solve()

print("Status: ", LpStatus[prob.status], "\n")
if(prob.status):
    print(20*"#")
    for food in foods:
        print(food, " : ", value(lpVars[food]))
    print(20*"-")
    print("Objective value: ", pulp.value(prob.objective))
    print(20*"#")








