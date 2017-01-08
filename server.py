# -*- coding: utf-8 -*-

from flask import Flask, g
from flask_helpers import crossdomain, api_data, api_error
from lib import process

PORT = 8010
app = Flask(__name__, static_url_path='')

@app.route('/ping')
@crossdomain(origin='*')
def ping():
    return 'pong'

@app.route('/')
@crossdomain(origin='*')
def index():
    return app.send_static_file('index.html')

@app.route('/api/v0/query/<query>', methods=['GET'])
@crossdomain(origin='*')
def get_tracks_from_query(query):
    data = process(query)
    if not data: return api_error('Oh no :( No results found for query {} ...'.format(query))
    return api_data(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
