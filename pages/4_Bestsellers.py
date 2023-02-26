import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard - Amazon Bestsellers Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "amazon.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "bestsellers.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

# Load Titanic dataset
df = pd.read_csv(DATA_PATH)

# PieChart
st.title('Pie Chart')
grouped_data = df.groupby(['Genre']).size().reset_index(name='count')

# Create a pie chart using Plotly Express
fig_1= px.pie(grouped_data, names='Genre', values='count', title='Proportion of Books by Genre')

# Display the chart
st.plotly_chart(fig_1, use_container_width=True)

expander=st.expander("View Data")
expander.dataframe(df)

# ScatterPlot
st.title("ScatterPlot")
st.write('To display the ratings for works based on auuthor')
fig = px.scatter(df, x="Author", y="User Rating", hover_data=["Name"])

# Add chart title
fig.update_layout(title="User Rating by Author")

# Display chart
st.plotly_chart(fig)