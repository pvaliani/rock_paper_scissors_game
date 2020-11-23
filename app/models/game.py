# - Class definition for the Rock, Paper, Scissors game

# - Import the Player class from the player.py class file 

from app.models.player import *

import random

class Game():

    # - Initialise variables for the Game class 

    # - Initialise two variables player_1 and player_2 to be utilised by play_game using self as the reference

    # - Don't need a constructor for players. Can just pass the players in as part of the game class

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def play_game(self):

    # - If player 2's name is Computer and their choice selection is empty then set Computer's choice using the method below

        if self.player_2.name == "Computer" and self.player_2.choice == "":
            self.player_2.choice = self.play_against_computer()
    
    # - The winner is determined based on the rules and player choices - can refactor this later

    # - If player choices match then result = "None" i.e the game is a draw - this could return "None" which produces a traceback on Flask because there is "nothing" to return

        if(self.player_1.choice == self.player_2.choice):
            return "Draw"

    # - Else compare the values of player choice for the scenario of rock vs paper and define the result as paper

        elif(( self.player_1.choice == "rock" and self.player_2.choice =="paper" ) or ( self.player_1.choice == "paper" and self.player_2.choice =="rock" )):
            result = "paper"
    
    # - Else compare the values of player choice for the scenario of scissors vs paper and define the result as scissors

        elif(( self.player_1.choice == "scissors" and self.player_2.choice =="paper" ) or ( self.player_1.choice == "paper" and self.player_2.choice =="scissors" )):
            result= "scissors"

    # - Else the result must be that rock wins

        else:
            result= "rock"

    # - If the the result is the same as player_1's choice then player_1 is returned as the winner else the winner is player_2

        if result == self.player_1.choice:
            return self.player_1.name
        elif result == self.player_2.choice:
            return self.player_2.name

    # - Play against the computer - the computers choice of RPS is weighted against a random integer between 1 and 3

    def play_against_computer(self):
        
        computer_choice = random.randint( 1, 3 )
        if computer_choice == 1:
            choice = 'rock'
        elif computer_choice == 2:
            choice = 'paper'
        else:
            choice = 'scissors'
        return choice