# CST 205
# Yvonne Cruz, Niel McMahan, Shawn Deppe, Albert Salas
# 12/06/2020
# Group Project - Team 28
# Website that searches through a NASA API

import requests, json
from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from PIL import Image


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'
endpoint = 'https://images-api.nasa.gov/search'
api_result = {}

class Search(FlaskForm):
    search_terms = StringField('Search Terms', validators=[DataRequired()])

def getResults(terms,api_result): 
    print("validate entered")
    payload = {
        'q': terms
    }
    try:
        r = requests.get(endpoint, params=payload)
        api_result = r.json()
    except:
        print('please try again')  

    with open('results.json', 'w') as json_file:
        json.dump(api_result, json_file)  

# homepage
@app.route('/', methods=('GET', 'POST'))
def index():
    form = Search()
    if form.validate_on_submit():
        getResults(form.search_terms.data,api_result)
        #redirect here
    return render_template('index.html', form=form)

