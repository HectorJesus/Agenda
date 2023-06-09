"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PIA_Agenda import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'indexLogIn.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/SingUp')
def SingUp():
    """Renders the contact page."""
    return render_template(
        'indexSingUp.html',
        title='SingUp',
        year=datetime.now().year,
        message='Registrate aqui.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
