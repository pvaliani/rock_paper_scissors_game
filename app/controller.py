# - This is the controller for the Rock, Paper, Scissors game to work with Flask

from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player

# - Listen on the route of choices then return a response. The choices will be variables. 

@app.route('/')
def base():

# - The get request handled by the base() function

    return render_template('base.html')
    
# - The get request which matches the players choices to return the result of the game. If the user inputs their choices in the browser as /rock/scissors for example, then the result will be returned in the browser as a string

@app.route('/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game(player_1, player_2)
    winner = game.play_game()
    return choice_1.title() + " " + choice_2.title() + " " + winner

#---------------------------------- MVP --------------------------------------------------------

@app.route('/welcome')
def welcome():

# - The get request handled by the welcome() function

    return render_template('welcome.html')


@app.route('/about')
def about():

# - The get request handled by the about() function

    return render_template('about.html')

@app.route('/play_game')
def play_game():

# - The get request handled by the play_game() function

    return render_template('play_game.html')