# Imports for image return page
import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO

# Create a filepath to the system where the main folder for the app lives:
filepath = os.path.join(Path(__file__).parents[1])

# Now I can insert the path and freely import my mongo class
sys.path.insert(0, filepath)
from to_mongo import ToMongo
# When I click on the page:
st.title("Park Image Return Page")

# We create a instance of our Mongo Class
c = ToMongo()

# Then we take an input from a user:
answer = st.text_input("Enter a Park Name:", value = 'Acadia National Park')

# Transform that input into a card name!
park_photo = list(c.park_info.find({'name':answer}))[0]['image_uris']['normal']
st.image(Image.open(BytesIO(requests.get(park_photo).content)))