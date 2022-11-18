from art import tprint
from game import Game
from character import Character

logo = "Main menu"

tprint(logo, "Bold")

print("1: New game")
print("2: Quit")

ans = input("Coise: ")

game = Game()
char = Character()
char.create()

match ans:
    case "1":
        game.is_game = True
        print("Game is ON! Enjoy")
        while game.is_game:
            if char.get_health() < 0:
                game.is_game = False
    case _:
        Game.is_game = False

