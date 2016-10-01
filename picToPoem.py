#Paul's part

# print "At lest the print works!\n"
# listOfTags = ["winter", "wolf", "snow"]
# listOfColors = ["white", "black", "red"]
listOfTags = []
listOfColors = []
# for i in listOfTags:
    # print i

from clarifai.client import ClarifaiApi
import json

#The clarifai object
clarifaiApi = ClarifaiApi()  # assumes environment variables are set.

tags = clarifaiApi.tag_image_urls('https://samples.clarifai.com/metro-north.jpg')
colors = clarifaiApi.color_urls('https://samples.clarifai.com/metro-north.jpg')

# print(json.dumps(tags, indent = 2))
# print(json.dumps(colors, indent = 2))

# print tags["results"]["result"]["tag"]["classes"]
listOfTags = json.loads(json.dumps(tags["results"][0]["result"]["tag"]["classes"], indent = 2))

for i in colors["results"][0]["colors"]:
    listOfColors.append(i["w3c"]["name"])

[x.encode('ASCII') for x in listOfTags]
[x.encode('UTF8') for x in listOfColors]

listOfTags = [str(x) for x in listOfTags]
listOfColors = [str(x) for x in listOfColors] 


#Now to split the colors

import re

newListOfColors = []

for i in range(0, len(listOfColors)):
    splitted = re.sub('(?!^)([A-Z][a-z]+)', r' \1', listOfColors[i]).split()
    newListOfColors.extend(splitted)

listOfColors = newListOfColors

# print type(listOfTags)
# print type(listOfColors)


# print listOfTags
# print listOfColors

listOfTags.extend(listOfColors)

print listOfTags
#Andrei's part

import urllib2
import re

# Build URL that displays poems which include at least one tag
url = "http://poetrydb.org/lines/'"

for i in listOfTags:
        url = url + i + "|"
        
url = url[:len(url) - 2] + "'"

# Read content of poems
content = urllib2.urlopen(url).read()

# Extract 3 lines around each match
for i in listOfTags:
        match[i] = p.match(((.*\n){1}.)i(.(.*\n){1}))[0]
        
# Display matches
match
