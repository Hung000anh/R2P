import os
from services.files import read_file

def build_project_overview(
    project_name,
    tree_lines,
    files,
    project_path,
    system_message=None,
    user_message=None
):
    parts = []

    if system_message:
        parts += ["===== SYSTEM MESSAGE =====", system_message.strip(), ""]

    if user_message:
        parts += ["===== USER MESSAGE =====", user_message.strip(), ""]

    parts += ["===== PROJECT TREE =====", f"📦 {project_name}", *tree_lines, ""]

    if files:
        parts.append("===== MÃ NGUỒN ĐÃ CHỌN =====")
        for f in files:
            parts.append(f"\n--- FILE: {os.path.relpath(f, project_path)} ---")
            parts.append(read_file(f))

    return "\n".join(parts)
