from flask import Flask, request, render_template, redirect, url_for
from anime import *
from difflib import *

app = Flask(__name__)

@app.route('/')
def HomePage():
    animes = search('None')
    return render_template('home.html', animeInfo = animes, title = "Anime and Manga Central")

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

if __name__ == "__main__":
    app.run(debug=True)