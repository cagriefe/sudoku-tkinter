import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from generator import generate_sudoku

# Function to display Sudoku board
def display_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != "":
                label = tk.Label(root, text=str(board[i][j]), font=('Arial', 20), width=4, relief="ridge")
            else:
                label = tk.Label(root, text="", font=('Arial', 20), width=4, relief="ridge")
            label.grid(row=i, column=j, ipadx=20, ipady=20)

root = tk.Tk()
root.title("Sudoku Classic")
root.minsize(800, 800)
root.maxsize(1200, 1200)
root.resizable(0, 0)

# Generate Sudoku board
sudoku_board = generate_sudoku('easy')

# Display Sudoku board
display_sudoku(sudoku_board)

button = tk.Button(root, text="Submit!")

root.mainloop()