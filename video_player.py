import tkinter as tk
from tkinter import messagebox as msb

from video_library import load_library_from_csv
from file_manager import save_library_to_csv

import font_manager as fonts

from check_videos import CheckVideos
from create_video_list import CreateVideoList



# Định nghĩa hàm khi nút "Check Videos" được nhấp:
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!") # Cập nhật trạng thái
    load_library_from_csv()  # Cập nhật dữ liệu từ file CSV
    CheckVideos(tk.Toplevel(window)) # Tạo cửa sổ con

# Định nghĩa hàm khi nút "Create Video List" được nhấp
def create_videos_clicked():
    status_lbl.configure(text="Create Video List button was clicked!") # Cập nhật trạng thái
    load_library_from_csv()  # Cập nhật dữ liệu từ file CSV
    CreateVideoList(tk.Toplevel(window)) # Tạo cửa sổ con
    
# Khởi tạo cửa sổ chính
window = tk.Tk()
window.geometry("400x150+20+20") # Cập nhật Kích thước và Vị trí
window.title("Video Player") # Đặt tiêu đề
window.tk_setPalette(background="#FBEAEB", foreground="#2F3C7E") # Đặt màu nền và màu chữ

# Cấu hình font
fonts.configure()

# Tạo nhãn tiêu đề
header_lbl = tk.Label(window, text="Select an option\nby clicking one\nof the buttons below")
header_lbl.grid(row=0, column=0, rowspan=2, sticky='W')
     
# Nút "Check Videos"
check_videos_btn = tk.Button(window, text="Check Videos",foreground="#FBEAEB", background="#2F3C7E", command=check_videos_clicked)
check_videos_btn.grid(row=0, column=1, padx=10, pady=10, sticky='W')
# Nút "Create Video List"
create_video_list_btn = tk.Button(window, text="Create Video List",foreground="#FBEAEB", background="#2F3C7E", command=create_videos_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

# Tạo nhãn trạng thái
status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Chạy vòng lặp chính của ứng dụng để hiển thị cửa sổ
window.mainloop()
