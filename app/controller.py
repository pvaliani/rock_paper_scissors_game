# - This is the controller for the Rock, Paper, Scissors game to work with Flask

from flask import render_template, request, redirect, url_for
from app import app
from app.models.game import Game
from app.models.player import Player

# - Listen on the route of choices then return a response. The choices will be variables. 

@app.route('/')
def base():

# - The get request handled by the base() function - If the home page is clicked then show the base page

    return render_template('base.html')
    
# - The get request which matches the players choices to return the result of the game. If the user inputs their choices in the browser as /rock/scissors for example, then the result will be returned in the browser as a string

# - **locals() - passes all local variables within a function and pass it in as a keyword argument. Can then call by exactly what its called in the method

@app.route('/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game(player_1, player_2)
    winner = game.play_game()
    return render_template('result.html', winner = winner, choice_1 = choice_1, choice_2 = choice_2)

# - The result page is created even if the game hasn't begun so that the user is aware they need to start a new game. This method returns a string to replace winner to let the player know the game has not started. 
@app.route('/result')
def result():

    return render_template('result.html', winner = ".....undecided as you need to play the game.")


#---------------------------------- MVP --------------------------------------------------------

@app.route('/welcome')
def welcome():

# - The get request handled by the welcome() function

    return render_template('welcome.html')


@app.route('/about')
def about():

# - The get request handled by the about() function

    return render_template('about.html')

@app.route('/rules')
def play_game():

# - The get request handled by the play_game() function

    return render_template('rules.html')

# - Create a play route to host the input form for the user to input their choice against the Computer
@app.route('/play')
def play():
    return render_template('play.html', title='Rock, Paper, Scissors')

# - Create a post request with the argument of 'select-choice' which takes the selected choice from the input form and processes it to the results. In effect the form "action" is linked to the post request path of "select-choice" to retrieve the data. Then the request argument for player one is the 2nd parameter request.form

# - Again, could use **locals() on line 74 to pass all variables

@app.route('/select-choice', methods=['POST'])
def select_choice():
    player_1 = Player( "Player 1", request.form['choice'] )
    player_2 = Player( "Computer", "")
    game = Game( player_1, player_2 )
    winner = game.play_game()
    return (render_template("result.html", winner=winner, choice_1=player_1.choice, choice_2=player_2.choice))