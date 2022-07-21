import streamlit

streamlit.title('my parents new healthy dinner')
streamlit.header('breakfast menu')
streamlit.text('blueberry')
streamlit.text('spinach')
streamlit.text('boiled egg')
streamlit.text('build your own fruit smoothie')
streamlit.header('build your own fruit smoothie')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacoda','Strawberries'])

# Display the table on the page
streamlit.dataframe(my_fruit_list)

