import streamlit
import pandas 
import snowflake.connector

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
my_data_row = my_cur.fetchone()
streamlit.text("fruit load list contains:")
streamlit.text(my_data_row)
