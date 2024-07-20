# Link demo : https://drive.google.com/file/d/1T-9Osh03ApQNMnrHBxNpYbEQDGQfMam4/view?usp=sharing
aizen_

## Công nghệ sử dụng

- **Langchain**: Một framework để xây dựng các ứng dụng dựa trên chuỗi ngôn ngữ.
- **Huggingface**: Thư viện để phát triển thêm những features ( ở đây là hai mô hình dành cho việc lấy thông tin bức ảnh )
- **Streamlit**: Một công cụ mã nguồn mở để tạo giao diện web cho các ứng dụng machine learning.
- **Gemini**: Mô hình ngôn ngữ sử dụng trong dự án này.

## Cài đặt

## Lưu ý tải 2 models ở file sau và cho vào file models để thực hiện xử lý ảnh : 
Link : https://huggingface.co/mys/ggml_llava-v1.5-7b
### Yêu cầu

- Python 3.12
- Các thư viện cần thiết được liệt kê trong file `requiremens.txt`

### Hướng dẫn cài đặt

1. Clone repository:
    ```bash
    git clone https://github.com/linhphongz/aizen_chatbot.git
    cd aizen_chatbot
    ```
2. Cài đặt các thư viện:
    ```bash
    pip install -r requirements.txt
    ```

## Sử dụng

### Chạy ứng dụng

- Chạy ứng dụng với terminal:
    ```bash
   streamlit run app.py
    ```
- Chạy ứng dụng với Docker:
  ⚠️Hiện tại build xong file Docker để chạy chương trình


## Đóng góp

Chúng tôi hoan nghênh mọi đóng góp cho dự án này. Vui lòng mở issue hoặc tạo pull request để đóng góp.
