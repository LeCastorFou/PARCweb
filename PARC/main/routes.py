from flask import Blueprint
from flask import render_template, url_for,flash, redirect, request, abort, send_from_directory, make_response
from PARC import bcrypt, mail
from PARC.main.utils import save_picture

from flask import render_template, url_for,flash, redirect, request, abort
from PARC import db, mail
from PARC.main.forms import  PostForm, AdminForm
from PARC.models import Post

from werkzeug import secure_filename
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
import pandas as pd
import secrets
import os
from datetime import timedelta
import math
from PIL import Image
import plotly
import json
from flask import jsonify
import datetime
######### LOADING BDD ########
#exec(open(os.getcwd() + '/tasty/MongoConnection/Functions_Mongo.py').read())
#exec(open('MongoConnection/Functions_Mongo.py').read())

### Acces to the DB ####
#db_mongo  = Get_MongoDB()
#ColNames = db_mongo.collection_names()
#ColNames.sort()

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('index.html')

@main.route("/senior")
def senior():
    return render_template('senior.html')

@main.route("/feminine")
def feminine():
    return render_template('feminine.html')

@main.route("/jeunes")
def cours():
    return render_template('jeunes.html')

@main.route("/blog")
def blog():
    return render_template('blog.html')

@main.route("/sponsors")
def sponsors():
    return render_template('sponsors.html')


# creer un post
@main.route("/post/new",  methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        post = Post(title=form.title.data, content=form.content.data, Image = picture_file)
        db.session.add(post)
        db.session.commit()
        flash('Post créé','success')
        return redirect(url_for('main.blog'))
    return render_template('create_post.html', title = 'Nouveau Post', form =form,legend = 'Nouveau Post')
