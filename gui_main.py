import csv
import time
from ast import Raise
from datetime import datetime
from time import strftime
import streamlit as st
import news_main as nm
import weather_main as wm

st.set_page_config(page_title="Home Dashboard", 
                    page_icon=None, 
                    layout="wide", 
                    initial_sidebar_state="auto", 
                    menu_items=None)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_streamlit_style = """
    <style>
    .css-1y0tads {padding-top: 0rem;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def digital_clock():
    time_reading = strftime('|| %A, %B %d %Y  ||   %I:%M%p  ||')
    return time_reading


clocktainer = st.empty()
datatainer = st.empty()
third_row = st.empty()

update_date = ""

while True:
    with clocktainer.container():
        clock = digital_clock()
        st.header(f"{clock}")
        time.sleep(1)
    
    with datatainer.container():
        weather = wm.get_weather()

        col1, col2, col3 = st.columns(3)
        with col1:
            if weather:
                st.header("Current Conditions")
                st.image(f"{weather.get('icon').replace('small', 'large')}")
                st.header(f"{weather.get('temperature')}°F")
                st.header(f"{weather.get('shortForecast')}")
                st.header(f"Wind: {weather.get('windSpeed')} {weather.get('windDirection')}")
        
        with col2:
            st.header("World News")
            news_package = nm.get_news()
            for news in news_package:
                st.write(f"[{news[0]}]({news[1]})")

        with col3:
            st.header("Daily David Lynch")
            
            num = 1

            if datetime.today().date() != update_date:
                with open('DL_quotes.csv', 'r') as file:
                    reader = csv.reader(file, delimiter=',')

                    for row in list(reader)[1:]:
                        if row:
                            if int(row[0]) == num:
                                st.subheader(f"{row[1]}")
                                st.subheader("- David Lynch")
                                break
            time.sleep(30)

    with third_row.container():
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.header("Column 1")
        with col2:
            st.header("Column 2")
        with col3:
            st.header("Column 3")
        with col4:
            st.header("Column 4")
        with col5:
            st.header("Column 5")
        with col6:
            st.header("Column 6")
        with col7:
            st.header("Column 7")
        
        time.sleep(30)

