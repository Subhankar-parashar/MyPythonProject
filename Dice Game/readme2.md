Target Sum Dice Generator

Overview

This Python project generates random dice values that add up to a user-specified total while ensuring every die remains within the valid range of 1–6.

Unlike a normal dice roller, the user chooses the desired total first, and the program creates a valid random combination of dice values that matches that total.

Features

* User selects:
    * Desired total
    * Number of dice
* Validates whether the requested total is possible
* Generates random dice values that exactly match the target total
* Displays the resulting dice using ASCII art
* Prevents impossible combinations

Concepts Used

* Lists
* Dictionaries
* Random Module
* Input Validation
* Loops
* Conditional Statements
* Constraint-Based Random Generation
* ASCII Art Rendering

How It Works

Step 1: Validation

For a given number of dice:

Minimum Possible Total:

Number of Dice × 1

Maximum Possible Total:

Number of Dice × 6

Example:

3 Dice

Minimum Total = 3

Maximum Total = 18

The program rejects any total outside this range.

Step 2: Generate Dice

* Every die starts with a value of 1.
* The remaining points are distributed randomly among the dice.
* No die is allowed to exceed 6.
* Distribution continues until the target total is reached.

Example

Input:

Enter the total: 15
Enter the no. of dice: 4

Output:

Dice values: [4, 2, 6, 3]
Total: 15

(ASCII Art Display)

Algorithm

1. Initialize all dice to 1.
2. Calculate remaining points.
3. Randomly select a die.
4. Add points without exceeding 6.
5. Repeat until no points remain.

Possible Improvements

* Fix ASCII-art display bug in the current version.
* Display dice horizontally.
* Generate all possible combinations for a given total.
* Add statistics and probability calculations.
* Create a graphical user interface using Tkinter.

Author

Subhankar

Created while learning Python programming and problem-solving with Python.