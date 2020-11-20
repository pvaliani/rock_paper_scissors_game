# - Import the unittest module for testing

import unittest

# -  Import the player and game class files in order to implement testing of the game

from app.models.player import *

class PlayerTest(unittest.TestCase):
    def setUp(self):
        pass