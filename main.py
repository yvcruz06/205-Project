# CST 205
# Yvonne Cruz, Niel McMahan, Shawn Deppe, Albert Salas
# 12/06/2020
# Group Project - Team 28
# Website that searches through a NASA API

from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from PIL import Image


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

class Search(FlaskForm):
    search_terms = StringField('Search Terms', validators=[DataRequired()])
    

# homepage
@app.route('/', methods=('GET', 'POST'))
def index():
    form = Search()
    return render_template('index.html', form=form)

