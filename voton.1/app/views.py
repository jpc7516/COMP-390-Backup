import os,sys
from flask import render_template, flash, redirect, request
from app import app
from app import db
from slots import Post
from .forms import LoginForm
import random

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods =['GET', 'POST'])
@app.route('/index', methods =['GET', 'POST'])

def index():
    rand = random.randrange(0, Post.query.count())
    retpost = Post.query.get(24+rand)
    #retpost = Post.query.order_by('-id').first()
    question = retpost.question
    src1 = retpost.image1
    src2 = retpost.image2
    print retpost.id
    print retpost.question
    print retpost.image1
    print retpost.vote1
    print retpost.vote2
    posts = Post.query.all()
    print posts
    #retimg = Image.query.order_by('-id')
    #img1 = retimg[0].vote
    #img2 = retimg[1].vote
    #image_names = os.listdir('voton/app/static/images')
    #c = len(image_names)
    #if (len(image_names) > 2):
    #    img1 = image_names[c-1]
    #    img2 = image_names[c-2]
    #    src1 = "../static/images/"+img1
    #    src2 = "../static/images/"+img2
    #elif len(image_names) > 0:
    #    img1=image_names[0]
    #    img2=image_names[1]
    #    src1 = "../static/images/"+img1
    #    src2 = "../static/images/"+img2
    #else:
    #src1 = "../static/tie1.jpg"
    #src2 = "../static/tie2.JPG"
    vote = request.form.get('choice')
    if vote == "first":
        retpost.vote1 = int(retpost.vote1) + 1
        print 'one'
    elif vote == "second":
        retpost.vote2 = retpost.vote2 + 1
        print 'two'
    else: print 'fffff'
    db.session.commit()
    vote1 = retpost.vote1
    vote2 = retpost.vote2
    return render_template('front.html', question=question, src1=src1, src2=src2, vote1=vote1, vote2=vote2)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    return render_template('questions.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/upload", methods=['POST'])
def upload():
    question = str(request.form['question'])
    image1 = str(request.form['image1'])
    image2 = str(request.form['image2'])
    if request.method == 'POST':
        print("Question: "+ question)
        print("Image 1: "+ image1)
        print("Image 2: " + image2)
        v1 = 0
        v2 = 0
        q = Post(question, image1, image2)
        db.session.add(q)
        db.session.commit()
        x = Post.query.all()
        print x
    #target = os.path.join(APP_ROOT, 'static/images/')
    #if not os.path.isdir(target):
    #    os.mkdir(target)
    #for file in request.files.getlist("file"):
    #    print(file)
    #    filename = file.filename
    #    destination = "/".join([target,filename])
    #    print(destination)
    #    file.save(destination)
    return render_template("complete.html")

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)
    
@app.route('/voted')
def redir():
    return render_template('redirect.html')
    