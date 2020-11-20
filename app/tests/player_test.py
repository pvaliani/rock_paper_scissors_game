# - Import the unittest module for testing

import unittest

# -  Import the player and game class files in order to implement testing of the game

from app.models.player import *

# - Perform unit tests for the Player class

class PlayerTest(unittest.TestCase):

    def setUp(self):

# - Set up a test variable of Player called "player_1" with a name and a choice for game

        self.player_1 = Player("Pedram Valiani", "Scissors")

# - Test that the player has a name based on player_1 - point to the name attribute and compare

    def test_player_has_name(self):
        self.assertEqual(self.player_1.name, "Pedram Valiani")

# - Test that the player has a choice based on player_1 - point to the choice attribute and compare

    def test_player_has_choice(self):
        self.assertEqual(self.player_1.choice, "Scissors")