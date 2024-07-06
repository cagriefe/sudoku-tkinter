# Sudoku Classic

A Sudoku game built with Python and Tkinter. This project includes functionalities to generate, display, and validate Sudoku boards with varying difficulties.

## Features

- Generate random Sudoku puzzles with different difficulty levels (easy, medium, hard).
- Display Sudoku board using Tkinter GUI.
- Allow user input to solve the Sudoku puzzle.
- Validate user solution.
- Make user-inputted cells read-only upon successful validation.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sudoku-classic.git
```

2. Navigate to the project directory:

```bash
cd sudoku-classic
```

3. Ensure you have Python installed (preferably Python 3.6+).

4. Install the required packages (Tkinter is included in standard Python installations):

```bash
pip install tkinter
```

## Usage

Run the application using the following command:

```bash
python app.py
```

## Project Structure

- `app.py`: The main application file that initializes the Tkinter GUI and handles user interactions.
- `generator.py`: Contains functions to generate a valid Sudoku board, solve the board, and remove numbers according to the selected difficulty.
- `validate.py`: Contains functions to validate the Sudoku board ensuring there are no duplicate numbers in rows, columns, and 3x3 grids.

## Example

When you run `app.py`, a Tkinter window will appear displaying a Sudoku board with some pre-filled cells. You can fill in the empty cells and press the "Submit" button to validate your solution. If the board is valid, the user-inputted cells will become read-only.

## License

This project is licensed under the GMU License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Sudoku puzzle generation and solving logic is inspired by common algorithms and methodologies used in the Sudoku community.
- Tkinter for providing the GUI components to build this application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve this project.

## Contact

If you have any questions or suggestions, please feel free to contact me.