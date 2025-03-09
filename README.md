# Linear Programming Solver (LPS)

## Overview
This project implements a **Linear Programming Solver (LPS)** that optimizes a given objective function subject to constraints using linear algebra.

## Features
- Computes the best production strategy to maximize profit.
- Compares individual production options with a balanced approach.
- Uses **NumPy** for efficient matrix calculations.
- Displays clear results including profits and the best choice.

## How It Works
1. **Define the Problem**: Inputs include:
   - Objective function coefficients.
   - Constraint coefficients.
   - Constraint limits.
   - Number of variables.
2. **Compute Options**:
   - Computes **solo options** (one variable at a time).
   - Computes a **balanced option** using NumPy's `linalg.solve()`.
3. **Compare Profits**:
   - Calculates profit for each option.
   - Displays the best choice.

## Installation
Ensure you have Python installed. Clone the repository and install **NumPy** if not already installed:
```bash
pip install numpy
```

## Usage
Run the script:
```bash
LPS.py
```
It will execute an example test case optimizing the production of pants and jackets based on given constraints.

## Example Interaction
```
Objective coefficients f(x): [-150, -100]
Constraint matrix is:
[4, 5]
[3, 1]
The constraint limits are: [80, 80]

Solo option profit:
Solo option 1: profit = $-3000.00
Solo option 2: profit = $-1600.00

Balanced option profit:
Balanced option: profit = $-2800.00, [-150, -100] balanced option= [10. 50.]

Solution:
The best option is the Balanced Option with a profit of $-2800.00
```

## License
This project is open-source and free to use.
