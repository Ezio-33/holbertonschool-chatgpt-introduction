#!/usr/bin/python3
import random

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.total_non_mine_cells = width * height - mines
        self.non_mine_cells_revealed = 0

    def print_board(self, reveal=False):
        print('  ', end='')
        for i in range(self.width):
            print(i, end=' ')
        print()
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or (x, y) in self.mines:
                    print('.', end=' ')
                else:
                    print(self.board[y][x], end=' ')
            print()

    def reveal(self, x, y):
        if (x, y) in self.mines:
            return False
        count = sum(1 for i in range(max(0, x-1), min(self.width, x+2))
                     for j in range(max(0, y-1), min(self.height, y+2))
                     if (i, j) in self.mines)
        self.board[y][x] = count
        self.non_mine_cells_revealed += 1
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Entrez la coordonnée x: "))
                y = int(input("Entrez la coordonnée y: "))
                if self.reveal(x, y):
                    if self.non_mine_cells_revealed == self.total_non_mine_cells:
                        self.print_board(reveal=True)
                        print("Félicitations ! Vous avez gagné le jeu.")
                        break
            except ValueError:
                print("Veuillez entrer des coordonnées valides.")


# Exemple d'utilisation
minesweeper = Minesweeper()
minesweeper.play()