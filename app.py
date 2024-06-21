import tkinter as tk
from generator import generate_sudoku

# Initialize Tkinter root window
root = tk.Tk()
root.title("Sudoku Classic")
root.resizable(0, 0)  # Disable resizing

# Generate Sudoku board
sudoku_board = generate_sudoku('easy')

# Function to display Sudoku board
def display_sudoku(board):
    frames = [[None] * 3 for _ in range(3)]
    entries = [[None] * 9 for _ in range(9)]

    def on_click(event):
        # Clear the entry's content when clicked
        event.widget.delete(0, tk.END)

    # Calculate frame size based on window size and number of cells
    min_frame_size = 20  # Adjust as needed
    frame_size = max(min_frame_size, min(root.winfo_width(), root.winfo_height()) // 12)

    for i in range(3):
        for j in range(3):
            frame = tk.Frame(root, width=3 * frame_size, height=3 * frame_size, highlightbackground="black", highlightthickness=2)
            frame.grid(row=i, column=j, padx=1, pady=1)
            frames[i][j] = frame

    for i in range(9):
        for j in range(9):
            frame = frames[i // 3][j // 3]
            subframe = tk.Frame(frame, width=frame_size, height=frame_size, highlightbackground="red", highlightthickness=0)
            subframe.grid(row=i % 3, column=j % 3)
            if board[i][j] != "":
                label = tk.Label(subframe, text=str(board[i][j]), font=('Arial', 20), width=2, relief="ridge")
                label.pack(ipadx=10, ipady=10)
            else:
                entry = tk.Entry(subframe, font=('Arial', 20), width=2, justify='center')
                entry.bind("<Button-1>", on_click)
                entry.pack(ipadx=10, ipady=10)
                entries[i][j] = entry

    # Submit button function
    def submit():
        for i in range(9):
            for j in range(9):
                if entries[i][j] is not None:
                    value = entries[i][j].get()
                    if value.isdigit() and 1 <= int(value) <= 9:
                        board[i][j] = int(value)
                    else:
                        board[i][j] = ""
        # Update display with new board state
        refresh_sudoku()

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=4, columnspan=3, pady=10)

# Function to refresh the Sudoku display with updated board
def refresh_sudoku():
    for widget in root.winfo_children():
        widget.destroy()
    display_sudoku(sudoku_board)

# Function to handle resize event with delay
def on_resize(event):
    if event.widget == root:
        if root.after_id is not None:
            root.after_cancel(root.after_id)  # Cancel any pending refresh
        root.after_id = root.after(200, refresh_sudoku)  # Delay refresh by 200ms

# Initialize the after_id attribute
root.after_id = None

# Bind event to resize the Sudoku board
root.bind("<Configure>", on_resize)
display_sudoku(sudoku_board)

root.mainloop()