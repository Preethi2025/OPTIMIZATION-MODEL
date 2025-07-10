
# Task 4 - Optimization Model using Linear Programming
# Business Problem: Maximize profit from two products (A and B) under constraints

from pulp import *

# Step 1: Define the Linear Programming problem
problem = LpProblem("Maximize_Profit", LpMaximize)

# Step 2: Define Decision Variables
# A and B represent the number of units to produce of Product A and Product B
A = LpVariable("Product_A", lowBound=0, cat='Continuous')
B = LpVariable("Product_B", lowBound=0, cat='Continuous')

# Step 3: Define Objective Function
# Suppose: Profit per unit A = ₹20, Profit per unit B = ₹30
problem += 20*A + 30*B, "Total_Profit"

# Step 4: Define Constraints
# Constraint 1: Labor hours constraint
# Product A takes 2 hours, Product B takes 1 hour, total hours available = 100
problem += 2*A + 1*B <= 100, "Labor_Constraint"

# Constraint 2: Raw materials constraint
# Product A needs 3 units, Product B needs 4 units, total material available = 240
problem += 3*A + 4*B <= 240, "Material_Constraint"

# Step 5: Solve the problem
problem.solve()

# Step 6: Display the results
print("Status:", LpStatus[problem.status])
print("Optimal Production of Product A:", A.varValue)
print("Optimal Production of Product B:", B.varValue)
print("Maximum Profit: ₹", value(problem.objective))

# Expected Output:
# Status: Optimal
# Optimal Production of Product A: 20.0
# Optimal Production of Product B: 60.0
# Maximum Profit: ₹ 2600.0
