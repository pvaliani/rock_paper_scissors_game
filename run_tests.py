# - Import the unittest module for running the game tests

import unittest

# - Import the game and player test files

from app.tests.game_test import *
from app.tests.player_test import *

if __name__ == '__main__':
    unittest.main()
