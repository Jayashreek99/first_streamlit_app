import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('🥣 My parents new healthy Diner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑 Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞 Hard-Boiled Free-Range Egg')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
 
#chapter 9a
#streamlit.header("Fruityvice Fruit Advice!")
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#streamlit.header("Fruityvice Fruit Advice!")
#try:
  #fruit_choice = streamlit.text_input('What fruit would you like information about?')
  #if not fruit_choice:
    #streamlit.error("Please select a fruit to get information")
  #else:
   #back_from_function= get_fruityvice_data(fruit_choice)
   #streamlit.dataframe(back_from_function)
    
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    #streamlit.dataframe(fruityvice_normalised)
  
#except URLError as e:
 #streamlit.error()
    
   #back_from_function= get_fruityvice_data(fruit_choice)
   #streamlit.dataframe(back_from_function)


#fruit_choice = streamlit.text_input('What fruit would you like information about?')
#streamlit.write('The user entered ', fruit_choice)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#streamlit.stop()

#import snowflake.connector
streamlit.header("View Our Fruit List - Add Your Favorites!")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows =get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  #streamlit.stop() 
  
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)
def insert_row_snowflake():
  fruits=['jackfruit','papaya', 'guava', 'kiwi']
  with my_cnx.cursor() as my_cur:
    for fruit in fruits:
       my_cur.execute(f"insert into fruit_load_list values('{fruit}')")
    return "Thanks for adding "
  
#add_my_fruit=streamlit.text_input('What fruit would you like to add?')  
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake()
  streamlit.text(back_from_function)
  
 #if streamlit.button('Add a Fruit to the List'):
    #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    #back_from_function = insert_row_snowflake(add_my_fruit)
   #streamlit.text(back_from_function)
   # my_data_rows= get_fruit_load_list()
   # streamlit.dataframe(my_data_rows)
