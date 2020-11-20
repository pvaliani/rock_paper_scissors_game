# - Class definition for the Rock, Paper, Scissors game

# - Import the Player class from the player.py class file 

from app.models.player import *

class Game():

    # - Initialise variables for the Game class 

    # - The class will take in two object instances of Player


    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result = ''


    def play_game(self, player_1, player_2):
    
    # - The winner is determined based on the rules and player choices - can refactor this later
        if self.player_1.choice == self.player_2.choice:
            self.result = "The game is a tie"

        elif(self.player_1.choice == "rock" and self.player_2.choice == "scissors") or \
            (self.player_1.choice == "scissors" and self.player_2.choice == "paper") or \
            (self.player_1.choice == "paper" and self.player_2.choice == "rock"):
            self._result =  f"{self.player_1.name} has won!"
        
        else:
            self.result = f"{self.player_2.name} has won!"