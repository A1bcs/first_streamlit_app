import streamlit
streamlit.title('my parents new healthy dinner')
streamlit.header('breakfast menu')
streamlit.title('blueberry')
streamlit.title('spinach')
streamlit.title('boiled egg')
streamlit.header('build your own fruit smoothie')
 
 import pandas
 my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
