# - Import the unittest module for testing

import unittest

# -  Import the player and game class files in order to implement testing of the game

from app.models.game import *
from app.models.player import *

class GameTest(unittest.TestCase):
    def setUp(self):

# - Define player_1 and player_2 objects based on the Player class which have their respective choices

        self.player_1 = Player("Player 1", "Rock")
        self.player_2 = Player("Player 2", "Rock")

# - Define a game as having player_1 and player_2 competing

        self.game = Game(self.player_1, self.player_2)
        
# - Tests the creation of a game by creating a string based on existing player choices

    def test_a_game_is_created(self):
        game_choices = self.player_1.choice + " vs " + self.player_2.choice
        self.assertEqual("Rock vs Rock", game_choices)

# - Tests whether the game is a draw or not by comparing the two player choices - could refactor this with a function 

    def test_game_is_a_draw(self):
        self.assertEqual(self.player_1.choice, self.player_2.choice)

# - Tests whether paper has beaten rock in the game - define two players with paper and rock choices, respectively and create a new game instance with the new values of player. Test that the values for paper and rock match each respective player choice. Test that Player 1 is the winner based on paper beating rock in the game.

    def test_paper_beats_rock(self):
        self.player_1 = Player("player 1", "paper")
        self.player_2 = Player("player 2", "rock")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("paper", self.player_1.choice)
        self.assertEqual("rock", self.player_2.choice)
        self.assertEqual("player 1", self.game.play_game())

# - Tests as above but with rock beating scissors instead. The final test checks the value of "Player 1" against the result of self.game.play_game() which inacts the play_game() method on the current game. No argument is required in play_game() as the function will already implicitly receive the values of both players in order to return the winner

    def test_rock_beats_scissors(self):
        self.player_1 = Player("player 1", "rock")
        self.player_2 = Player("player 2", "scissors")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("rock", self.player_1.choice)
        self.assertEqual("scissors", self.player_2.choice)
        self.assertEqual("player 1", self.game.play_game())

# - Tests as above but with scissors beating paper

    def test_scissors_beats_paper(self):
        self.player_1 = Player("player 1", "scissors")
        self.player_2 = Player("player 2", "paper")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("scissors", self.player_1.choice)
        self.assertEqual("paper", self.player_2.choice)
        self.assertEqual("player 1", self.game.play_game())

        