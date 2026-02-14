# R2P – Project Directory Tree Prompt Builder

## 1. Mục đích

R2P là ứng dụng xây dựng bằng Streamlit cho phép:

* Quét và hiển thị cấu trúc thư mục của một project.
* Chọn file nguồn trực tiếp từ giao diện tree.
* Tạo nội dung tổng hợp (project tree + mã nguồn đã chọn).
* Sinh prompt hoàn chỉnh để sử dụng cho LLM (ChatGPT, Claude, Gemini…).

Ứng dụng phục vụ mục tiêu phân tích code base, review kiến trúc, sinh tài liệu, hoặc tạo prompt AI một cách có cấu trúc.

---

## 2. Tính năng chính

1. Nhập đường dẫn thư mục dự án.
2. Tự động xây dựng cây thư mục (directory tree).
3. Cho phép ignore theo đuôi file (.py, .js, .md, …).
4. Chọn nhiều file từ tree bằng checkbox.
5. Hiển thị mã nguồn có syntax highlighting.
6. Thêm System Message và User Message.
7. Sinh khối nội dung chuẩn gồm:

   * SYSTEM MESSAGE
   * USER MESSAGE
   * PROJECT TREE
   * MÃ NGUỒN ĐÃ CHỌN
8. Sao chép toàn bộ nội dung chỉ với một nút bấm.

---

## 3. Cấu trúc thư mục

```
📦 R2P
├── 📁 assets/
│   └── prompt.ico
├── 📁 prompt/
│   └── builder.py
├── 📁 services/
│   ├── files.py
│   └── tree.py
├── 📁 ui/
│   ├── content.py
│   ├── inputs.py
│   ├── sidebar.py
│   └── tree.py
├── app.py
├── requirements.txt
├── run.bat
└── state.py
```

---

## 4. Kiến trúc hệ thống

### 4.1 app.py – Entry Point

* Cấu hình layout Streamlit (wide).
* Khởi tạo session state.
* Render các thành phần giao diện.
* Chia layout 2 cột:

  * Cột trái: nội dung chính.
  * Cột phải: tree selector.

Luồng xử lý:

1. init_state()
2. Nhập project path
3. Render sidebar
4. Render tree selector
5. Render nội dung chính

---

### 4.2 state.py – Quản lý trạng thái

Quản lý các biến trong `st.session_state`:

* ignore_exts
* checked_files
* tree
* tree_lines
* system_message
* user_message

Tách state riêng giúp tránh logic rải rác trong UI.

---

### 4.3 services/

#### services/tree.py

Chức năng:

* scan_extensions(): quét toàn bộ đuôi file.
* build_tree(): xây dựng cấu trúc thư mục dạng dictionary.
* tree_to_nodes(): chuyển sang format dùng cho streamlit-tree-select.
* render_tree_pretty(): xuất tree dạng ASCII.
* collect_folder_values(): phục vụ expand tree.

Tự động ignore:

* **pycache**
* venv
* .venv
* thư mục bắt đầu bằng dấu chấm

#### services/files.py

* read_file(): đọc file UTF-8, bỏ qua lỗi encoding.
* guess_language(): suy đoán ngôn ngữ để highlight code.

---

### 4.4 ui/

Tách UI thành nhiều module độc lập:

* inputs.py: nhập đường dẫn dự án.
* sidebar.py: nhập System / User message.
* tree.py: hiển thị và chọn file từ tree.
* content.py: hiển thị tổng quan và mã nguồn.

Thiết kế theo hướng:

* UI không chứa logic xử lý nặng.
* Logic đặt trong services.
* Prompt builder tách riêng.

---

### 4.5 prompt/builder.py

Hàm `build_project_overview()` tạo nội dung tổng hợp theo cấu trúc chuẩn:

```
===== SYSTEM MESSAGE =====
...

===== USER MESSAGE =====
...

===== PROJECT TREE =====
📦 project_name
├── ...

===== MÃ NGUỒN ĐÃ CHỌN =====
--- FILE: path/to/file ---
...
```

Đây là phần cốt lõi để tạo prompt dùng cho LLM.

---

## 5. Yêu cầu hệ thống

* Python 3.9 trở lên
* pip

Dependencies:

* streamlit
* streamlit-tree-select
* st-copy-to-clipboard

---

## 6. Cài đặt

Cài thư viện:

```
pip install -r requirements.txt
```

---

## 7. Chạy ứng dụng

### Cách 1

```
streamlit run app.py
```

### Cách 2 (Windows)

Chạy:

```
run.bat
```

Script sẽ:

1. Tạo virtualenv nếu chưa tồn tại.
2. Cài dependency.
3. Chạy app tại port 8502.

---

## 8. Cách sử dụng

1. Mở ứng dụng.
2. Nhập đường dẫn project.
3. Chọn ignore extension nếu cần.
4. Tick các file muốn đưa vào prompt.
5. Nhập System / User message trong sidebar.
6. Nhấn “Áp dụng”.
7. Nhấn “Sao chép” để copy toàn bộ nội dung.

---

## 9. Ứng dụng thực tế

* Phân tích kiến trúc project bằng AI.
* Code review tự động.
* Sinh tài liệu README.
* Refactor gợi ý.
* Chuẩn bị prompt lớn có cấu trúc rõ ràng.
* Hỗ trợ làm việc với code base lớn.

---

## 10. Hướng mở rộng

* Hỗ trợ ignore theo pattern (.gitignore).
* Thêm bộ lọc theo kích thước file.
* Thêm chế độ chỉ xuất tree.
* Thêm chế độ export ra Markdown.
* Tích hợp trực tiếp API LLM.
* Thêm tìm kiếm file trong tree.

---

## 11. Tổng kết

R2P là công cụ trực quan hóa và trích xuất mã nguồn có cấu trúc, được thiết kế module hóa rõ ràng (UI – Services – Prompt Builder – State). Mục tiêu chính là tạo một workflow hiệu quả để chuẩn bị prompt AI từ bất kỳ project nào.
