# European Floating-Strike Asian Call Option Pricing

## Overview

This repository contains a mathematical model and Python implementation for pricing a European floating-strike Asian call option. This project was developed as part of the Stochastic Methods in Finance course at the University of St. Gallen. 

The primary goal is to build and implement a multi-period binomial tree model to establish the arbitrage-free price of the option. The model is calibrated using real-world historical data from Apple Inc. (AAPL) sourced from Yahoo Finance.


---

## Project Structure

The project is organized into the following directories and files, as seen in the repository's architecture:

###  Code
* **`Data_downloader.py`**: A script designed to download historical prices for Apple Inc. and calculate the annualized volatility $\sigma$ based on daily returns from 2020 to 2026.
* **`Tasks_i)-v).ipynb`**: The main Jupyter notebook containing the implementation of the 25-period binomial tree, the augmented state-space logic for path-dependency, the backward induction pricing algorithm, as well as a robstuness check.
* **`Task_vii.ipynb`**: A dedicated notebook for developing the normal distribution approximation used to validate the binomial model's results.

### Data
* **`aapl_28apr.csv`**: The dataset containing historical price information used to set the initial price $S_0$ as of April 28, 2026.

---

## Key Features

* **Augmented State Space**: To handle the path-dependency of the Asian option, the model tracks both the current stock price $S_t$ and the cumulative sum $C_t$ at each node to maintain the Markov property.
* **Risk-Neutral Pricing**: Derivation and application of risk-neutral probabilities $q$ to ensure an arbitrage-free valuation.
* **Visual Analysis**: Includes distributions of terminal payoffs and visualizations of path dependency (Terminal Price $S_n$ vs. Arithmetic Average $\bar{S}_n$).

---

## Mathematical Setup

The model follows the Cox-Ross-Rubinstein (CRR) framework with the following parameters:
* **Maturity ($T$)**: 6 months.
* **Steps ($n$)**: 25 periods.
* **Risk-free rate ($r$)**: 1% per annum.
* **Payoff Function**: $A_{T} = \max\left(S_{n} - \frac{1}{n+1}\sum_{t=0}^{n}S_{t}, 0\right)$.

---

## Usage

* Calibration: Run Data_downloader.py to obtain the daily historical returns from Yahoo Finance.
* Tree Construction: Open Tasks_i-v.ipynb to build the tree and compute the risk-neutral probabilities $q$ based on the risk-free rate of 1%.  
* Pricing: The notebooks execute backward induction to find the price at $t=0$, accounting for path history through the running average. 

---

## Source Code Directory Tree

```bash
.
├── Code
│   ├── Data_downloader.py
│   ├── Task_vii.ipynb
│   └── Tasks_i-vi.ipynb
├── Data
│   └── aapl_28apr.csv
├── README.md
├── LICENSE
└── .gitignore
```