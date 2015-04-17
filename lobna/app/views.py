from flask import render_template
from app import app
import os
from models import *
from js import *
from flask import Flask, jsonify, send_from_directory,request, redirect, url_for
from werkzeug import secure_filename

#create path of pictures
@app.route('/img/<path:path>')
def send_js(path):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               path, as_attachment=True)

"""@app.route('/')
@db_session
def index():
    images = Photo.select() 

    return render_template("index.html",
                           title='Home',
                           photos=images)"""
@app.route('/')
@db_session
def index():
    return render_template("home.html")


#render all pictures from database as json objects
@app.route('/photos')
@db_session
def photos():
    photos = Photo.select()
    return to_json(db, photos, include=[])
  

"""@app.route('/comments')
@db_session
def comment():
    comment = Comment.select()
    return to_json(db, comment, include=[])"""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in set([  'png', 'jpg'])

@app.route('/upload', methods=['GET', 'POST'])
@db_session
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            x = Photo(picture=filename)
            commit()
            file.save(path)
            return redirect('/')
    return render_template("upload.html")
