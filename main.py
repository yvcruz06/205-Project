# CST 205
# Yvonne Cruz, Niel McMahan, Shawn Deppe, Albert Salas
# 12/06/2020
# Group Project - Team 28
# Website that searches through a NASA API
# https://github.com/yvcruz06/205-Project

import requests, json
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from PIL import Image
from io import BytesIO
from image_filter import FilteredImage
from image_resizer import resize_image
import numpy as np
import cv2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
bootstrap = Bootstrap(app)

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'superhero'

my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'
endpoint = 'https://images-api.nasa.gov/search'
api_result = {}

class Search(FlaskForm):
    search_terms = StringField('Search Terms', validators=[DataRequired()])

def getResults(terms): 
    global api_result
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
        getResults(form.search_terms.data)
        #redirect here
        return render_template("results.html", results=api_result["collection"]["items"])
    return render_template('index.html', form=form)

@app.route("/image/<string:nasa_id>", methods=('GET', 'POST'))
def image(nasa_id):
    if request.method == "GET":
        # check to see if the id provided in the URL is a valid one
        for result in api_result["collection"]["items"]:
            if result["data"][0]["nasa_id"] == nasa_id:
                # grab URL for image and convert to PIL image
                url = requests.get(result["links"][0]["href"])
                image = Image.open(BytesIO(url.content))
                image.save("static/image.png")
                return render_template("image.html", image=result)

        return redirect("/")
    else:
        # here we check what options the user selected
        if "submit" in request.form:
            # Modified ifs so that it can no longer look at empty data
            if request.form['filters']!="none":
                #very clumsy, but it does properly map images
                if request.form['filters']=="colormap":
                    colormap = int(request.form['colormap'])
                    mapped_image = cv2.imread("static/image.png", cv2.IMREAD_GRAYSCALE)
                    mapped_image = cv2.applyColorMap(mapped_image, colormap)
                    cv2.imwrite("static/image.png", mapped_image)
                else:    
                    filtered_image = FilteredImage(request.form['filters'])
            if request.form['size']!="none":
                resized_image = resize_image(request.form['size'])
        return redirect("/modifiedImage")

# this route renders a page with the image and the modifcations a user chose
@app.route("/modifiedImage")
def modifiedImage():
    return render_template("modified_image.html")
