# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:43:02 2023

@author: rathk
"""

import streamlit as st
import pandas as pd

data = pd.read_csv(r'C:/Users/rathk/OneDrive/Desktop/test_sample/skills.csv')

# Set the title and a brief description for your app
st.title("Skill Set Finder")

st.write(data)

st.write("Select a skill and expertise level to filter individuals:")

# Create a multi-select widget for skill selection
selected_skills = st.multiselect("Select Skills", data['Skill'].unique())

# Create a selection widget for expertise level
selected_level = st.selectbox("Select Expertise Level", data['Expertise'].unique())

# Filter the DataFrame based on user selections
filtered_data = data[(data['Skill'].isin(selected_skills)) & (data['Expertise'] == selected_level)]

# Display the filtered DataFrame
st.write("Filtered Data:")
st.write(filtered_data)