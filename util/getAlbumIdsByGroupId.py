import yaml
import urllib2
import urllib
import json
import re

f = open('../data.yaml')
config = yaml.load(f)
f.close()

Keywords = config["word_list"]
GroupIds = config["group_ids"]
AlbumIds = [] 

apikey = '5d469c7d31414635667c333268774d'
baseurl = 'https://api.meetup.com/2/photo_albums/?'

parse_json = lambda s: json.loads(s.decode('utf-8'))

def unique(seq):
    setified = set(seq)
    return list(setified)

Filter = re.compile( '(' + '|'.join(Keywords) + ')', re.IGNORECASE )

for groupId in GroupIds:

    data = {}
    data['key'] = apikey
    data['group_id'] = groupId
    data['page'] = "10000"

    params = urllib.urlencode(data)
    full_url = baseurl+params

    # /2/photo_albums isn't utf8 by default
    request = urllib2.Request(full_url, headers={"Accept-Charset":"utf-8"})
    
    response = urllib2.urlopen(request).read()
    results = parse_json(response) 

    for album in results["results"]:

        if 'title' in album:
            match = Filter.match(album["title"])

            if match:
                print album["title"] + ' | ' + str(album["photo_album_id"])
                AlbumIds.append( str(album["photo_album_id"]) )


print ','.join( unique(AlbumIds) )

exit();
