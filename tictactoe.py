import tkinter as tk
from tkinter import messagebox

c1="#B0C4DE"
c2="#000000"
class TTT:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("470x350")
        self.window.resizable(0, 0)
        self.window.title("Tic Tac Toe")
        self.window.configure(background="#B0E0E6")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.place()

    def bc(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled", disabledforeground="black")
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"

    def place(self):
        self.buttons = []
        button_font = ("Helvetica", 20, "bold")
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = tk.Button(self.window, text="", width=8, height=2, font=button_font, bg=c1, fg=c2,
                                   command=lambda r=row, c=col: self.bc(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        restart_button = tk.Button(self.window, text="Restart", font=("Helvetica", 14, "bold"), bg="#3cb371", fg="white",
                                   command=self.restart_game)
        restart_button.grid(row=3, column=0, columnspan=3, pady=10)

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def reset_board(self):
        # Clear the board and reset buttons
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="active")

    def restart_game(self):
        self.reset_board()
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ttt = TTT()
    ttt.run()



