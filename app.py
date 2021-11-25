from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

file = open('data.json')

data = json.load(file)

file.close()


@app.route('/')
def incrementer():
    return jsonify(data)


@app.route('/noun')
@app.route('/noun/<int:number>')
def noun(number=1):
    return jsonify(random.choices(data['nouns'], k=number))


@app.route('/pronoun')
@app.route('/pronoun/<int:number>')
def pronoun(number=1):
    return jsonify(random.choices(data['pronouns'], k=number))


@app.route('/verb')
@app.route('/verb/<int:number>')
def verb(number=1):
    return jsonify(random.choices(data['verbs'], k=number))


@app.route('/adjective')
@app.route('/adjective/<int:number>')
def adjective(number=1):
    return jsonify(random.choices(data['adjectives'], k=number))


@app.route('/adverb')
@app.route('/adverb/<int:number>')
def adverb(number=1):
    return jsonify(random.choices(data['adverbs'], k=number))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
