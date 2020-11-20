# - This is the controller for the Rock, Paper, Scissors game to work with Flask

from flask import render_template
from app import app
from app.models.game import *

# - Listen on the route of choices then return a response. The choices will be variables. 

@app.route('/choice_1/choice_2')
def base():
    return render_template('base.html', title='Home', tasks=tasks)