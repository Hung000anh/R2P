import os

IGNORE_FOLDERS = {"__pycache__", "venv", ".venv", ".ico" ,".png", ".jpg"}

def scan_extensions(root_dir):
    exts = set()
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in IGNORE_FOLDERS]
        for f in files:
            ext = os.path.splitext(f)[1]
            if ext:
                exts.add(ext)
    return sorted(exts)

def build_tree(root_dir, ignore_exts):
    tree = {}
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in IGNORE_FOLDERS]
        rel = os.path.relpath(root, root_dir)
        cur = tree
        if rel != ".":
            for p in rel.split(os.sep):
                cur = cur.setdefault(p, {})
        for d in dirs:
            cur.setdefault(d, {})
        for f in files:
            if os.path.splitext(f)[1] not in ignore_exts:
                cur[f] = None
    return tree

def tree_to_nodes(tree, base):
    nodes = []
    for name, sub in sorted(tree.items()):
        path = os.path.join(base, name)
        if isinstance(sub, dict):
            nodes.append({
                "label": f"📁 {name}",
                "value": path,
                "children": tree_to_nodes(sub, path),
                "showCheckbox": False
            })
        else:
            nodes.append({"label": f"📄 {name}", "value": path})
    return nodes

def render_tree_pretty(tree, prefix=""):
    lines = []
    items = sorted(tree.items(), key=lambda x: (not isinstance(x[1], dict), x[0]))
    for i, (name, sub) in enumerate(items):
        last = i == len(items) - 1
        branch = "└── " if last else "├── "
        if isinstance(sub, dict):
            lines.append(prefix + branch + f"📁 {name}/")
            lines.extend(render_tree_pretty(sub, prefix + ("    " if last else "│   ")))
        else:
            lines.append(prefix + branch + f"📄 {name}")
    return lines

def collect_folder_values(nodes):
    vals = []
    for n in nodes:
        if "children" in n:
            vals.append(n["value"])
            vals.extend(collect_folder_values(n["children"]))
    return vals
