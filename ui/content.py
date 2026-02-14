import os
import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
from services.files import read_file, guess_language
from prompt.builder import build_project_overview
def render_main_content(project_path, valid_project):
    if not valid_project:
        st.info("Chưa có thư mục dự án hợp lệ")
        return

    project_name = os.path.basename(os.path.normpath(project_path))

    col_title, col_btn = st.columns([5, 1])
    with col_title:
        st.header("Tổng quan dự án")

    with col_btn:
        full_text = build_project_overview(
            project_name,
            st.session_state.tree_lines,
            st.session_state.checked_files,
            project_path,
            st.session_state.get("system_message"),
            st.session_state.get("user_message"),
        )
        st_copy_to_clipboard(text= full_text, before_copy_label="📋 Sao chép", after_copy_label="✅ Đã chép!")

    if st.session_state.get("system_message"):
        st.subheader("Yêu cầu hệ thống")
        st.markdown(st.session_state.system_message)

    if st.session_state.get("user_message"):
        st.subheader("Yêu cầu người dùng")
        st.markdown(st.session_state.user_message)

    st.subheader("Cây thư mục")
    st.text(f"📦 {project_name}\n" + "\n".join(st.session_state.tree_lines))

    if st.session_state.checked_files:
        st.divider()
        st.subheader("Mã nguồn đã chọn")
        for f in st.session_state.checked_files:
            st.markdown(f"### `{os.path.relpath(f, project_path)}`")
            st.code(read_file(f), language=guess_language(f))
