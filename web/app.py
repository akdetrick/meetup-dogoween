import yaml
from random import choice
from flask import Flask
from flask import request 
from flask import render_template
from flask import jsonify

# starting with a simple app - hard code all photo ids
f = open('../data.yaml')
data = yaml.load(f)
f.close()

PhotoUrls = data['album_ids']

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return render_template('index.html', photourl=choice(PhotoUrls)) 

@app.route('/_get_new_photo')
def get_new_photo():
    return jsonify(id=str(choice(PhotoUrls)))

@app.route('/photo/<int:photo_id>')
def deeplink(photo_id):
    return 'photo deep link to photo ' + str(photo_id)

if __name__ == '__main__':
    app.run()

