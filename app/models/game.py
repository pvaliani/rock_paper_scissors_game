# - Class definition for the Rock, Paper, Scissors game

# - Import the Player class from the player.py class file 

from app.models.player import *

class Game():

    # - Initialise variables for the Game class 

    # - The class will take in two object instances of Player


    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        


    def play_game(self, player_1, player_2):
    
    # - The winner is determined based on the rules and player choices - can refactor this later

    # - If player choices match then result = "None" i.e the game is a draw

        if (self.player_1.choice == self.player_2.choice):
            result = "None"

    # - Else compare the values of player choice for the scenario of rock vs paper and define the result as paper

        elif(( self.player_1.choice == "Rock" and self.player_2.choice =="Paper" ) or ( self.player_1.choice == "Paper" and self.player_2.choice =="Rock" )):
            result = "Paper"
    
    # - Else compare the values of player choice for the scenario of scissors vs paper and define the result as scissors

        elif(( self.player_1.choice == "Scissors" and self.player_2.choice =="Paper" ) or ( self.player_1.choice == "Paper" and self.player_2.choice =="Scissors" )):
            result= "Scissors"

    # - Else the result must be that rock wins

        else:
            result= "Rock"

    # - If the the result is the same as player_1's choice then player_1 is returned as the winner else the winner is player_2

        if result == self.player_1.choice:
            return player_1.name
        else:
            return player_2.name