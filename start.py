from flask import Flask, request, request, send_from_directory
from flask import render_template
from util.config import *


app = Flask(__name__, static_folder='')
#Swagger(app)


@app.route('/')
def root():
    return app.send_static_file('public/index.html')


@app.route('/<path:path>')
def return_libs(path):
    return send_from_directory('public/', path)


if __name__ == '__main__':
    app.run(host=ADRESS, port=PORT, debug=DEBUG)
