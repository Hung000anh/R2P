import streamlit as st
from state import init_state
from ui.inputs import render_project_input
from ui.sidebar import render_sidebar
from ui.tree import render_tree_selector
from ui.content import render_main_content

st.set_page_config(layout="wide")
st.title("Project Directory Tree")

init_state()

project_path, valid_project = render_project_input()
render_sidebar()

col_content, col_select = st.columns([3, 1])
with col_select:
    render_tree_selector(project_path, valid_project)

with col_content:
    render_main_content(project_path, valid_project)
