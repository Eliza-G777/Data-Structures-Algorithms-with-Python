# CodeCraft: Data Structures & Algorithms in Python

Implementations of core data structures and algorithms in Python, written from scratch, along with three applications that use them and an experiment on sorting performance.

## Contents

### Fundamentals
Python basics, recursion, and Big O notation.

### Data structures
- Arrays
- Linked lists
- Stacks and queues
- Hash tables
- Binary search trees
- Graphs (adjacency list and matrix)
- Heaps / priority queues

### Algorithms
- Searching: linear search, binary search
- Sorting: bubble, selection, insertion, merge sort
- Graphs: BFS, DFS, connected components, Dijkstra's shortest path
- Problem-solving: two pointers, greedy, divide and conquer, dynamic programming

### Projects
- **Maze Solver**: finds the shortest path through a maze using BFS, and compares it with DFS and A*.
- **Student Search System**: stores and searches student records, comparing lookup methods.
- **Study Scheduler**: orders study tasks by priority using a heap.

### Experiments
- **Sorting performance**: how input size affects the running time of different sorting algorithms.

## Repository structure

```
01_fundamentals/      Python basics, recursion, complexity
02_data_structures/   Data structure implementations
03_algorithms/        Searching, sorting, graph algorithms
04_problem_solving/   Problem solutions with explanations
projects/             Maze Solver, Student Search, Study Scheduler
experiments/          Performance experiments and reports
tests/                Unit tests
```

## Running the code

Requires Python 3.10 or newer.

```bash
python 01_fundamentals/<file>.py
```

Tests use pytest:

```bash
pip install pytest
pytest
```
