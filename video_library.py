from library_item import LibraryItem
import csv
from file_manager import save_library_to_csv


# Khởi tạo một từ điển (dictionary) để lưu trữ các mục trong thư viện
library = {}

# Thêm các mục vào thư viện
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4, 0)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5, 0)
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, 0)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1, 0)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, 0)

# Hàm đọc dữ liệu từ file CSV và cập nhật thư viện
def load_library_from_csv():
    with open('videos.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua hàng đầu tiên
        for row in reader:
            id, name, director, rating, plays = row 
            library[id] = LibraryItem(name, director, int(rating), int(plays))


# Liệt kê tất cả các mục trong thư viện
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


# Lấy tên của một mục dựa trên mã số
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


# Lấy tên đạo diễn của một mục dựa trên mã số
def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


# Lấy xếp hạng của một mục dựa trên mã số
def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

# Đặt xếp hạng cho một mục dựa trên mã số
def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

# Lấy số lần phát của một mục dựa trên mã số
def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

# Tăng số lần phát của một mục lên 1 dựa trên mã số
def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return