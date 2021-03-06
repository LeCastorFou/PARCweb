import os
import pandas as pd
import numpy as np
import secrets
import os
from PIL import Image
from wtforms.fields.html5 import DateField
import datetime
from datetime import timedelta
from flask import current_app, url_for
from flask_mail import Message

def save_picture(form_picture):
    # donne un nom random a l'image pour eviter les noms similaires
    random_hex = secrets.token_hex(8)
    # recupere l'extention du fichier importe par l'user
    # le _ sert a ignorer la variable (on ne s'en servira pas)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    # avoir le path general ou sauver l'image
    picture_path = os.path.join(current_app.root_path, 'static/post_pics', picture_filename)

    i = Image.open(form_picture)

    i.save(picture_path)
    return picture_filename
