import streamlit as st
import random
from PIL import Image

numbers = [i for i in range(0, 44)]

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
    img = Image.open(f'{i+1}.png')
    st.image(img)


st.button("Новый вопрос", on_click=change_num)
main_con = st.container()
with main_con:
    on = st.toggle('Показать ответ')

    if on:
        print_hello()