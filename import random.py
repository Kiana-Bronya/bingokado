import tkinter as tk
import random

class BingoCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo Card Generator")
        self.grid_size = 5
        self.bingo_numbers = self.generate_bingo_numbers()
        self.selected_cells = set()
        self.buttons = []

        # Create Bingo Grid
        self.create_bingo_grid()

    def generate_bingo_numbers(self):
        # Generate unique numbers for a 5x5 bingo card according to traditional bingo rules
        columns = {
            "B": random.sample(range(1, 16), self.grid_size),
            "I": random.sample(range(16, 31), self.grid_size),
            "N": random.sample(range(31, 46), self.grid_size),
            "G": random.sample(range(46, 61), self.grid_size),
            "O": random.sample(range(61, 76), self.grid_size),
        }

        # Combine columns to form the 5x5 grid
        bingo_numbers = []
        for key in columns:
            bingo_numbers.extend(columns[key])

        random.shuffle(bingo_numbers)
        return bingo_numbers

    def create_bingo_grid(self):
        # Populate the 5x5 grid with buttons
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                index = i * self.grid_size + j
                number = self.bingo_numbers[index]
                button = tk.Button(self.root, text=str(number), width=5, height=2)
                button.config(command=lambda b=button: self.select_number(b))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def select_number(self, button):
        # Mark a number as selected
        if button in self.selected_cells:
            return
        button.config(bg="lightgreen")
        self.selected_cells.add(button)
        self.check_bingo()

    def check_bingo(self):
        # Check for bingo and reach conditions
        selected_positions = {(button.grid_info()['row'], button.grid_info()['column'])
                              for button in self.selected_cells}
        for row in range(self.grid_size):
            if all((row, col) in selected_positions for col in range(self.grid_size)):
                self.show_message("Bingo!")
                return
        for col in range(self.grid_size):
            if all((row, col) in selected_positions for row in range(self.grid_size)):
                self.show_message("Bingo!")
                return

    def show_message(self, message):
        popup = tk.Toplevel()
        tk.Label(popup, text=message).pack()
        tk.Button(popup, text="OK", command=popup.destroy).pack()

# Initialize GUI
root = tk.Tk()
bingo_app = BingoCard(root)
root.mainloop()
