import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Happiness App", layout="wide")

st.header("Happiness by country")

df = pd.read_csv("happy.csv")

x_axis = st.selectbox(label="Select data to display on the X-axis", options=["GDP", "Happiness", "Generosity"])
match x_axis:
    case "GDP":
        x_axis_data = df["gdp"]
    case "Happiness":
        x_axis_data = df["happiness"]
    case "Generosity":
        x_axis_data = df["generosity"]

y_axis = st.selectbox(label="Select data to display on the Y-axis", options=["GDP", "Happiness", "Generosity"])
match y_axis:
    case "GDP":
        y_axis_data = df["gdp"]
    case "Happiness":
        y_axis_data = df["happiness"]
    case "Generosity":
        y_axis_data = df["generosity"]

st.header(f"{x_axis} and {y_axis}")

figure = px.scatter(x=x_axis_data, y=y_axis_data, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)

