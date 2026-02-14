import streamlit as st
from streamlit_tree_select import tree_select
from services.tree import (
    scan_extensions,
    build_tree,
    tree_to_nodes,
    collect_folder_values,
    render_tree_pretty,
)

def render_tree_selector(project_path, valid_project):
    if not valid_project:
        return

    all_exts = scan_extensions(project_path)
    st.subheader("Ignore theo đuôi file")

    with st.expander("Chọn đuôi file cần ignore", expanded=False):
        for ext in all_exts:
            st.checkbox(ext, key=f"ignore_{ext}")

    st.session_state.ignore_exts = {
        ext for ext in all_exts
        if st.session_state.get(f"ignore_{ext}", False)
    }

    tree = build_tree(project_path, st.session_state.ignore_exts)
    nodes = tree_to_nodes(tree, project_path)

    result = tree_select(
        nodes=nodes,
        check_model="leaf",
        only_leaf_checkboxes=True,
        expanded=collect_folder_values(nodes),
        show_expand_all=True
    )

    st.session_state.tree = tree
    st.session_state.tree_lines = render_tree_pretty(tree)
    st.session_state.checked_files = result["checked"]
