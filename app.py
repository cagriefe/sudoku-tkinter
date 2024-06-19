import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from generator import generate_sudoku

root = tk.Tk()
root.title("Sudoku Classic")
root.resizable(0, 0)


# Generate Sudoku board
sudoku_board = generate_sudoku('easy')


def display_sudoku(board):
    
    frames = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(root, highlightbackground="black", highlightthickness=5)
            frame.grid(row=i, column=j)
            frames[i][j] = frame

    for i in range(9):
        for j in range(9):
            frame = frames[i // 3][j // 3]
            subframe = tk.Frame(frame, highlightbackground="red", highlightthickness=0)
            subframe.grid(row=i % 3, column=j % 3)
            if board[i][j] != "":
                label = tk.Label(subframe, text=str(board[i][j]), font=('Arial', 20), width=2, relief="ridge")
            else:
                label = tk.Label(subframe, text="", font=('Arial', 20), width=2, relief="ridge")
            label.pack(ipadx=20, ipady=20)

display_sudoku(sudoku_board)
    
    

root.mainloop()