import tkinter as tk
from tkinter import messagebox as msb
from video_library import library
from video_library import load_library_from_csv
from file_manager import save_library_to_csv


class CreateVideoList:
    
    # Phương thức khởi tạo cho lớp
    def __init__(self, window):
        # Gán đối tượng cửa sổ cho thuộc tính window của lớp
        self.window = window 
        window.title("Create Video List") # Đặt tiêu đề
        window.geometry("950x600+550+20") # Cập nhật Kích thức và Vị trí
        window.tk_setPalette(background="#FBEAEB", foreground="#2F3C7E") # Đặt màu nền và màu chữ
        # Khởi tạo danh sách trống
        self.selected_videos = []
        self.create_widgets() # Gọi phương thức tạo giao diện người dùng
        load_library_from_csv()


    # Phương thức tạo giao diện người dùng
    def create_widgets(self):
        # Phần hiển thị các video trong thư viện
        self.lbl_instruction = tk.Label(self.window, text="Create your own playlists")
        self.lbl_instruction.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.lbl_instruction = tk.Label(self.window, text="List all video")
        self.lbl_instruction.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.lst_videos = tk.Listbox(self.window, width=35, height=7, selectmode=tk.MULTIPLE)
        self.lst_videos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.fill_videos()
        self.lst_videos.configure(background="#F0A07C", foreground="#4A274F")  # Đặt màu nền và màu chữ
        
        # Phần hiển thị playlist vừa chọn
        self.lbl_instruction = tk.Label(self.window, text="Your playlist")
        self.lbl_instruction.grid(row=4, column=3, columnspan=2, padx=10, pady=10)
        
        self.lst_your_videos = tk.Listbox(self.window, width=35, height=7, selectmode=tk.MULTIPLE)
        self.lst_your_videos.grid(row=6,rowspan=3, column=3, columnspan=2, padx=10, pady=10)
        
        self.lst_your_videos.configure(background="#F0A07C", foreground="#4A274F") # Đặt màu nền và màu chữ
        
        # Nút "Add Video to Playlist"
        self.btn_add_to_playlist = tk.Button(self.window, text="Add to Playlist",foreground="#FBEAEB", background="#2F3C7E", command=self.add_to_playlist)
        self.btn_add_to_playlist.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Nút "Run"
        self.btn_run_playlist = tk.Button(self.window, text="Run",foreground="#FBEAEB", background="#2F3C7E", command=self.run_playlist)
        self.btn_run_playlist.grid(row=6, column=5, padx=10, pady=10)
        
        # Nút "Remove"
        self.btn_remove_playlist = tk.Button(self.window, text="Remove",foreground="#FCE77D", background="#F96167", command=self.remove_playlist)
        self.btn_remove_playlist.grid(row=7, column=5, padx=10, pady=10)
        
        # Nút "Reset"
        self.btn_reset_playlist = tk.Button(self.window, text="Reset",foreground="#295F2D", background="#FFE67C", command=self.reset_playlist)
        self.btn_reset_playlist.grid(row=8, column=5, padx=10, pady=10)
        
        # Nhãn trạng thái
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=9, column=4, padx=10, pady=10)
        
        # Thêm menu dropdown cho lựa chọn tìm kiếm
        self.search_option = tk.StringVar()  # Biến để lưu trữ loại tìm kiếm
        self.search_option.set("Name")  # Mặc định là tìm kiếm theo tên

        self.option_menu = tk.OptionMenu(self.window, self.search_option, "Name", "Director", "ID")
        self.option_menu.grid(row=1, column=3, padx=0, pady=5)

        # Thêm trường nhập thông tin tìm kiếm
        self.entry_search_input = tk.Entry(self.window, width=30)
        self.entry_search_input.grid(row=1, column=4, padx=0, pady=5)
        
        # Nút "Search"
        self.btn_search = tk.Button(self.window, text="Search",foreground="#FBEAEB", background="#2F3C7E", command=self.search_videos)
        self.btn_search.grid(row=1, column=5, padx=5, pady=5)
        
        # Label hiển thị kết quả tìm kiếm
        self.lbl_instruction = tk.Label(self.window, text="Search videos")
        self.lbl_instruction.grid(row=0, column=3, columnspan=2, padx=10, pady=10)
        
        self.lbl_search_result = tk.Listbox(self.window, width=35, height=7, selectmode=tk.MULTIPLE)
        self.lbl_search_result.grid(row=3, column=3, columnspan=2, padx=10, pady=10)
        
        self.lbl_search_result.configure(background="#F0A07C", foreground="#4A274F")  # Đặt màu nền và màu chữ
        
        # Nút "Add"
        self.btn_add_to_playlist_search = tk.Button(self.window, text="Add",foreground="#FBEAEB", background="#2F3C7E", command=self.add_selected_from_search)
        self.btn_add_to_playlist_search.grid(row=3, rowspan=3, column=5, padx=5, pady=5)
        
        # Label hiển thị lịch sử video vừa được ấn phát
        self.lbl_history_instruction = tk.Label(self.window, text="History")
        self.lbl_history_instruction.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.lbl_play_history = tk.Listbox(self.window, width=35, height=4, selectmode=tk.MULTIPLE)
        self.lbl_play_history.grid(row=7,rowspan=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.lbl_play_history.configure(background="#F0A07C", foreground="#4A274F")  # Đặt màu nền và màu chữ
        
        # Nút "Remove history"
        self.btn_remove_history = tk.Button(self.window, text="Remove history",foreground="#FCE77D", background="#F96167", command=self.remove_history)
        self.btn_remove_history.grid(row=9, column=0, padx=5, pady=5)
        
        # Nút "Remove all"
        self.btn_remove_history_all = tk.Button(self.window, text="Remove all",foreground="#295F2D", background="#FFE67C", command=self.remove_history_all)
        self.btn_remove_history_all.grid(row=9, column=1, padx=5, pady=5)
        
        
    # Phương thức điền dữ liệu video của giao diện người dùng
    def fill_videos(self):
        # Xóa tất cả các mục đã có trong danh sách
        self.lst_videos.delete(0, tk.END) 
        # Lặp qua từng cặp key - value trong thư viện và thêm vào danh sách hiển thị
        for video_id, video_info in library.items():
            # Thêm một mục mới vào danh sách video, hiển thị thông tin về video
            self.lst_videos.insert(tk.END, f"{video_id} : {video_info.name} - {video_info.director}")


    # Xử lý sự kiện khi nút "Add to Playlish" được nhấn
    def add_to_playlist(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Add to Playlish button was clicked!")
        load_library_from_csv()
        # Lấy chỉ mục các video được chọn trong danh sách hiển thị
        selected_indices = self.lst_videos.curselection()
        if not selected_indices: # Kiểm tra nếu không có video được chọn
            msb.showwarning("Warning", "Please select at least one video to add to playlist.")
            return
        # Lặp qua các chỉ mục video được chọn
        for idx in selected_indices:
            # Lấy chỉ số của video trong danh sách hiển thị
            video_index = int(idx)
            # Lấy ID của video từ chỉ số
            video_id = list(library.keys())[video_index]
            # Kiểm tra video đã tồn tại trong danh sách phát chưa
            if video_id not in self.selected_videos: # Chưa tồn tại
                self.selected_videos.append(video_id) # Thêm vào danh sách phát
                self.lst_your_videos.insert(tk.END, f"{video_id} : {library[video_id].name} - {library[video_id].director}") # Hiện thị ra
            else: # Đã tồn tại
                msb.showinfo("Info", f"{library[video_id].name} - {library[video_id].director} is already in the playlist.")   
                
                        
    # Xử lý sự kiện khi nút "Run" được nhấn  
    def run_playlist(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Run button was clicked!")
        load_library_from_csv()
        # Lấy chỉ mục các video được chọn trong danh sách hiển thị
        selected_indices = self.lst_your_videos.curselection()
        if not selected_indices: # Kiểm tra nếu không có video được chọn
            msb.showwarning("Warning", "Please select a video to play!")
            return
        # Khởi tạo một danh sách để lưu các video đã được phát
        played_videos = []
        # Lặp qua các chỉ mục của video được chọn trong danh sách phát của người dùng
        for idx in selected_indices:
            video_id = self.selected_videos[idx]  # Lấy video ID từ danh sách video được chọn dựa vào chỉ mục
            # Tăng số lượt phát của video trong thư viện thêm 1 lần
            library[video_id].play_count += 1
            # Thêm thông tin video vào danh sách lịch sử phát
            played_videos.append(f"{video_id} : {library[video_id].name} - {library[video_id].director}")
        # Lưu thay đổi vào thư viện
        save_library_to_csv(library)
        self.fill_videos() # Cập nhật lại danh sách video hiển thị
        # Hiển thị lịch sử phát trong lbl_play_history
        self.update_play_history(played_videos, append=True)  # Thêm vào lịch sử phát
        msb.showinfo("Success", "Selected videos played!")

        
    # Xử lý sự kiện khi nút "Remove" được nhấn 
    def remove_playlist(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Remove button was clicked!")
        # Lấy chỉ mục các video được chọn trong danh sách hiển thị
        selected_indices = self.lst_your_videos.curselection()
        if not selected_indices: # Kiểm tra nếu không có video được chọn
            msb.showwarning("Warning", "Please select at least one video to remove from the playlist.")
            return
        # Hiển thị cảnh báo trước khi xóa
        confirmation = msb.askokcancel("Confirmation", "Are you sure you want to remove the selected items from the playlist?")
        if confirmation:
            # Lặp qua các chỉ mục được chọn theo thứ tự ngược lại để đảm bảo rằng việc loại bỏ các mục không gây ra lỗi chỉ mục.
            for idx in selected_indices[::-1]:
                # Loại bỏ video khỏi danh sách phát hiển thị
                self.lst_your_videos.delete(idx)
                # Lấy video ID từ danh sách video được chọn dựa vào chỉ mục
                video_id = self.selected_videos.pop(idx)  # Loại bỏ phần tử tại chỉ mục idx từ self.selected_videos

            # Lưu thay đổi vào thư viện
            save_library_to_csv(library)
            
            # Cập nhật lại danh sách video hiển thị
            self.fill_videos()
            msb.showinfo("Remove Playlist", "Videos removed from the playlist successfully.")




    # Xử lý sự kiện khi nút "Reset" được nhấn 
    def reset_playlist(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Reset button was clicked!")
        # Hiển thị cảnh báo trước khi reset playlist
        confirmation = msb.askokcancel("Confirmation", "Are you sure you want to reset the playlist?")
        if confirmation:
            # Đặt lại playlist về trống
            self.lst_your_videos.delete(0, tk.END)
            self.selected_videos = []
            msb.showinfo("Playlist Reset", "Playlist reset successfully.")
        
        
    # Xử lý sự kiện khi nút "Search" được nhấn 
    def search_videos(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Search button was clicked!")
        # Xóa kết quả tìm kiếm trước đó trong danh sách hiển thị
        self.lbl_search_result.delete(0, tk.END)
        # Lấy thông tin về loại tìm kiếm và từ khóa tìm kiếm từ người dùng
        search_option = self.search_option.get()
        search_input = self.entry_search_input.get().strip().lower()
        if not search_input: # Nếu chưa nhập thông tin tìn kiếm
            msb.showwarning("Warning", "Please enter search keywords!")
            return
        # Khởi tạo danh sách chứa kết quả tìm kiếm
        found_videos = []
        # Duyệt thư viện
        for video_id, video_info in library.items():
            if search_option == "Name":
                match_condition = search_input in video_info.name.lower() # Từ khóa có 1 phần của thông tin, không phân biệt viết hoa hay thường
            elif search_option == "Director":
                match_condition = search_input in video_info.director.lower() # Từ khóa có 1 phần của thông tin, không phân biệt viết hoa hay thường
            elif search_option == "ID":
                match_condition = search_input == video_id
            # Thêm vào danh sách tìm kiếm nếu có kết quả
            if match_condition:
                found_videos.append(f"{video_id} : {video_info.name} - {video_info.director}")
        # Hiển thị kết quả
        if found_videos: # Nếu có thông tin tìm kiếm
            for video in found_videos:
                self.lbl_search_result.insert(tk.END, video)
        else: # Không có thông tin tìm kiếm
            self.lbl_search_result.insert(tk.END, "No matching videos were found!")


    # Xử lý sự kiện khi nút "Add" được nhấn 
    def add_selected_from_search(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Add button was clicked!")
        load_library_from_csv()
        # Xác định video đã chọn
        selected_videos = [self.lbl_search_result.get(idx) for idx in self.lbl_search_result.curselection()]
        if not selected_videos: # Nếu chưa chọn
            msb.showwarning("Warning", "Please select at least one video from the search list!")
            return
        # Kiểm tra xem video đã tồn tại trong danh sách phát chưa
        for video in selected_videos:
            video_id = video.split(' : ')[0] # Lấy ID của video
            if video_id not in self.selected_videos: # Nếu chưa
                self.selected_videos.append(video_id) # Thêm vào danh sách ID video
                self.lst_your_videos.insert(tk.END, video) # Hiển thị video
            else: # Nếu đã tồn tại
                msb.showinfo("Information", f"{video} already in the playlist!")

                
        
    # Phương thức cập nhật lịch sử phát
    def update_play_history(self, played_videos, append=True):
        load_library_from_csv()
        if not append: # Nếu append = False
            self.lbl_play_history.delete(0, tk.END) # Xóa tất cả các mục trong lịch sử phát
        # Lặp qua danh sách, hiện thị thông tin từng video
        for video in played_videos:
            self.lbl_play_history.insert(tk.END, video)


    # Xử lý sự kiện khi nút "Remove history" được nhấn 
    def remove_history(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Remove history button was clicked!")
        # Lấy chỉ mục các video được chọn trong danh sách hiển thị
        selected_indices = self.lbl_play_history.curselection()
        if not selected_indices: # Nếu chưa chọn mục cần xóa
            msb.showwarning("Warning", "Please select at least one video from the play history!")
            return
        # Lặp qua các chỉ số của các mục được chọn trong lịch sử phát từ cuối lên đầu
        for idx in selected_indices[::-1]:
            self.lbl_play_history.delete(idx)


    # Xử lý sự kiện khi nút "Remove all" được nhấn 
    def remove_history_all(self):
        # Cập nhật trạng thái
        self.status_lbl.configure(text="Remove all button was clicked!")
        self.lbl_play_history.delete(0, tk.END) # Xóa tất cả các mục từ 0 đến END


# Code dưới đây để thử nghiệm lớp CreateVideoList trong một cửa sổ tkinter

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Create Video List")
    app = CreateVideoList(window)
    window.mainloop()


