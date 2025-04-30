import tkinter as tk
from tkinter import messagebox
import random
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        self.player = "X"
        self.ai = "O"
        self.current_player = "X"
        self.board = [""] * 9


        self.buttons = []
        self.create_board_buttons()

    def create_board_buttons(self):

        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 20),
                    width=5,
                    height=2,
                    command=lambda r=i, c=j: self.click(r, c)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def click(self, row, col):
        if self.current_player == self.player:
            index = 3 * row + col


            if self.board[index] == "":
                self.board[index] = self.player
                self.buttons[index].config(text=self.player, state="disabled")

                if self.check_winner(self.player):
                    messagebox.showinfo("Game Over", "You win!")
                    self.disable_buttons()
                elif "" not in self.board:
                    messagebox.showinfo("Game Over", "The game ended in a draw!")
                    self.disable_buttons()
                else:
                    self.current_player = self.ai
                    self.root.after(500, self.ai_move)

    def ai_move(self):
        best_move = self.find_best_move()
        if best_move is not None:
            self.board[best_move] = self.ai
            self.buttons[best_move].config(text=self.ai, state="disabled")

            if self.check_winner(self.ai):
                messagebox.showinfo("Game Over", "AI wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "The game ended in a draw!")
                self.disable_buttons()
            else:
                self.current_player = self.player

    def find_best_move(self):

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.ai
                if self.check_winner(self.ai):
                    self.board[i] = ""
                    return i
                self.board[i] = ""


        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.player
                if self.check_winner(self.player):
                    self.board[i] = ""
                    return i
                self.board[i] = ""


        empty_spots = []
        for i in range(9):
            if self.board[i] == "":
                empty_spots.append(i)
        if empty_spots:
            return random.choice(empty_spots)
        return None

    def check_winner(self, player):

        for i in range(0, 9, 3):
            if self.board[i] == player and self.board[i] == self.board[i + 1] == self.board[i + 2]:
                return True


        for i in range(3):
            if self.board[i] == player and self.board[i] == self.board[i + 3] == self.board[i + 6]:
                return True


        if self.board[0] == player and self.board[0] == self.board[4] == self.board[8]:
            return True
        if self.board[2] == player and self.board[2] == self.board[4] == self.board[6]:
            return True

        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()