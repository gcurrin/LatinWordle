from flask import Flask, render_template
from app import colorizer
from app.word_list import WordList

# DON'T RUN THIS FILE TO RUN THE PROGRAM!!! RUN wsgi.py!!!
# DON'T RUN THIS FILE TO RUN THE PROGRAM!!! RUN wsgi.py!!!
# DON'T RUN THIS FILE TO RUN THE PROGRAM!!! RUN wsgi.py!!!

print('main.py console test')

app = Flask('Latin Wordle')
wordList = WordList()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/colorize_guess/<string:target_word>/<string:guess>')
def colorize_guess(target_word, guess):
    return colorizer.colorize_guess(target_word, guess)

@app.route('/validate_word/<string:word>')
def validate_word(word: str) -> str:
    return str(word in wordList)

@app.route('/choose_random_word')
def choose_random_word() -> str:
    return wordList.choose_random()