import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Titanic1.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)

# Bar Chart - Survived Passangers
df['survived?'] = df['survived'].map({0: 'Not survived', 1: 'survived'})
survival_count = df.groupby('survived?').size().reset_index(name='Count')
fig_1 = px.bar(survival_count, x='survived?', y='Count',labels={'survived?': 'survived?', 'Count': 'Count'}, color='survived?')

st.header("Bar Chart and Data")

# TABS for Chart and Data 
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

tab1.subheader("Bar Chart showing the number of passangers that survived and those that did not")
tab1.plotly_chart(fig_1, use_container_width=True)

tab2.subheader("Data")
tab2.dataframe(df)

# Columns for the other Histogram and Scatter chart
col1, col2 = st.columns(2)


# Histogram - Age distribution of passangers
fig_2 = px.histogram(df, x='age')
col1.subheader("Histogram")
col1.plotly_chart(fig_2, use_container_width=True)
expander=col1.expander("Description")
expander.write('The above Histogram shows the age distribution of the passangers')

# Scatter plot - Relationship between fare paid and the age of the passengers.
fig_3 = px.scatter(df, x='age', y='fare', color='survived')
col2.subheader("Scatterplot")
col2.plotly_chart(fig_3, use_container_width=True)
expander=col2.expander("Description")
expander.write('The above scatterplot shows the relationship between the fair paid and the age of the passangers')