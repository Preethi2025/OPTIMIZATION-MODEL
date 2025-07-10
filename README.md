# OPTIMIZATION-MODEL

"Company":CODTECH IT SOLUTONS

"NAME":KANUMALA PREETHI

"INTERN ID":CTO4DG851

"DOMAIN":DATA-PIPELINE-DEVELOPMENT

"DURATION":4WEEKS

"MENTOR": NEELA SANTHOSH

DESCRIPITON OF THE TASK:Objective:
The primary goal of this task is to solve a real-world business problem using mathematical optimization techniques. Specifically, we aim to use Linear Programming (LP) to maximize profit under given constraints using Python and the PuLP library.
🧠 Problem Overview:
In many business scenarios, companies must make decisions that optimize resources such as time, labor, materials, or costs. Linear programming helps in formulating such problems mathematically. For this task, we considered a manufacturing business that produces two products: Product A and Product B. Each product contributes differently to the overall profit and consumes different amounts of resources (labor hours and raw materials). Our aim was to determine the optimal number of units of each product to manufacture in order to maximize total profit, while not exceeding available resources.
🧰 Tools Used:
Python: Programming language used for implementation.
PuLP: A linear programming library in Python used to define and solve optimization problems.
Command Line / VS Code: For writing and executing the Python script.
🧮 Mathematical Model:
Decision Variables:
Let:
A = Number of units to produce of Product A
B = Number of units to produce of Product B
Objective Function (to maximize):
Profit = 20A + 30B
(Product A gives ₹20 per unit and Product B gives ₹30 per unit)
Constraints:
Labor hours: 2A + 1B ≤ 100
Material usage: 3A + 4B ≤ 240

Both decision variables must be greater than or equal to zero (A, B ≥ 0).
🧑‍💻 Implementation:
Using the PuLP library, we created an LP problem, defined the decision variables, objective function, and constraints. The problem.solve() function was used to compute the optimal solution.
Once executed, the script printed the optimal values of A and B along with the maximum profit.

#ouput:
<img width="978" height="107" alt="Image" src="https://github.com/user-attachments/assets/004ceede-f217-44a8-ac41-7fd738db9fb2" />
