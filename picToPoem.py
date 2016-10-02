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


#The command line arguments
import sys
import os
import glob


if len(sys.argv) == 1:
    print "PARAM: emotions: [0 - anger] [1 - disgust] [2 - fear] [3 - joy] [4 - sadness]",
    print "+ [Specify a URL or a location]"
    sys.exit()
elif len(sys.argv) == 2:
    imageURL = 'https://samples.clarifai.com/metro-north.jpg'
else:
    imageURL = sys.argv[2]



#The clarifai object
clarifaiApi = ClarifaiApi()  # assumes environment variables are set.

# tags = clarifaiApi.tag_image_urls(imageURL)
# colors = clarifaiApi.color_urls(imageURL)

tags = {}
color = {}

if imageURL.startswith('http') or imageURL.startswith('https'):
    tags = clarifaiApi.tag_image_urls(imageURL)
    colors = clarifaiApi.color_urls(imageURL)
elif os.path.isfile(imageURL):
    with open(imageURL,'rb') as image_file:
        tags = clarifaiApi.tag_images(open(imageURL, 'rb'))
        colors = clarifaiApi.color(open(imageURL, 'rb'))



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

curatedListOfTags = []

for element in listOfTags:
    if element.isalpha():
        curatedListOfTags.append(element)

listOfTags = curatedListOfTags
# print listOfTags

#Andrei's part

from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
        username='f0862e98-79e0-4643-afb0-4ce2eea971f4',
        password='ciiTHIb61CRP',
        version='2016-05-19')


import urllib2
import re
import os
import random

# Shuffle frets
random.shuffle(listOfTags)

# Cut tags
listOfTags_short = listOfTags[0:14]
 
# print listOfTags_short

# Build URL that displays poems which include at least one tag
url = "http://poetrydb.org/author,author,author,lines/Shakespeare;Milton;Byron;'"

for i in listOfTags_short:
    url = url + i + "|"

url = url[:len(url) - 1] + "'"


# url = "file:///home/paul/Documents/poetry.html" # DEVELOPMENT ONLY!!
# Read content of poems
content = urllib2.urlopen(url).read()

# Split text
content_list = content.split("\n")

#The data object that is going to hold all the poems
poems = []

for count in range(0, 10):

    matches = ""

# Shuffle frets
    random.shuffle(listOfTags_short)

# Shuffle it
    random.shuffle(content_list)

# Extract a line around each match
    for i in listOfTags_short:
        for line in content_list:
            if i in line and "title" not in line and "author" not in line:
                lineToAdd = line.strip()
                lineToAdd = lineToAdd[1:-2]
                lineToAdd = lineToAdd.strip()
                matches = matches + lineToAdd + "\n"
                break


    # print matches
    poemData = json.loads(json.dumps(tone_analyzer.tone(text=matches), indent=2))
    poems.append((matches, poemData))


# print poems[1][0]

# print poems

emotion = int(sys.argv[1])
print 
#Manual sorting, 3 is Joy
for i in range(0, len(poems)):
    for j in range(i, len(poems)):
        if poems[i]\
                [1]\
                ["document_tone"]\
                ["tone_categories"]\
                [0]\
                ["tones"]\
                [emotion]\
                ["score"]\
            < poems[j][1]["document_tone"]["tone_categories"][0]["tones"][emotion]["score"]:
                temp = poems[i]
                poems[i] = poems[j]
                poems[j] = temp

print poems[0][0]
# print poems

