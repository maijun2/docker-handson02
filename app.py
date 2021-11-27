import os, flask
from flask import Flask
from flask import render_template

PORT = int(os.environ['PORT'])
app = flask.Flask('app server')

@app.route('/')
def index():
    return render_template('index.html', title='動作確認')
    
app.run(debug=True, host='0.0.0.0',port=PORT)