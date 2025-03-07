# Optimal Portfolio Liquidation

This project contains a complete replication of the model and numerical experiments presented in [Guéant, Lehalle, and Fernandez-Tapia (2012)](http://arxiv.org/abs/1106.3279). The codebase implements the theoretical framework for optimal portfolio liquidation using limit orders and extends the analysis with sensitivity studies and comparisons with benchmark strategies.

## What is Covered in the Code

### Core Modules

- **methods.py**  
  This module contains the fundamental numerical routines for solving the model. It implements:
  - **ODE Solver:** Uses a backward Euler scheme to solve the system of ordinary differential equations (ODEs) for the functions $w_q(t)$ (see Equation (10) with terminal conditions in Equation (11) from the paper). These functions form the basis for computing the optimal ask quotes.
  - **Optimal Quote Computation:** Implements the formula for the optimal ask quote (Equation (13)) based on the precomputed $w_q(t)$.
  - **Trading Path Simulation:**  Simulates a number of price paths and evaluates the corresponding strategy, keeping track of cash and inventory.
- **optimal_quotes.ipynb**  
  This script replicates the key figures from the original paper that display the evolution of the optimal ask quotes. It covers:
  - Short-horizon scenarios (e.g., 5-minute liquidation windows).
  - Long-horizon scenarios (e.g., 2-hour liquidation windows).

- **trading_curve.ipynb**  
  This script simulates the trading process using Monte Carlo methods. It:
  - Implements the dynamics of the inventory process, price process (using the Euler–Maruyama discretization), and cash process.
  - Generates the corresponding trading curves, which capture the average remaining inventory over time.

- **sensitivities.ipynb**  
  In this script, we perform a sensitivity analysis by varying different model parameters:
  - Parameters such as volatility $\sigma$, execution intensity scale $A$, liquidation cost $b$, risk aversion $\gamma$, intensity decay $k$, and drift $\mu$.
  - Plots are generated to show how the optimal ask quote $\delta^{a*}(0,q)$ changes with inventory $q$ for different values of these parameters.

- **strategies_comparison.ipynb**  
  This module extends the analysis of the original paper by comparing the optimal strategy with three benchmark strategies:
  - **Safe Strategy:** Posts conservative quotes that depend on inventory.
  - **Greedy Strategy:** Uses a fixed, higher quote regardless of inventory.
  - **Random Strategy:** Samples quotes uniformly from a predefined interval.
  - The script simulates the trading curves and final cash distributions for each strategy.
 

![strategies_comparison_trading_curve](https://github.com/user-attachments/assets/5822627c-e342-4265-a402-b6f6788f5515)
![strategies_comparison_pnl](https://github.com/user-attachments/assets/6e5a8f20-921f-4fcb-b6a1-25b399e577e8)



