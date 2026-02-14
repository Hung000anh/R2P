import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.header("Thiết lập ngữ cảnh")

        system_message = st.text_area(
            "System message",
            placeholder="Ví dụ: Bạn là một kiến trúc sư phần mềm.",
            height = 100
        )

        user_message = st.text_area(
            "User message",
            placeholder="Ví dụ: Phân tích thư mục và cải tiến kiến trúc nếu có.",
            height = 100
        )

        if st.button("Áp dụng"):
            st.session_state.system_message = system_message
            st.session_state.user_message = user_message
