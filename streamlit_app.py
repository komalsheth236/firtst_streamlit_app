import streamlit
import pandas 

streamlit.title(" My Parents New Healthy Dinner ")

streamlit.header("Breakfast Menu")
streamlit.text("Oatmeal")
streamlit.text("SMoothie")
streamlit.text("Egg")

streamlit.title(" 🍌🥭 Bulid Own SMoothies 🥝🍇 ")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
