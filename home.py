#importing library flask for implememting flask ap;lication
from flask import Flask, render_template, request,url_for,redirect
#importing all functions from other files 
from SearchTagSentiment import senti
from profileTweeetSentiment import prof
from GetImage import imag,profimag
#importing ceil function from math library
from math import ceil

#initilising the sentiment to not found and image to not found to prevent errors
n="not found"
l="no image"
#flask application 
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


if __name__=='__main__':
    app.run(debug = True)



                           

