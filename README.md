# AI Algorithms in Python

> Sup fellow coders! 🤘 Dumping my AI algorithm collection from those loooong college nights when coffee was my best friend and sleep was just a concept.

<p align="center">
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" alt="AI Brain" width="300" />
</p>

## 📚 Table of Contents
- [🛠️ What's Inside](#️-whats-inside)
- [⚙️ Installation](#️-installation)
- [🚀 How to Run](#-how-to-run)
- [👾 Algorithm Breakdown](#-algorithm-breakdown)
- [☕ Java Version](#-java-version)
- [🤝 Contributing](#-contributing)
- [⚠️ Disclaimer](#️-disclaimer)

## 🛠️ What's Inside

Here's the AI stuff I survived implementing:

<details>
<summary><b>🔍 Search Algorithms</b> - Finding paths through problems</summary>
<br>

| Algorithm | Description | File |
|-----------|-------------|------|
| **BFS** | Breadth-First Search - Explores all neighbors before going deeper | `BFS_UCS.py` |
| **DFS** | Depth-First Search - Goes as deep as possible before backtracking | `DFS.py` |
| **DFID** | Depth-First Iterative Deepening - Combines BFS's completeness with DFS's memory efficiency | `DFID.py` |
| **UCS** | Uniform Cost Search - Like BFS but considers path costs | `BFS_UCS.py` |
| **A*** | A-Star - Uses heuristics to find optimal paths efficiently | `A_star.py` |

</details>

<details>
<summary><b>⛰️ Hill Climbing</b> - Just keeps going up until it can't anymore</summary>
<br>

Simple optimization algorithm that:
- Starts at a random solution
- Iteratively makes small improvements
- Stops when no better neighbor exists
- Often gets stuck in local maxima

```python
def hill_climbing(problem):
    current = problem.initial()
    while True:
        neighbor = problem.best_neighbor(current)
        if problem.value(neighbor) <= problem.value(current):
            return current
        current = neighbor
```

</details>

<details>
<summary><b>🧬 Genetic Algorithms</b> - Digital Darwin stuff where code evolves and the fittest survives</summary>
<br>

Evolution-inspired approach that:
- Creates a population of potential solutions
- Evaluates their fitness
- Selects the best individuals
- Creates new solutions through crossover and mutation
- Repeats until convergence

</details>

<details>
<summary><b>🧠 Prolog</b> - Logic programming that'll make you question your life choices 🤔</summary>
<br>

Python implementations of logic programming concepts:
- Knowledge representation
- Rule-based systems
- Logical inference

</details>

## ⚙️ Installation

```bash
# Clone this repository
git clone https://github.com/Jia2005/AI-codes-in-Python.git

# Navigate into the directory
cd AI-codes-in-Python

# No external dependencies required - just Python 3.6+
```

## 🚀 How to Run

```bash
# Run any algorithm (example with BFS/UCS)
python3 BFS_UCS.py

# Run other algorithms
python3 DFS.py
python3 DFID.py
python3 A_star.py
```

## 👾 Algorithm Breakdown

### Search Algorithms Visualized

```
BFS                          DFS
────────────                 ────────────
   [1]                          [1]
  ↙   ↘                        ↙   ↘
[2]     [3]                  [2]     [3]
↙ ↘     ↙ ↘                 ↙        ↙ ↘
4   5   6   7               4        6   7
                            ↙
                           5
```

- **BFS/DFS**: Think of these as different ways to explore a maze - BFS goes wide, DFS goes deep
- **A***: The overachiever that finds optimal paths while being smart about it
- **Genetic Algorithms**: Digital survival of the fittest - letting solutions evolve through generations
- **Hill Climbing**: Like hiking with no map - just keep going up and hope for the best

## ☕ Java Version

More of a Java person? No judgment (ok maybe a little 😉)

<a href="https://github.com/Jia2005/AI-codes-in-Java">
  <img src="https://img.shields.io/badge/Check%20out-Java%20Version-orange?style=for-the-badge&logo=java" alt="Java Version" />
</a>

## 🤝 Contributing

Found a bug? Have a better way to implement something? Open a pull request!

```
1. Fork the repository
2. Create your feature branch: git checkout -b amazing-feature
3. Commit your changes: git commit -m 'Add some amazing feature'
4. Push to the branch: git push origin amazing-feature
5. Open a pull request
```

<p align="center">
  If this helped you with your assignments or understanding AI concepts, a star ⭐ would be awesome.<br>
  No pressure... (but seriously, it takes like 2 seconds)
</p>

## ⚠️ Disclaimer

Fair warning: This is college-assignment-level code. It works, it's readable, but it's not winning any optimization awards. 

Think "Toyota Corolla" not "Ferrari" - gets the job done but don't expect miracles.

---

<div align="center">
  Made with ☕ and 😴 deprivation
</div>
