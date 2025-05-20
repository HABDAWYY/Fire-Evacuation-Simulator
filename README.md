# 🔥 Fire Evacuation Simulator

This project simulates a fire evacuation scenario on a 10×10 grid. It models people escaping fire and smoke using two search algorithms: **Breadth-First Search (BFS)** for the shortest path and **Uniform Cost Search (UCS)** for the safest path considering fire and smoke hazards.

## 📋 Features

- Fire spreads to adjacent cells and creates smoke.
- People (`P`) must reach the nearest exit (`E`) while avoiding fire (`F`), smoke (`S`), and obstacles (`X`).
- BFS is used to find the **shortest path** to the nearest exit.
- UCS is used to find the **safest path**, minimizing movement cost (with smoke being more costly).

## 🔧 Grid Representation

The environment is defined using a 10×10 ASCII grid where:

| Symbol | Meaning        |
|--------|----------------|
| `.`    | Empty space    |
| `F`    | Fire source    |
| `S`    | Smoke          |
| `X`    | Wall/Obstacle  |
| `E`    | Exit           |
| `P`    | Person         |

Example grid:
. . . F . . . E . .
. X X . X X . . . .
. . . . . . . . . .
. . . S . . X . . .
. . X S . . . . . .
X . . . X . . . . .
. . . . . X . P . .
. . . . X . . . . .
. . . . . . . . . .
E . . . . . . P . .

## 🧠 Algorithms

### ✅ Breadth-First Search (BFS)
- Finds the minimum number of steps to the nearest exit.
- Avoids fire and obstacles.

### ✅ Uniform Cost Search (UCS)
- Computes the least-cost path to the exit.
- Takes into account:
  - Empty cell cost: `1`
  - Smoke cost: `3`
  - Fire is impassable: `∞`

## 🛠 Functions

- `bfs(start: Person)` – Returns number of steps to nearest exit using BFS.
- `UCS(start: Person)` – Returns movement cost to nearest exit using UCS.
- `fire_spread(grid)` – Simulates fire spreading and turning adjacent cells to smoke.
- `simulate(full_grid)` – Detects people and exits, performs one step of fire spread, then applies BFS and UCS to each person.
