from pathlib import Path
import streamlit as st
import sys
import os

# Grab the filepath:
filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

# Insert the filepath into the system:
sys.path.insert(0, filepath)

# Import the ToMongo Class now:
from to_mongo import ToMongo

# Instantiate the class:
c = ToMongo()
st.header('Park Info Page')
st.write('This page will search our database for any information on a National park you input. Spelling currently must be exact.')

answer = st.text_input('Enter a National Park Name to retreive information on it:', value = 'Arcadia National Park')
st.write(list(c.park_info.find({'name': answer})))