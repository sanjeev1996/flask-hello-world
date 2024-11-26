from flask import Flask, jsonify, render_template, request
import requests, re

app = Flask(__name__)

@app.route('/')
def ticket_fields1():
    return render_template('line_converter.html')

@app.route('/api', methods=["post"])
def ticket_fields2():
    text = str(request.get_json()["text"])
    text = ' '.join(text.split('\n'))
    return text

@app.route('/character_counting')
def character_counting1():
    return render_template('character_counting.html')

@app.route('/character_counting', methods=["post"])
def character_counting2():
    text = str(request.get_json()["text"])
    text = len(text.strip())
    return str(text)

if __name__ == "__main__":
  app.run()
