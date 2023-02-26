import streamlit as st
import pandas as pd
import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard - Restaurant Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Tips.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

img = image.imread(IMAGE_PATH)
st.image(img,width=350)

# Load Titanic dataset
df = pd.read_csv(DATA_PATH)

st.header("Bar Chart and Data")

# TABS for Chart and Data 
tab1, tab2 = st.tabs(["📈 Plot", "🗃 Data"])


# Scatter Plot -Relationship between total bill and tip
fig_1 = px.scatter(df, x='total_bill', y='tip', color='sex',hover_data=['smoker', 'day', 'time', 'size'])
tab1.subheader("ScatterPlot")
tab1.plotly_chart(fig_1, use_container_width=True)

tab2.subheader("Data")
tab2.dataframe(df)

expand=st.expander("Description")
expand.write("Scatter plot to show the relationship between total bill and tip")



# Pie Chart - Smokers distribution by Gender
st.title('Pie Chart')
grouped_data = df.groupby(['sex', 'smoker']).size().reset_index(name='count')

# Create a pie chart using Plotly Express
fig = px.pie(grouped_data, names='sex', values='count',color='sex', title='Proportion of Smokers by Gender')

# Display the chart
st.plotly_chart(fig, use_container_width=True)

