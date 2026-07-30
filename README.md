#
TFT Set 18 Trait Tool

This tool is a mathematical optimization program designed for Teamfight Tactics (TFT) Set 18. It calculates the best possible boards to maximize the number of active traits for a given board size while strictly minimizing the total gold cost.

## 🎯 Motivation

This optimizer was explicitly built to maximize the value of specific TFT augments that reward fielding a high volume of traits. It is highly effective for maximizing the value of:

* **Trait Ladder:** Gain a random emblem. After fielding non-unique traits in a player combat, gain a reward. Then increase the number of traits needed and the size of the reward.
* **Bronze For Life I:** Your team gains Damage Amp for each Bronze-tier trait.
* **Bronze For Life II:** Your team gains Damage Amp and Armor and Magic Resist for each Bronze-tier trait.

By utilizing this script, you can immediately identify the cheapest "trait soup" boards to farm the highest possible yields from these specific augments.

## ✨ Key Features

* **Trait Maximization:** Uses MILP (Mixed-Integer Linear Programming) via the `pulp` library to find the absolute maximum number of active traits that can fit on your board.
* **Cost Minimization:** Out of thousands of valid combinations, it filters and returns only the boards that require the least amount of gold to build.
* **Unit Frequency Stats:** Analyzes the top 20 optimal boards and provides a percentage breakdown of the most essential units, allowing you to prioritize the correct champions in your shop.
* **Custom Filters:** 
  * Force specific traits to be active.
  * Simulate holding a +1 emblem.
  * Exclude expensive 4/5-cost units from the pool.
  * Set a custom minimum trait target to lower costs further.

## 🚀 Installation & Usage

### 1. Requirements
Ensure you have [Python](https://www.python.org/downloads/) installed on your system.

### 2. Install Dependencies
The application requires the `pulp` library to solve optimization problems. Install it via terminal/command prompt:
```bash
pip install pulp
```

### 3. Run the Application

Save the script as a Python file (e.g., `tool.py`) and execute it via your terminal or command prompt:

```bash
python tool.py
```
