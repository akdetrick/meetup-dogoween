import urllib2
import urllib
import json

TOPIC_LIST = [
    'dachshund',
    'pug', 
    'dogs', 
    'beagles', 
    'beagles', 
    'chihuahua', 
    'itgreyhound', 
    'greyhound', 
    'greyhound-italiano', 
    'whippet', 
    'toydog', 
    'dog-lovers', 
    'activedogs', 
    'dog-play-groups', 
    'smallbreeddogs'
]
GroupIds = []

apikey = 'API_KEY_HERE' # my api key has been reset if you're curious enough to check revision history
baseurl = 'https://api.meetup.com/2/groups/?'

parse_json = lambda s: json.loads(s.decode('utf-8'))

def unique(seq):
    setified = set(seq)
    return list(setified)

for topic in TOPIC_LIST:
    print "fetching group ids for " + topic
    data = {}
    data['key'] = apikey
    data['topic'] = topic
    data['page'] = "10000"
    params = urllib.urlencode(data)
    
    response = urllib2.urlopen(baseurl + params).read()
    results = parse_json(response) 

    for group in results["results"]:
        if str(group['visibility']) == "public":
            print "+ " + group["name"]
            GroupIds.append( str(group["id"]) )
        else:
            print "PRIVATE: " + group["name"]

print "GroupIds = ["
print ','.join( unique(GroupIds))
print "]"

exit();
