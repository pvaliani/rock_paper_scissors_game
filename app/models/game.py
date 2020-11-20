# - Class definition for the Rock, Paper, Scissors game

# - Import the Player class from the player.py class file 

from app.models.player import *

class Game():

    # - Initialise variables for the Game class
    
    def __init__(self, player_1, player_2, player_1_choice, player_2_choice):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_choice = player_1_choice
        self.player_2_choice = player_2_choice


    def determine_winner(self, player_1, player_2, player_1_choice, player_2_choice):
        pass