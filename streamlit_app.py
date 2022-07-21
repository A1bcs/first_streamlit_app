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
streamlit.dataframe(my_fruit_list)
