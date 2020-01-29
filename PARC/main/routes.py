from flask import Blueprint
from flask import render_template, url_for,flash, redirect, request, abort, send_from_directory, make_response
from PARC import bcrypt, mail
from PARC.main.utils import save_picture

from flask import render_template, url_for,flash, redirect, request, abort
from PARC import db, mail
from PARC.main.forms import  PostForm, AdminForm, NewsForm
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
from functools import wraps
from flask import request, Response


######### LOADING BDD ########
#exec(open(os.getcwd() + '/tasty/MongoConnection/Functions_Mongo.py').read())
#exec(open('MongoConnection/Functions_Mongo.py').read())

### Acces to the DB ####
#db_mongo  = Get_MongoDB()
#ColNames = db_mongo.collection_names()
#ColNames.sort()

main = Blueprint('main',__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'PARC' and password == 'PaurayRC!'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@main.route("/",  methods=['GET','POST'])
@main.route("/home",  methods=['GET','POST'])
def home():
    form = NewsForm()
    if form.validate_on_submit():
        with open('PARC/static/List_Mail.csv','a') as fd:
            fd.write(form.mail.data+"\n")
        return redirect(url_for('main.home'))
    posts = Post.query.all()
    posts = reversed(posts[-3:])
    month = {'January':'Jan','February':'Fev','March':'Mar','April':'Avr','May':'Mai','June':'Juin','July':'Juil','August':'Aout','September':'Sept','October':'Oct','November':'Nov','December':'Dec'}
    return render_template('index.html',posts=posts, month =month, form=form)

@main.route("/senior")
def senior():
    return render_template('senior.html')

@main.route("/feminine")
def feminine():
    return render_template('feminine.html')

@main.route("/jeunes")
def jeunes():
    return render_template('jeunes.html')

@main.route("/blog")
def blog():
    posts = Post.query.all()
    posts = reversed(posts[-10:])
    month = {'January':'Jan','February':'Fev','March':'Mar','April':'Avr','May':'Mai','June':'Juin','July':'Juil','August':'Aout','September':'Sept','October':'Oct','November':'Nov','December':'Dec'}
    return render_template('blog.html',posts=posts, month =month)

@main.route("/sponsors")
def sponsors():
    return render_template('sponsors.html')

@main.route("/equipements")
def equipements():
    return render_template('equipements.html')

@main.route("/medical")
def medical():
    return render_template('medical.html')


# creer un post

@main.route("/post/new",  methods=['GET','POST'])
@requires_auth
def new_post():
    posts = Post.query.all()
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        post = Post(title=form.title.data, content=form.content.data, image_file = picture_file)
        db.session.add(post)
        db.session.commit()
        flash('Post créé','success')
        Mails = pd.read_csv('PARC/static/List_Mail.csv',sep=';')
        Mails = set(list(Mails[Mails.columns[0]]))
        #Mails = ['valent1lefranc@gmail.com'] #tests
        msg = Message('PARC News' + ' : ' +form.title.data,sender='aurayrugbynews@gmail.com',recipients= Mails)
        msg.body = form.content.data
        mail.send(msg)
        return redirect(url_for('main.blog'))
    return render_template('create_post.html', title = 'Nouveau Post', posts = posts,form =form,legend = 'Nouveau Post')


# Delete post
@main.route("/post/<int:post_id>/delete", methods=['GET','POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    posts = Post.query.all()
    return redirect(url_for('main.new_post'))
