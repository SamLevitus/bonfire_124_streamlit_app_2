import streamlit as st
from pathlib import Path
import sys
import os
import pandas as pd

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0,filepath)

from to_mongo import ToMongo

c=ToMongo()
cursor=c.park_info.find()

# list into a dataframe
df =  pd.DataFrame(list(cursor))

# Creating a unique list of activities to select from
a_list = []
for i in range(len(df['activities'])):
    for act in df['activities'][i]:
        a_list.append(act)
a_list = list(set(a_list))

selection = st.selectbox('Type out the activity you want to see which parks have:', options=a_list)
if selection:
    p_list = []
    for i in range(len(df['activities'])):
        for act in df['activities'][i]:
            if act == selection:
                p_list.append(df['full_name'][i])
    p_list = list(set(p_list))
    st.write(pd.DataFrame({"Park Names": p_list}))