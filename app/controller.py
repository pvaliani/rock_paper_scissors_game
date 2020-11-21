# - This is the controller for the Rock, Paper, Scissors game to work with Flask

from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player


# - Listen on the route of choices then return a response. The choices will be variables. 

@app.route('/')
def base():
    return render_template('base.html', title='Rock Paper Scissors Game')

@app.route('/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game(player_1, player_2)
    winner = game.play_game()
    return choice_1.title() + " " + choice_2.title() + " " + winner




# @app.route(‘/<hand1>/<hand2>’)
# Def play_game(hand_1,hand_2):

# Player_1 = PLayer(“Player 1”, hand_1)
# player_2 = Player(“Player 2”, hand_2)

# Current_game = Game(player_1, player_2)
# Winner = current_game.get_winner() - we want an if statement in get_winner  i.e if player _1.hand_1 == rock and player_2.hand_2 == rock then its a draw