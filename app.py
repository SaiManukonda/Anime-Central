from flask import Flask, request, render_template, redirect, url_for, session
from anime import *
from difflib import *

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def HomePage():
    animes = search('None')
    return render_template('home.html', animeInfo = animes, title = "ANIME CENTRAL")

@app.route('/results/')
@app.route('/results/<animeName>')
def Results(animeName = 'None'):
    if(animeName == 'None'):
        return redirect(url_for('HomePage'))
    animes = search(animeName)
    temp = "Results for " + animeName.capitalize()
    if(len(animes) == 0):
        temp = "No Results for "+ animeName.capitalize()
    return render_template('home.html', animeInfo = animes, title = temp)

@app.route('/watched/')
def watched():
    if len(session) > 0:
        return render_template('home.html', animeInfo = session, title = "YOUR WATCHED")
    else:
        return redirect(url_for('HomePage'))

@app.route('/title/<animeName>', methods = ["POST", "GET"])
def title(animeName = 'None'):
    if request.method == "POST":
        try:
            animeName = request.form['foo']
            session[animeName] = getStoredImage(animeName)
        except:
          animeName = request.form['remove']
          if(animeName in session):
            del session[animeName]
        return redirect(url_for('watched'))
    else:
        return render_template('results2.html', title = animeName, image = getStoredImage(animeName))


if __name__ == "__main__":
    app.run(debug=True)