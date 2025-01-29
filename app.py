import streamlit as st

st.title("Sawubona Mhlaba! 🌍")

st.caption("'possibility is not the same as conceivability' - possible worlds, an introduction to logic and its philosophy")

# Collect basic information
name = "Sakhile Marcus Zungu, DSc"
field = "Astronomy/Astrophysics"
institution = "University of KwaZulu-Natal, Westville"

# Create 2 columns
clmn1, clmn2 = st.columns(2,  vertical_alignment="bottom")


with clmn1:
    # Display basic profile information
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

from PIL import Image
with clmn2:
    image = Image.open("gardens.jpg")
    rotated_image = image.rotate(-90)
    st.image(rotated_image)

st.divider()

st.write("Hello from Streamlit :) You can call me Shwakhile with a 'hwi' 🌌 Here's a quick number slider.")

st.divider()

st.header("Number selection:")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}. That was great! Now, let's get more visual!!!")

st.divider()

st.header("Visualizations:")

import pandas as pd
import plotly.express as px

st.subheader("Using Sample Data")

data = pd.DataFrame({"units": [1, 2, 3], "tens": [10, 20, 30]})

# Display the data on the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="units", y="tens", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)

st.divider()