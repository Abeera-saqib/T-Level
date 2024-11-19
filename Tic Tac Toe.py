import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[' ']*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text=" ", font=("Helvetica", 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
    
    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Congratulations!", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.toggle_player()
    
    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
                self.board[i][j] = ' '
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
