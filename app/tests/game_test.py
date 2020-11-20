# - Import the unittest module for testing

import unittest

# -  Import the player and game class files in order to implement testing of the game

from app.models.game import *
from app.models.player import *

class GameTest(unittest.TestCase):
    def setUp(self):

# - Define player_1 and player_2 objects based on the Player class which have their respective choices

        self.player_1 = Player("Player 1", "Rock")
        self.player_2 = Player("Player 2", "Scissors")

# - Define a game as having player_1 and player_2 competing

        self.game = Game(self.player_1, self.player_2)
        
# - Tests the creation of a game by creating a string based on existing player choices

    def test_a_game_is_created(self):
        game_choices = self.player_1.choice + " vs " + self.player_2.choice
        self.assertEqual("Rock vs Scissors", game_choices)

# - Tests whether the game is a draw or not by comparing the two player choices 

    def test_game_is_a_draw(self):
        self.player_2 = Player("Player 2", "Rock")
        self.assertEqual(self.player_1.choice, self.player_2.choice)