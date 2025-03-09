import numpy as np

class LPS:
    """
    Linear Programming Solver (LPS) for solving optimization problems using linear algebra.
    Determines the optimal solution for maximizing profit given constraints.
    """
    def __init__ (self, var, fX, cD, limits):
        """
        Initializes the LPS object with problem variables.

        Args:
            var (int): Number of variables.
            fX (list): Coefficients of the objective function.
            cD (list): Matrix representing constraint coefficients.
            limits (list): Constraint limits.
        """
        self.var = var
        self.fX = fX
        self.cD = cD
        self.limits = limits
    
    def linearCalc(self):
        """
        Computes the optimal solution for the linear programming problem.
        Determines the best option between solo options and a balanced option.
        """
        solo_options = []
        
        # Compute solo options sorted by the lowest constraint limit
        for i in range(self.var):
            solo_option = [0] * self.var
            solo_option[i] = min(self.limits[i], self.limits[i-1]) / self.cD[i][i]
            solo_options.append(solo_option)

        # Compute balanced option using numpy linear algebra solver
        A = np.array(self.cD)
        b = np.array(self.limits)
        balanced_option = np.linalg.solve(A, b)

        # Compute profits for solo options
        solo_profits = [solo_option[0] * self.fX[i] for i, solo_option in enumerate(solo_options)]
        balanced_profit = np.dot(self.fX, balanced_option)
        
        def display():
            """
            Displays the solution, including objective function, constraints, and best option.
            """
            print("Objective coefficients f(x):", self.fX)
            print("Constraint matrix is:")
            for row in self.cD:
                print(row) 
            print("The constraint limits are:", self.limits)

            print("\nSolo option profit:")
            for i, profit in enumerate(solo_profits):
                print(f"Solo option {i+1}: profit = ${profit:.2f}")

            print("\nBalanced option profit:")
            print(f"Balanced option: profit = ${balanced_profit:.2f}, {self.fX} balanced option= {balanced_option}")
            
            # Determine the best option
            best_option_index = np.argmax(solo_profits)
            if solo_profits[best_option_index] > balanced_profit:
                best_option = solo_options[best_option_index]
                best_profit = solo_profits[best_option_index]
                print("\nSolution:")
                print(f"The best option is Solo Option {best_option_index + 1} with a profit of ${best_profit:.2f}")
            else:
                print("\nSolution:")
                print(f"The best option is the Balanced Option with a profit of ${balanced_profit:.2f}")
    
        display()

def mainTest():
    """
    Executes an example test case using a pants and jackets production problem.
    """
    variableAcc = 2
    objective_function = [-150, -100]
    cd = [[4, 5], [3, 1]]
    limits = [80, 80]
    linear = LPS(variableAcc, objective_function, cd, limits)
    linear.linearCalc()
    
if __name__ == "__main__":
    mainTest()

"""Copy and pasted run of program:
--------------------------------------
Objective coefficients f(x): [50, 40]
Constraint matrix is:
[2, 3]
[2, 1]
The constraint limits are: [1500, 1000]

Solo option profit:
Solo option 1: profit = $25000.0.
Solo option 2: profit = $20000.0.

Balanced option profit:
Balanced option: profit = 28750.0, [50, 40] balanced option= [375. 250.]

Solution:
The best option is the Balanced Option with a profit of 28750.0
"""

