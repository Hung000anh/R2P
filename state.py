import streamlit as st

def init_state():
    if "ignore_exts" not in st.session_state:
        st.session_state.ignore_exts = set()
    if "checked_files" not in st.session_state:
        st.session_state.checked_files = []
