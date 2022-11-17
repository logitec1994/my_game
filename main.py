from art import tprint
from game import Game

logo = "Main menu"

tprint(logo, "Bold")

print("1: New game")
print("2: Quit")

ans = input("Coise: ")

while Game.is_game:
    match ans:
        case "1":
            print("Game is ON! Enjoy")
        case _:
            is_game = False