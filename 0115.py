import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime as dt
import datetime 


st.title("이것이 타이틀이다.")
st.header("이것이 헤더이다.")
st.subheader("이것이 서브헤더이다.")
st.text("이것이 일반 텍스트")

st.title("smile")
st.caption("캡션을 넣어보자")
st.markdown("**이지은**,*이지은*")

#코드표시
sample_code="""
def hello():
    print("Hello, world")"""

st.code(sample_code,language='python')

#마크다운 문법지원
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체를 설정할수 있다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]와 같은 수식도 지원한다.")
st.latex(r'\sqrt{x^2+y^2}=1')

st.title("데이터프레임 출력하기")


# dataframe 생성
dataframe=pd.DataFrame(
    {"first column":[1,2,3,4],
    "second column":[10,20,30,40]}
)
# dataframe
st.dataframe(dataframe)

# 테이블 출력
st.table(dataframe)

# 메트릭
st.metric(label="온도",value="25℃",delta="1.2℃")
st.metric(label="삼성전자",value="140,000원",delta="+3,800원")

#컬럼으로 영역 나누어 표기
col1, col2, col3= st.columns(3)
col1.metric(label="달러USD",value="1471원",delta="+30원")
col2.metric(label="유로EUR",value="1590원",delta="+20원")
col2.metric(label="엔JPY",value="1050원",delta="-5원")

# 버튼클릭/체크박스
button=st.button("버튼을 눌러주세요.")
if button:
    st.write(":blue[버튼]버튼 눌렀어")
agree=st.checkbox("체크박스를 누르세요.")
if agree:
    st.write("체크박스가 선택되었습니다")

# 라디오 버튼
mbti=st.radio(
    "당신의 MBTI는 무엇인가요?",
    ('INTJ','ENFP','ISTP','ESFJ'),
    index=2)
if mbti=='INTJ':
    st.write("당신은 전략가형입니다.")
elif mbti=='ENFP':
    st.write("당신은 활동가형입니다.")
elif mbti=='ISTP':
    st.write("당신은 장인형입니다.")
else:
    st.write("당신은 사교형입니다.")

# 셀렉트박스
favorite_color=st.selectbox(
    "당신이 가장 좋아하는 색깔은 무엇인가요?",
    ('빨강','파랑','노랑','초록')
)
st.write(f"당신의 선택한 색깔은 :red[{favorite_color}], 입니다.")

# 멀티셀렉박스
hobbies=st.multiselect(
    "당신의 취미를 선택해주세요",
    ['독서','여행','운동','요리','게임']
)
st.write("당신의 취미는 다음과 같습니다:",hobbies)

# 슬라이더
age=st.slider(
    "당신의 나이는 어떻게 되나요?",
    0,100,25
)
st.write(f"당신의 나이는 :blue[{age}]세 입니다.")

value=st.slider(
    "범위의 값을 다음과 같은 범위로 설정하세요",
    0.0, 100.0, (25.0, 75.0)
)
st.write(f"선택한 범위는:green[{value}]입니다.")

# 날짜선택
start_time=st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2026,1,1,0,0),
    max_value=dt(2026,12,31,0,0),
    value=dt(2026,1,15,0,0),
    step=datetime.timedelta(days=1),
    format="YYYY-MM-DD HH:mm"
)
st.write(f"약속날짜는: green[{start_time}]입니다.")

# 텍스트입력
title=st.text_input(
    label="가고싶은 여행지가 있나요?",
    placeholder="예:이집트,스위스,이탈리아"
)
st.write(f"당신이 가고싶은 여행지는:green[{title}]입니다.")

# 숫자 입력
number=st.number_input(
    label="당신이 좋아하는 숫자는 무엇인가요?",
    min_value=0,
    max_value=100,
    value=42,
    step=2
)
st.write(f"당신이 좋아하는 숫자는:green[{number}]입니다.")

# 파일 다운로드 버튼
st.download_button(
    label="CSV 다운로드",
    data=dataframe.to_csv(index=False).encode('utf-8'),
    file_name="sample.csv",
    mine="text/csv"
)






