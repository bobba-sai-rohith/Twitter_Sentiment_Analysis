from flask import Flask, render_template, request,url_for,redirect
from twittersentimentconsole import senti
from profiletweets import prof
from getimagetweet import imag,profimag
from math import ceil

n="not found"
l="no image"
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sept.html')

@app.route('/test/<string:n>/')
def index(n):
    return render_template('prabhu.html' ,sentiment=n,image=l)

@app.route("/sentiment", methods=['GET', 'POST'])
def sentimentPolarity():
    if request.method=='POST':
        name=request.form['search']
        r=int(request.form['button1'])
        print(r)
        if(r==1):
            n=senti(name)
            n=ceil(n)
            l=imag(name)
            
        elif(r==2):
            n=prof(name)
            n=ceil(n)
            l=profimag(name)
            
        print(n)
        return render_template('output2.html',  sentiment = n ,image=l)
    else:
        return render_template("aps.html")

"""
def hello():
    name=input()
    n=senti(name)
    print(n)

"""

if __name__=='__main__':
    app.run(debug = True)



                           

