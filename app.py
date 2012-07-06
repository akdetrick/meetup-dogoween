import os
import yaml
import shelve
from random import choice
from flask import Flask
from flask import request 
from flask import render_template
from flask import jsonify

# starting with a simple app - hard code all photo ids
f = open('urls.yaml')
data = yaml.load(f)
f.close()
PhotoUrls = data['photoUrls']

# app settings
app = Flask(__name__)
app.debug = True

# ------------------------- routes

@app.route('/')
def index():
    D = shelve.open('storage/candy', writeback=True, flag='c')
    imgurl = choice(PhotoUrls)
    idx = PhotoUrls.index(imgurl)

    try:
        temp = D[str(imgurl)]
    except KeyError: 
        temp = None
        print "you tried to get a non-existent key"

    if temp:
        return render_template('index.html', photourl=str(imgurl), candycount=temp, photoindex=idx) 
    else:
        return render_template('index.html', photourl=str(imgurl), candycount=0, photoindex=idx) 


@app.route('/_get_new_photo')
def get_new_photo():
    D = shelve.open('storage/candy', writeback=True, flag='c')
    imgurl = choice(PhotoUrls)
    idx = PhotoUrls.index(imgurl)

    try:
        temp = D[str(imgurl)]
    except KeyError: 
        temp = None
        print "you tried to get a non-existent key"

    D.close()
    
    if temp:
        return jsonify(url=str(imgurl), candycount=temp, photoindex=idx)
    else:
        return jsonify(url=str(imgurl), candycount=0, photoindex=idx)


@app.route('/_record_candy', methods=['POST'])
def record_candy():
    imgurl = request.form.get('imgurl')

    D = shelve.open('storage/candy', writeback=True, flag='c')

    try:
        temp = D[str(imgurl)]
    except KeyError: 
        temp = None
        print "you tried to get a non-existent key"

    if temp is not None:
        temp += 1
        D[str(imgurl)] = temp
        print D[str(imgurl)]
        return jsonify(candycount=temp)
    else:
        D[str(imgurl)] = 1
        print D[str(imgurl)]
        return jsonify(candycount=1)
        
    D.close()


@app.route('/photo/<int:photo_idx>')
def deeplink(photo_idx):
    D = shelve.open('storage/candy', writeback=True, flag='c')
    imgurl = PhotoUrls[photo_idx]

    try:
        temp = D[str(imgurl)]
    except KeyError: 
        temp = None
        print "you tried to get a non-existent key"

    if temp:
        return render_template('index.html', photourl=str(imgurl), candycount=temp) 
    else:
        return render_template('index.html', photourl=str(imgurl), candycount=0) 

if __name__ == '__main__':
    try:
        portvar = os.environ['PORT']
    except KeyError:
        portvar = None
        print "not on heroku"

    if portvar:
        app.run(host='0.0.0.0',port=int(os.environ['PORT']))
    else:
        app.run(host='0.0.0.0',port=5000)

