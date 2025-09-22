import streamlit as st
from chatterbot import ChatBot

chatbot = ChatBot('MyBot', database_uri='sqlite:///database.sqlite3')

st.title("Deep Learning ChatBot")
user_input = st.text_input("You:")

if st.button("Send"):
    if user_input.strip() != "":
        response = chatbot.get_response(user_input)
        st.write("Bot:", response)
