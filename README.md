Minesweeper is a classic game implemented in Python using core programming concepts such as recursion, arrays (2D lists), and game state management. This project is a command-line based version that focuses on clean logic and fundamental problem-solving techniques rather than graphics.

The game generates a grid dynamically, places mines randomly, and calculates the number of adjacent mines for each cell. When a player reveals an empty cell, recursion is used to automatically reveal neighboring safe cells. The game continues until the player either reveals all non-mine cells or hits a mine.

This project demonstrates the use of conditional statements, loops, recursion, and structured program flow in Python. It is intended as a learning project for understanding how classic games manage state and logic at a fundamental level.

The code is simple, readable, and easy to modify, making it suitable for beginners who want to practice Python programming and game logic development.
Instructions

Requirements

Python 3.x installed

How to Run

Download or clone the project

Open a terminal in the project folder

Run the file using:
python minesweeper.py

How to Play

The game displays an 8 x 8 grid

Enter the row number and column number when prompted

Revealing a mine ends the game

Revealing all safe cells wins the game

Game Rules

Numbers indicate how many mines are adjacent to a cell

Empty cells automatically reveal nearby safe cells using recursion

Notes

This is a command-line based game

Grid size and number of mines can be changed in the code

Built using basic Python concepts for learning purposes