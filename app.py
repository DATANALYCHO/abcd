import streamlit as st
from openai import OpenAI


MODEL = "gpt-4o-mini"

st.set_page_config(
    page_title="OpenAI Chatbot",
    page_icon="💬",
    layout="centered",
)

st.title("💬 OpenAI 챗봇")
st.caption(f"모델: {MODEL} · Streamlit Community Cloud")


def get_client() -> OpenAI:
    """Create an OpenAI client from Streamlit Community Cloud Secrets."""
    api_key = st.secrets.get("OPENAI_API_KEY")
    if not api_key:
        st.error(
            "OPENAI_API_KEY가 설정되지 않았습니다. "
            "Streamlit Cloud의 App settings → Secrets에 키를 등록해 주세요."
        )
        st.stop()
    return OpenAI(api_key=api_key)


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 무엇을 도와드릴까요?",
        }
    ]

with st.sidebar:
    st.header("설정")
    if st.button("대화 초기화", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
        ]
        st.rerun()
    st.divider()
    st.write("API 키는 Streamlit Secrets에서 안전하게 관리됩니다.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        try:
            client = get_client()
            stream = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                full_response += delta
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )
        except Exception as error:
            response_placeholder.error(f"응답을 가져오는 중 오류가 발생했습니다: {error}")
