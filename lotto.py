import streamlit as st
import random
import datetime

st.title("로또 번호 생성기")

def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45) # 1~45 범위 수정
        lotto.add(number)
    return sorted(list(lotto)) # 정렬 추가

button = st.button("로또 번호 생성해주세요.")

if button:
    for i in range(1, 6):
        # f-string 위치 수정: f"..." 형태가 되어야 함
        st.subheader(f"{i}번째 추천 로또번호: {generate_lotto()}")
        
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

   