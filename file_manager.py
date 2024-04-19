import csv

def save_library_to_csv(library):
    with open('videos.csv', 'w', newline='') as f: # Mở CSV
        csvwriter = csv.writer(f) # Tạo đối tượng
        csvwriter.writerow(['ID', 'Name', 'Director', 'Rating', 'Plays']) # Ghi 1 hàng vào CSV
        # Lặp qua từng mục
        for video_id, video_info in library.items():
            csvwriter.writerow([video_id, video_info.name, video_info.director, video_info.rating, video_info.play_count]) # Ghi một hàng vào CSV cho mỗi video
