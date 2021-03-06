# Poem from Your Picture

Poem from Your Picture is an innovative app that does exactly as it says: you feed it a picture, it composes a poem inspired by it. The app uses Clarifai API to identify relevant tags for the picture you've just fed it and PoetryDB API to extract lines out of famous poems that contain those tags, then recombines them to render 16 unique poems tailored to your image. Then, IBM Watson API kicks in and selects the poem with the most emotional value, that, in the end, gets presented to you, the user. 

Built in Python, it can be utilised in the command line by feeding it a link/address of a picture (URL or folder location) and selecting from a range of emotions that you want to stand out in your poem (anger, disgust, fear, joy, sadness). It replies in the command line with your finished poem.
