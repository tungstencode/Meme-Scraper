import urllib2
import urllib
import json

def grabimgurimglink(imgid):
	print json.loads(urllib2.urlopen('http://api.imgur.com/2/image/'+imgid+'.json').read())['image']['links']['original']

#define some variables
someurl = 'http://www.reddit.com/r/tinytits.json?limit=100'
directlinks = []
otherlinks  = []

# download the json string
#older requester
#json_string = urllib2.urlopen(someurl).read()
json_string = urllib2.urlopen(urllib2.Request(someurl, None, { 'User-Agent' : 'dl-script' })).read()

# de-serialize the string so that we can work with it
the_data = json.loads(json_string)

#narrow the stuff
somedata = the_data['data']['children']

# print the name of each trend
for x in somedata:
	somevalue = x['data']['url']
	if 'i.imgur.com' in somevalue:
		directlinks.append(somevalue)
	else:
		otherlinks.append(somevalue)

urllib.urlretrieve(directlinks[0], "00000001.jpg")

print '-------------direct links-------------'
print directlinks
print '-------------other links-------------'
print otherlinks



