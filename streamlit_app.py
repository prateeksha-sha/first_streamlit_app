import streamlit

streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')



streamlit.text('🥘 Omega 3 and Blueberry Oatmeal')

streamlit.text('🥬 Kale,Spinach and Rocket Smoothie')

streamlit.text('🥚🐔 Hard-Boiled free-range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🥭🍍Build Your OWN Fruit Smoothie🍉🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
