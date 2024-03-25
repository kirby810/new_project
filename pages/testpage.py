import streamlit as st
import requests
import json

# API 요청
city = "Seoul"
apiKey = "f7344dc26488d7a393e9e63665948ccf"
lang = 'kr'
units = 'metric'
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
weather = json.loads(result.text)

wind_speed = weather['wind']['speed']
weather_status = weather['weather'][0]['description']
temp = weather['main']['temp']
temp_feel = weather['main']['feels_like']
temp_min = weather['main']['temp_min']
temp_max = weather['main']['temp_max']

# Streamlit 페이지 설정
st.set_page_config(layout="centered")

st.header('새로운 프로젝트 제목입니다.', divider='rainbow')

col1, col2 = st.columns(2)

with col1:
    st.header('현재 날씨 정보')
    styled_text = f"""
    <div style='border: 2px solid white; padding: 15px;'>
        <p>현재 기상상태: {weather_status}</p>
        <p>현재기온: {temp}°C</p>
        <p>풍속: {wind_speed} m/s</p>
        <p>체감온도: {temp_feel}°C</p>
        <p>최저온도: {temp_min}°C</p>
        <p>최고온도: {temp_max}°C</p>
    </div>
    """
    st.markdown(styled_text, unsafe_allow_html=True)

with col2:
    st.header("실시간 현황?")
