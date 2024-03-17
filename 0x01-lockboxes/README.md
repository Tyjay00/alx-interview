# Lockboxes

## Introduction
This repository contains a Python script that implements a method for determining whether all boxes in a set of locked boxes can be opened. The problem statement involves having a collection of locked boxes numbered sequentially from 0 to n - 1, where each box may contain keys to other boxes. The task is to develop a function that returns `True` if all boxes can be opened, and `False` otherwise.

## Method
The method `canUnlockAll(boxes)` is implemented to solve the problem. It takes a list of lists (`boxes`) as input, where each inner list represents a box and contains integers representing the keys contained within that box. The function iterates through the boxes, keeping track of the keys it has collected and the boxes it can open. If it successfully opens all boxes, it returns `True`; otherwise, it returns `False`.

## Testing
The script includes a testing module that verifies the correctness of the implementation. The provided test cases cover various scenarios, including different box configurations and edge cases. Upon executing the script, it will run these test cases and print the results to the console.

## Execution
To execute the script, run the provided `main_0.py` file in the terminal:

```bash
./main_0.py
```
