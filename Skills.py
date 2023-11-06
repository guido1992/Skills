# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:43:02 2023

@author: rathk
"""

### ----- SKILL SELECTION APPLICATION -----

# Import Libraries
import streamlit as st
import pandas as pd

# Read data file
data = pd.read_csv(r'C:/Users/rathk/OneDrive/Desktop/test_sample/skills.csv')

### ----- SET TITLE & DESCRIPTION FOR APPLICATION -----
st.title("Skill Set Finder")

# Add an image to the top left of the application
st.write("""
         ***Add image to app***
         """)
#st.image("C:/Users/rathk/OneDrive/Desktop/test_sample/CSLogo.jpeg", use_column_width=False)

st.write("""
         We have a new client and want to find resources in our employee pool for this new project. Below is a sample dataset to
         illustrate the workings of this application.
         """)

st.write("""
         Using this dataset we want to find employees with specific skills and levels of expertise that are available to work on this
         project.
         """)

# Display dataframe
st.write(data)

#### ----- FORMAT APPLICATION -----

# Set Filter
st.subheader("***Filter selection***")

# Description
st.write("Select a skill and expertise level to find individuals for specific projects.")

# Create three columns for Skill 1, Skill 2 and Skill 3 selections
col1, col2, col3 = st.columns(3)

# Within the first column, create multi-select widgets for Skill 1
with col1:
    selected_skill_1 = st.multiselect("**Select Skill 1**", data['Skill'].unique())
    selected_level_1 = st.multiselect("**Select Expertise Level for Skill 1**", data['Expertise'].unique())

# Within the second column, create multi-select widgets for Skill 2
with col2:
    selected_skill_2 = st.multiselect("**Select Skill 2**", data['Skill'].unique())
    selected_level_2 = st.multiselect("**Select Expertise Level for Skill 2**", data['Expertise'].unique())

# Within the third column, create multi-select widgets for Skill 3
with col3:
    selected_skill_3 = st.multiselect("**Select Skill 3**", data['Skill'].unique())
    selected_level_3 = st.multiselect("**Select Expertise Level for Skill 3**", data['Expertise'].unique())

# Filter the DataFrame based on user selections
filtered_data = data[
    (data['Skill'].isin(selected_skill_1) & data['Expertise'].isin(selected_level_1)) |
    (data['Skill'].isin(selected_skill_2) & data['Expertise'].isin(selected_level_2)) |
    (data['Skill'].isin(selected_skill_3) & data['Expertise'].isin(selected_level_3))
]

### ----- DISPLAY THE INDIVIDUALS WHO FIT THE SKILL SELECTION -----

# Outcome
st.subheader("***Outcome view***")

# Add a statement about the selected individuals for the project
if not filtered_data.empty:
    st.write("You have selected the following individuals for your project:")
    
    for index, row in filtered_data.iterrows():
        st.write(f"- **{row['Person']}** has expertise in {row['Skill']} at the {row['Expertise']} level.")
else:
    st.write("No individuals found with the selected skillsets for your project.")
