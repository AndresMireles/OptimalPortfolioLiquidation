# Optimal Portfolio Liquidation

This project contains a complete replication of the model and numerical experiments presented in [Gueant, Lehalle, and Fernandez-Tapia (2012)](http://arxiv.org/abs/1106.3279). The codebase implements the theoretical framework for optimal portfolio liquidation using limit orders and extends the analysis with sensitivity studies and comparisons with benchmark strategies.

## What is Covered in the Code

### Core Modules

- **methods.py**  
  This module contains the fundamental numerical routines for solving the model. It implements:
  - **ODE Solver:** Uses a backward Euler scheme to solve the system of ordinary differential equations (ODEs) for the functions \(w_q(t)$ (see Equation (10) with terminal conditions in Equation (11) from the paper). These functions form the basis for computing the optimal ask quotes.
  - **Optimal Quote Computation:** Implements the formula for the optimal ask quote (Equation (13)) based on the precomputed \(w_q(t)$.

- **optimal_quotes.ipynb**  
  This script replicates the key figures from the original paper that display the evolution of the optimal ask quotes. It covers:
  - Short-horizon scenarios (e.g., 5-minute liquidation windows).
  - Long-horizon scenarios (e.g., 2-hour liquidation windows).
  - Comparison of the numerical outputs with the analytical expressions provided in the paper.

- **trading_curve.ipynb**  
  This script simulates the trading process using Monte Carlo methods. It:
  - Implements the dynamics of the inventory process, price process (using the Euler–Maruyama discretization), and cash process.
  - Generates trading curves, which plot the average remaining inventory over time.
  - Illustrates how the optimal strategy gradually reduces the inventory over the liquidation horizon.

- **sensitivity.ipynb**  
  In this script, we perform a detailed sensitivity analysis by varying key model parameters:
  - Parameters such as volatility $sigma$, execution intensity scale $A$, liquidation cost $b$, risk aversion $gamma$, intensity decay $k$, and drift $mu$.
  - Plots are generated to show how the optimal ask quote $\delta^{a*}(0,q)$ changes with inventory $q$ for different values of these parameters.
  - These experiments help validate the model's behavior as predicted by the analytical formulas in the paper.

- **strategies_comparison.ipynb**  
  This module extends the analysis by comparing the optimal strategy with three benchmark strategies:
  - **Safe Strategy:** Posts conservative quotes that depend on inventory.
  - **Greedy Strategy:** Uses a fixed, higher quote regardless of inventory.
  - **Random Strategy:** Samples quotes uniformly from a predefined interval.
  - The script simulates the trading curves and final cash distributions for each strategy, enabling a performance comparison in terms of liquidation speed and cash outcomes.

## Summary

The code in this project replicates the theoretical framework of [Gueant, Lehalle, and Fernandez-Tapia (2012)] and includes:
- A robust numerical solver for the ODE system underlying the optimal quote computation.
- Monte Carlo simulations to analyze trading dynamics.
- Sensitivity analysis to assess the impact of key parameters.
- Benchmark strategy comparisons to evaluate performance trade-offs.

Feel free to explore the source files in the `src/` directory and the accompanying LaTeX report in the `report/` folder for a detailed exposition of the methodology and results.
