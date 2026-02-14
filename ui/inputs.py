import os
import streamlit as st

def render_project_input():
    project_path = st.text_input(
        "Dán đường dẫn thư mục dự án",
        placeholder="C:/Users/Name/project hoặc /home/user/project"
    )
    valid_project = bool(project_path and os.path.isdir(project_path))
    return project_path, valid_project
