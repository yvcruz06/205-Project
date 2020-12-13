# CST 205
# Yvonne Cruz, Niel McMahan, Shawn Deppe, Albert Salas
# 12/06/2020
# Group Project - Team 28
# Website that searches through a NASA API

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


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
bootstrap = Bootstrap(app)

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
        for result in api_result["collection"]["items"]:
            if result["data"][0]["nasa_id"] == nasa_id:
                url = requests.get(result["links"][0]["href"])
                image = Image.open(BytesIO(url.content))
                image.save("static/image.png")
                return render_template("image.html", image=result)

        return redirect("/")
    else:
        if "submit" in request.form:
            if request.form["filters"]:
                filtered_image = FilteredImage(request.form["filters"])
            if request.form["size"]:
                resized_image = resize_image(request.form["size"])
        return redirect("/modifiedImage")

@app.route("/modifiedImage")
def modifiedImage():
    return render_template("modified_image.html")
