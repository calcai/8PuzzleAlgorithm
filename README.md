# 8 Puzzle Solver

This project creates an implementation of a 8 puzzle games and solves it with two different algorithms. The rules for the 8 puzzle game are as followed: you are given a 3x3 board with tiles placed numbered one through eight, and a blank tile. By swapping the blank (represented by zero) tile with adjacent (not diagonal) tiles, you want to make moves until the board is ordered from one to eight in left to right top down order, with the zero tile in the first position.

## A* Search
The first algorithm used is A* Search, in which two heuristics are used: the number of misplaced tiles, and the manhattan distance heuristic, which is the sum of all tiles distances from correct position.

A* Search: $f(n) = g(n) + h(n)$

where $f(n) =$ estimated total cost, $g(n) =$ cost from start node to node n, and $h(n) =$ estimated distance to goal state

## Beam Search
The next algorithm used is Beam Search, which similarly used Manhattan Distance, with its primary feature being that it limits the number of past moves to the "beam size", to limit space complexity.
