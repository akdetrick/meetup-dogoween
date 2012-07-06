import yaml
import shelve
from random import choice
from flask import Flask
from flask import request 
from flask import render_template
from flask import jsonify

# starting with a simple app - hard code all photo ids
f = open('../urls.yaml')
data = yaml.load(f)
f.close()
PhotoUrls = data['photoUrls']

# app settings
app = Flask(__name__)
app.debug = True

# ------------------------- routes

@app.route('/')
def index():
    return render_template('index.html', photourl=choice(PhotoUrls)) 


@app.route('/_get_new_photo')
def get_new_photo():
    return jsonify(url=str(choice(PhotoUrls)))


@app.route('/_record_candy', methods=['POST'])
def record_candy():
    imgurl = request.form.get('imgurl')
    print "got"+str(imgurl)

    D = shelve.open('../storage/candy', 'n')

    if data and imgurl:
        D[str(imgurl)] += 1
        print data
        return jsonify(success="updated candy count to "+str(data))
    elif imgurl:
        D[str(imgurl)] = 1
        print data
        return jsonify(success="recorded first candy")
    else:
        print "why u no url?"


@app.route('/photo/<int:photo_id>')
def deeplink(photo_id):
    return 'photo deep link to photo ' + str(photo_id)

if __name__ == '__main__':
    app.run()

