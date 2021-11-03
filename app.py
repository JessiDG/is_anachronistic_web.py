#This is the file where the front-end's infrastructure is laid out

import requests
import json
from flask import Flask, request, url_for, redirect, render_template, jsonify
from word_obj import word_obj
from output_obj import output_obj
from find_anachronistic_words import Is_Anachronistic
from input_obj import input_obj

app = Flask(__name__)

years = {'1812':'unique_set_1812.txt', '1851':'unique_set_1851.txt', '1966':'unique_set_1966.txt', }

@app.route('/')
def home():
   return render_template('home.html')

#This submit function passes the text and selected year through, passes the year through to the open method,
#reads in the comparison text, builds the output object, and returns it as a json file
@app.route("/result", methods=['GET', 'POST'])
def submit():
    input = input_obj(request.form.get('text'), request.form.get('year'))
    year_file = years[input.get_date()]
    comparison_text = open(year_file, 'r', encoding='utf8')
    comparison_text_read = comparison_text.read()
    return_result = output_obj(Is_Anachronistic(input.get_text(), comparison_text_read).find_difference())
    return jsonify(return_result.serialize())

#the result function resturns the tet and the year
def result():
    return request.form.get('text') + " " + request.form.get('year')

# def game_play():
# @app.route('/game_play', methods=['GET', 'POST'])
#     load_game()
#     return render_template('game_play.html')

if __name__ == '__main__':
    app.run()