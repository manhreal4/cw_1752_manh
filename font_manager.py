# cấu hình font cho giao diện người dùng trong ứng dụng sử dụng thư viện tkinter

import tkinter.font as tkfont

# sử dụng để cấu hình font cho các phần khác nhau của giao diện người dùng

def configure():
    # family = "Segoe UI"
    family = "Helvetica"
    
    # Trả về font mặc định được sử dụng cho các phần tử như nhãn (Label), nút (Button), vv
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=15, family=family)
    
    # Trả về font được sử dụng cho vùng văn bản (Text)
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=12, family=family)
    
    # Trả về font được sử dụng cho vùng văn bản cố định (Text có kiểu font cố định)
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=12, family=family)
