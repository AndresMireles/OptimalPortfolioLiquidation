# OptimalPortfolioLiquidation

This project replicates and extends the theoretical and numerical results of [Gueant, Lehalle, and Fernandez-Tapia (2012)](http://arxiv.org/abs/1106.3279) on optimal portfolio liquidation using limit orders. The implementation uses a backward Euler scheme to solve the associated ODE system from the Hamilton-Jacobi-Bellman framework, performs Monte Carlo simulations for trading dynamics, and includes extensive sensitivity and benchmark strategy analyses.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Replicating the Results](#replicating-the-results)
  - [Sensitivity Analysis](#sensitivity-analysis)
  - [Benchmark Strategies](#benchmark-strategies)
- [Files and Directories](#files-and-directories)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project replicates the key results of Gueant, Lehalle, and Fernandez-Tapia (2012) on optimal portfolio liquidation. Specifically, it:
- Solves the ODE system derived from the HJB equation using a backward Euler method.
- Computes the optimal ask quotes, trading curves, and limit-case behaviors.
- Performs sensitivity analysis with respect to model parameters such as volatility $sigma$, intensity scale $A$, liquidation cost $b$, risk aversion $gamma$, and the intensity decay parameter $k$.
- Compares the optimal strategy with several benchmark strategies (safe, greedy, and random) 
