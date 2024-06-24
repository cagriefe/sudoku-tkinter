import tkinter as tk
from generator import generate_sudoku
from validate import validate_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Classic")
        self.root.resizable(0, 0)

        self.sudoku_board = generate_sudoku('') #'easy','medium',''

        self.frames = [[None] * 3 for _ in range(3)]
        self.entries = [[None] * 9 for _ in range(9)]

        self.user_filled_cells = set()

        self.display_sudoku()

    def display_sudoku(self):
        frame_size = 50

        for i in range(3):
            for j in range(3):
                frame = tk.Frame(self.root, width=3 * frame_size, height=3 * frame_size, highlightbackground="black", highlightthickness=2)
                frame.grid(row=i, column=j, padx=1, pady=1)
                self.frames[i][j] = frame

        for i in range(9):
            for j in range(9):
                frame = self.frames[i // 3][j // 3]
                subframe = tk.Frame(frame, width=frame_size, height=frame_size, highlightbackground="red", highlightthickness=0)
                subframe.grid(row=i % 3, column=j % 3)
                if self.sudoku_board[i][j] != "":
                    label = tk.Label(subframe, text=str(self.sudoku_board[i][j]), font=('Arial', 20), width=2, relief="ridge")
                    label.pack(ipadx=10, ipady=10)
                else:
                    entry = tk.Entry(subframe, font=('Arial', 20), width=2, justify='center')
                    entry.pack(ipadx=10, ipady=10)
                    self.entries[i][j] = entry

        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.grid(row=4, columnspan=3, pady=10)

    def submit(self):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j] is not None and self.entries[i][j]['state'] != 'readonly':
                    value = self.entries[i][j].get()
                    if value.isdigit() and 1 <= int(value) <= 9:
                        self.sudoku_board[i][j] = int(value)
                        self.user_filled_cells.add((i, j))
                    else:
                        self.sudoku_board[i][j] = ""

        if validate_sudoku(self.sudoku_board):
            print("Board is valid")
            for i, j in self.user_filled_cells:
                if self.entries[i][j] is not None:
                    self.entries[i][j].config(state='readonly')
        else:
            print("Board is invalid")

        self.refresh_sudoku()

    def refresh_sudoku(self):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j] is not None and self.entries[i][j]['state'] != 'readonly':
                    self.entries[i][j].delete(0, tk.END)
                    if self.sudoku_board[i][j] != "":
                        self.entries[i][j].insert(0, str(self.sudoku_board[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()