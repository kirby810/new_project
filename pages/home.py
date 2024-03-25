import streamlit as st
import requests
import json



city = "Seoul"
apiKey = "f7344dc26488d7a393e9e63665948ccf"
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
weather = json.loads(result.text)

wind_speed = weather['wind']['speed'] #풍속
weather_status = weather['weather'][0]['description'] #현재 기상상태
temp = weather['main']['temp'] #현재 기온
temp_feel =weather['main']['feels_like'] #체감온도
temp_min =weather['main']['temp_min'] #최저온도
temp_max =weather['main']['temp_max'] #최고온도






# streamlit page
st.set_page_config(layout="centered")

st.header('새로운 프로젝트 제목입니다.', divider='rainbow')

col1, col2 = st.columns(2)
with col1:
    texts = [st.header(f"현재 기상상태: {weather_status}"),
            st.header(f"현재기온: {temp}"),
            st.header(f"풍속: {wind_speed}"),
            st.header(f"체감온도: {temp_feel}"),
            st.header(f"최저온도: {temp_min}"),
            st.header(f"최고온도: {temp_max}")]

    # 각 텍스트를 <div> 태그로 감싸고 하나의 문자열로 묶기
    styled_texts = ''.join([f'<div style="border: 2px solid white; padding: 10px; margin-bottom: 10px;">{text}</div>' for text in texts])

    # Streamlit에 표시
    st.markdown(styled_texts, unsafe_allow_html=True)
with col2:
    st.header("실시간 현황?")