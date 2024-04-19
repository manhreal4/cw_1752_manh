import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb

import csv

import video_library as lib

from video_library import library
from video_library import load_library_from_csv
from file_manager import save_library_to_csv
from library_item import LibraryItem

import font_manager as fonts



# Hàm thiết lập nội dung cho một vùng văn bản trong giao diện người dùng
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


# Lớp tạo giao diện kiểm tra video
class CheckVideos():
    
    # Phương thức khởi tạo của class CheckVideos, được gọi khi một đối tượng CheckVideos được tạo
    def __init__(self, window):
        window.geometry("850x350+20+400") # Cập nhật Kích thước và Vị trí
        window.title("Check Videos") # Đặt tiêu đề
        window.tk_setPalette(background="#FBEAEB", foreground="#2F3C7E") # Đặt màu nền và màu chữ
        self.video_lib = VideoLib()  # Khởi tạo một đối tượng video_lib


        # Nút "List All Videos" có chức năng liệt kê tất cả các video
        list_videos_btn = tk.Button(window, text="List All Videos",foreground="#FBEAEB", background="#2F3C7E", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)


        # Tạo vùng nhập dữ liệu ID Video
        enter_lbl = tk.Label(window, text="Enter Video ID", background="#FBEAEB")
        enter_lbl.grid(row=0, column=2, padx=10, pady=10, sticky='E')
        # Vùng nhập dữ liệu
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=3, padx=10, pady=10)


        # Nút "Check Video" để kiểm tra thông tin về video có ID đã nhập
        check_video_btn = tk.Button(window, text="Check Video",foreground="#FBEAEB", background="#2F3C7E", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=4)


        # Tạo một vùng văn bản cuộn ScrolledText để hiển thị danh sách video
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1,rowspan=5, column=0, columnspan=3, sticky="W", padx=10, pady=10)       
        self.list_txt.configure(background="#F0A07C", foreground="#4A274F")  # Cập nhật màu nền và màu chữ


        # Tạo các nhãn để hiển thị tiêu đề của thông tin chi tiết
        tk.Label(window, text="ID :", width=7).grid(row=1, column=3, sticky="W")
        tk.Label(window, text="Name :", width=7).grid(row=2, column=3, sticky="W")
        tk.Label(window, text="Director :", width=7).grid(row=3, column=3, sticky="W")
        tk.Label(window, text="Rating :", width=7).grid(row=4, column=3, sticky="W")
        tk.Label(window, text="Plays :", width=7).grid(row=5, column=3, sticky="W")


        # Tạo các entry để hiển thị thông tin chi tiết của video
        # ID
        self.id_entry = tk.Entry(window, width=24)
        self.id_entry.grid(row=1, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Name
        self.name_entry = tk.Entry(window, width=24)
        self.name_entry.grid(row=2, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Director
        self.director_entry = tk.Entry(window, width=24)
        self.director_entry.grid(row=3, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Rating
        self.rating_entry = tk.Entry(window, width=24)
        self.rating_entry.grid(row=4, column=4,columnspan=2, sticky="W", padx=2, pady=2)
        # Plays
        self.plays_label = tk.Label(window, text="", width=10)
        self.plays_label.grid(row=5, column=4,columnspan=2, sticky="W", padx=2, pady=2)


        # Các nút chức năng
        # Nút "Add"
        self.btn_add = tk.Button(window, text='Add',foreground="#FBEAEB", background="#2F3C7E", command=self.add_video)
        self.btn_add.grid(row=6, column=3, sticky='W')
        # Nút "Update"
        self.btn_update = tk.Button(window, text='Update',foreground="#295F2D", background="#FFE67C", command=self.update_video)
        self.btn_update.grid(row=6, column=4, sticky='W')
        # Nút "Delete"
        self.btn_delete = tk.Button(window, text='Delete',foreground="#FCE77D", background="#F96167", command=self.delete_video)
        self.btn_delete.grid(row=6, column=5, sticky='W')
        

        # Tạo một nhãn để hiển thị trạng thái hoạt động
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), background="#FBEAEB", foreground="#2F3C7E")
        self.status_lbl.grid(row=6, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        self.list_videos_clicked()
        
    
    # Xử lý sự kiện khi nút "Check Video" được nhấn
    def check_video_clicked(self):
        self.status_lbl.configure(text="Check Video button was clicked!") # Cập nhật trạng thái

        key = self.input_txt.get() # Lấy id từ ô nhập liệu input_txt

        # Kiểm tra xem ID có tồn tại hay không
        if not self.video_lib.is_id_exists(key):
            msb.showwarning('Warning', f'Video with ID {key} does not exist!')
            return

        name = lib.get_name(key) # Lấy tên video có id là key
        director = lib.get_director(key) # Lấy tên tác giả
        rating = lib.get_rating(key) # Lấy xếp hạng
        play_count = lib.get_play_count(key) # Lấy lượt phát

        # Cập nhật giá trị của các entry để hiển thị thông tin chi tiết
        # ID
        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, key)
        # Name
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        # Director
        self.director_entry.delete(0, tk.END)
        self.director_entry.insert(0, director)
        # Rating
        self.rating_entry.delete(0, tk.END)
        self.rating_entry.insert(0, rating)
        # Plays
        self.plays_label.configure(text=play_count)
            


    # Xử lý sự kiện khi nút "List All Videos" được nhấn
    def list_videos_clicked(self):
        self.status_lbl.configure(text="List Videos button was clicked!") # Cập nhật trạng thái
        self.video_lib.load_videos_from_csv()  # Load lại danh sách video từ CSV
        video_list = lib.list_all() # Lấy tất cả các video
        set_text(self.list_txt, video_list) # Cập nhật văn bản lên vùng cuộn list_txt


    # Xử lý sự kiện khi nút "Delete" được nhấn
    def delete_video(self):
        self.status_lbl.configure(text="Delete button was clicked!") # Cập nhật trạng thái
        
        id = self.input_txt.get() # Lấy id từ ô nhập liệu input_txt
        
        if not id: # Kiểm tra đã nhập id muốn xóa chưa
            msb.showwarning('Warning', 'Please enter the ID of the video to be deleted!')
            return

        # Kiểm tra xem ID có tồn tại trong thư viện không
        if not self.video_lib.is_id_exists(id):
            msb.showwarning('Warning', f'Video with ID {id} does not exist!')
            return

        # Hiển thị hộp thoại xác nhận trước khi xóa
        confirmation = msb.askyesno('Confirmation', f"Are you sure you want to delete the video with ID {id}?")

        if confirmation:
            try:
                # Xóa video từ thư viện video
                self.video_lib.delete_video_by_id(id)
                # Xóa video từ danh sách hiển thị
                self.list_txt.delete(1.0, tk.END)
                # Tải lại danh sách video
                self.list_videos_clicked()
                msb.showinfo('Success', 'The video has been successfully deleted!')
            except Exception as e:
                msb.showerror('Error', e)



    # Xử lý sự kiện khi nút "Update" được nhấn
    def update_video(self):
        self.status_lbl.configure(text="Update button was clicked!") # Cập nhật trạng thái
        
        # Lấy ID từ vùng nhập liệu
        id = self.input_txt.get()
        if not id:
            msb.showwarning('Warning', 'Please enter the ID of the video to be updated!')
            return

        # Kiểm tra xem ID có tồn tại hay không
        if not self.video_lib.is_id_exists(id):
            msb.showwarning('Warning', f'Video with ID {id} does not exist!')
            return

        # Hiển thị hộp thoại xác nhận trước khi xóa
        confirmation = msb.askyesno('Confirmation', f"Are you sure you want to update the video with ID {id}?")

        if confirmation:
            try:
                # Lấy thông tin video từ các ô nhập liệu
                name = self.name_entry.get()
                director = self.director_entry.get()
                rating = self.rating_entry.get()
                # Cập nhật video trong thư viện video
                self.video_lib.update_video_by_id(id, name, director, int(rating))
                # Xóa và tải lại danh sách video
                self.list_videos_clicked()
                self.video_lib.save_videos_to_csv()
                msb.showinfo('Success', 'The video has been updated successfully!')
            except Exception as e:
                msb.showerror('Error', e)


    # Xử lý sự kiện khi nút "Add" được nhấn
    def add_video(self):
        self.status_lbl.configure(text="Add button was clicked!") # Cập nhật trạng thái
        
        # Lấy thông tin video từ các ô nhập liệu
        id = self.id_entry.get()
        name = self.name_entry.get()
        director = self.director_entry.get()
        rating = self.rating_entry.get()

        # Kiểm tra xem ID đã tồn tại hay chưa
        if self.video_lib.is_id_exists(id):
            msb.showwarning('Warning', f'Video with ID {id} already exists!')
            return

        # Hiển thị hộp thoại xác nhận trước khi xóa
        confirmation = msb.askyesno('Confirmation', f"Are you sure you want to add a new video?")
        
        if confirmation:
            try:
                # Tạo một đối tượng video
                video = Video(id, name, director, int(rating))
                # Thêm video vào thư viện video
                self.video_lib.add_video(video)
                # Thêm video vào danh sách hiển thị
                self.list_txt.insert(tk.END, name)
                # Cập nhật thư viện
                library[id] = LibraryItem(name, director, int(rating))
                # Lưu video vào tệp CSV
                self.video_lib.save_videos_to_csv()
                msb.showinfo('Success', 'The video has been added successfully!')
            except Exception as e:
                msb.showerror('Error', e)


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc



# Lớp định nghĩa một video
class Video:
    def __init__(self, id, name, director, rating):
        self.__id = id
        self.__name = name
        self.__director = director
        self.__rating = rating
        
    # Getter cho id
    @property 
    def id(self):
        return self.__id
    
    # Getter cho name
    @property
    def name(self):
        return self.__name
    # Setter cho name
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('name cannot be empty')
        self.__name = value
        
    # Getter cho director
    @property
    def director(self):
        return self.__director
    # Setter cho director
    @director.setter
    def director(self, value):
        if value == '':
            raise ValueError('director cannot be empty')
        self.__director = value
        
    # Getter cho rating
    @property
    def rating(self):
        return self.__rating
    # Setter cho rating
    @rating.setter
    def rating(self, value):
        if value < 0 and value > 5:
            raise ValueError('rating cannot be negative')
        self.__rating = value
        
        
        
# Lớp quản lý thư viện video
class VideoLib:
    
    def __init__(self):
        self.__videos = []
        self.load_videos_from_csv()  # Load videos from CSV file

    # Phương thức kiểm tra xem ID đã tồn tại hay chưa
    def is_id_exists(self, id):
        return id in library

    # Phương thức để load danh sách video từ tệp CSV
    def load_videos_from_csv(self):
        self.__videos.clear()  # Xóa video hiện có
        library.clear()  # Xóa thư viện hiện có
        with open('videos.csv', 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader)  # Bỏ qua tiêu đề
            play_index = header.index('Plays')  # Lấy chỉ mục của cột 'Plays'
            for row in csvreader:
                id = row[0]
                name = row[1]
                director = row[2]
                rating = int(row[3])
                plays = int(row[play_index])  # Lấy số lượt xem từ cột 'Plays'
                video = Video(id, name, director, rating)
                self.__videos.append(video)
                # Update library here
                library[id] = LibraryItem(name, director, rating, plays)

    # Phương thức để lấy tên của tất cả các video
    def get_name(self):
        return [video.name for video in self.__videos]

    # Phương thức để lấy thông tin của một video cụ thể
    def get_video(self, i):
        video = self.__videos[i]
        return video.id, video.name, video.director, video.rating
        
    # Phương thức update video
    def update_video_by_id(self, id, name, director, rating):
        # Tìm video dựa vào id, gán idex = chỉ mục của video đó trong danh sách, nếu không thấy trả về None
        index = next((i for i, video in enumerate(self.__videos) if video.id == id), None)
        if index is not None: # Kiểm tra video tồn tại
            video = self.__videos[index] # Gán video được tìm thấy vào biến video
            video.name = name # Gán tên mới
            video.director = director # Gán tác giả mới
            video.rating = rating # Gán đánh giá mới
            self.save_videos_to_csv()  # Lưu video vào tệp CSV sau khi cập nhật
        else:
            raise ValueError(f'Không tìm thấy video với ID {id}')

    # Phương thức add video
    def add_video(self, v):
        self.__videos.append(v)
        self.save_videos_to_csv()  # Save videos to CSV file after adding
        
    # Phương thức delete video
    def delete_video_by_id(self, id):
        # Tìm video dựa vào id, gán idex = chỉ mục của video đó trong danh sách, nếu không thấy trả về None
        index = next((i for i, video in enumerate(self.__videos) if video.id == id), None) 
        if index is not None: # Kiểm tra video tồn tại
            del self.__videos[index] # Xóa video khỏi danh sách
            del library[id]  # Xóa video khỏi thư viện
            self.save_videos_to_csv()  # Lưu thay đổi vào tệp CSV sau khi xóa
        else:
            raise ValueError(f'Video with ID {id} not found!')

    # Phương thức lưu thông tin vào tệp CSV 
    def save_videos_to_csv(self):
        # Mở tệp csv, nếu tồn tại sẽ ghi đè, nếu không sẽ tạo mới
        with open('videos.csv', 'w', newline='') as f:
            csvwriter = csv.writer(f) # Tạo đối tượng để ghi dữ liệu vào tệp CSV được mở
            csvwriter.writerow(['ID', 'Name', 'Director', 'Rating', 'Plays'])  # Viết hàng tiêu đề
            # Duyệt danh sách các video
            for video in self.__videos:
                # Viết 1 hàng dữ liệu, lượt xem mặc định là 0
                csvwriter.writerow([video.id, video.name, video.director, video.rating, 0]) 
                
    
