import yaml
import urllib2
import urllib
import json
import re

f = open('../data.yaml')
config = yaml.load(f)
f.close()

AlbumIds = config["album_ids"]
PhotoUrls = [] 

apikey = '5d469c7d31414635667c333268774d'
baseurl = 'https://api.meetup.com/2/photos/?'

parse_json = lambda s: json.loads(s.decode('utf-8'))

def unique(seq):
    setified = set(seq)
    return list(setified)

for albumId in AlbumIds:

    data = {}
    data['key'] = apikey
    data['photo_album_id'] = str(albumId)
    data['page'] = "200"

    params = urllib.urlencode(data)
    full_url = baseurl+params

    request = urllib2.Request(full_url, headers={"Accept-Charset":"utf-8"})
    
    response = urllib2.urlopen(request).read()
    results = parse_json(response) 

    for photo in results["results"]:
        PhotoUrls.append( str(photo["highres_link"]) )


print ','.join( unique(PhotoUrls) )

exit();
