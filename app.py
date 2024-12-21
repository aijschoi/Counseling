import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# 웹페이지 기본 설정
st.set_page_config(page_title="AI 친구와 대화하기", layout="wide")

# 웹페이지 헤더
st.title("💬 AI 친구와 대화해보세요!")
st.write("질문을 입력하고 AI와 대화해보세요.")

# 사용자 입력 창
user_input = st.text_input("당신의 질문은 무엇인가요?", "")

# 챗봇 응답
def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"오류가 발생했습니다: {e}"

# 응답 출력
if st.button("응답 받기") and user_input:
    with st.spinner("AI가 생각 중..."):
        response = get_response(user_input)
        st.text_area("AI의 응답", response, height=300)
