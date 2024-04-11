# N Queens

## Task Description

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.

## How to Solve

To solve the N queens problem, you can use backtracking algorithm. Here's a general approach:

1. Start with an empty chessboard.
2. Place a queen in the first row.
3. Move to the next row and place a queen in a safe position (where it doesn't attack any other queens).
4. Repeat step 3 for each row, backtracking when no safe position is found.
5. When all queens are placed, print the solution.

Ensure that queens are placed in such a way that they do not attack each other horizontally, vertically, or diagonally.
