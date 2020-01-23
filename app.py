#!usr/bin/env python3

from flask import Flask, render_template
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)
logger_address = '192.168.3.30'
app.stati_folder = "static"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logger/<request>')
def logger(request):
    ### forward requests directly to the logger 
    requestURL = logger_address + '/?'+request
    print(requestURL)
    r = requests.get(requestURL)
    ### is r.text the right way to access to logger data? 
#    print(r.text)
    ### return the returned json to the client
    return (r.text)


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=3134)