import streamlit as st
import random

numbers = [i for i in range(0, 45)]

if 'my_num' not in st.session_state:
    st.session_state.my_num = random.choice(numbers)

i = st.session_state.my_num

st.header('Тренажер по матанализу')
f = open('questions.txt', 'r+', encoding='UTF8')
content = f.readlines()

st.write(f"{content[i]}")

def change_num():
    st.session_state.my_num = random.choice(numbers)

def print_hello():
    st.image(f'{i+1}.jpg')


st.button("Новый вопрос", on_click=change_num)
main_con = st.container()
with main_con:
    on = st.toggle('Показать ответ')

    if on:
        print_hello()
