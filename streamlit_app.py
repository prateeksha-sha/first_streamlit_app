import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')



streamlit.text('🥘 Omega 3 and Blueberry Oatmeal')

streamlit.text('🥬 Kale,Spinach and Rocket Smoothie')

streamlit.text('🥚🐔 Hard-Boiled free-range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🥭🍍Build Your OWN Fruit Smoothie🍉🍇')
# importpandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# new section to display fruityvise api response

streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get information.")
   else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
        streamlit.dataframe(fruityvice_normalized)
