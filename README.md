# Maze Escape AI (CodinGame Puzzle)

## Overview

This project is a solution to a maze-based puzzle from CodinGame.
The goal is to control a character (Rick) navigating through an unknown maze, locating a control room, and escaping before an alarm triggers.

The maze is partially hidden and revealed progressively, requiring both **exploration** and **path optimization**.

---

## Problem Description

* The maze is a grid of size `R x C`
* Cells may contain:

  * `#` → Wall
  * `.` → Empty space
  * `T` → Exit
  * `C` → Control room
  * `?` → Unknown cell

### Objectives:

1. Explore the maze to find the control room (`C`)
2. Determine if it is possible to reach the exit (`T`) within the allowed number of turns after triggering the alarm
3. If safe, go to `C`, then return to `T`
4. Otherwise, continue exploring

---

## Approach

The solution is based on:

### Breadth-First Search (BFS)

* Used to compute shortest paths in the maze
* Handles both:

  * Exploration (towards unknown cells `?`)
  * Optimal routing (towards `C` and `T`)

### Strategy

* If the control room is not found → explore unknown areas
* Once found:

  * Compute shortest path from `C` to `T`
  * If the path is short enough (≤ alarm timer):

    * Go to `C`
    * Then return to `T`
  * Otherwise:

    * Keep exploring

---

## Key Functions

* `find_path_bfs(...)`
  Computes shortest path using BFS

* `proximiter(...)`
  Returns accessible neighboring cells

* `proximiter_pt(...)`
  Same as above but avoids unknown cells

---

## How to Run

This script is designed to run inside the CodinGame environment.


## Project History

This project was originally developed in **June 2023** as part of a CodinGame challenge.
The Git repository and commit history were created later for archival.


