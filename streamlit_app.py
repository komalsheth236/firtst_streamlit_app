import streamlit
import pandas 
import snowflake.connector
import requests

streamlit.title(" My Parents New Healthy Dinner ")

streamlit.header("Breakfast Menu")
streamlit.text("Oatmeal")
streamlit.text("SMoothie")
streamlit.text("Egg")

streamlit.title(" 🍌🥭 Bulid Own SMoothies 🥝🍇 ")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Apple'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("fruit load list contains:")
streamlit.dataframe(my_data_rows)


# add from fruity vice
streamlite.header("fruity Vice")
try:
  fruit_choice = streamlit.text_input ("what fruit to get info about?")
  fruit_rep = requests.get("https://www.fruityvice.com/api/fruit/"+ fruit_choice)
  json_body = pandas.json_normalize(fruit_rep.json())
  strealite.dataframe(json_body)
  
  
  
  
  
  
  
