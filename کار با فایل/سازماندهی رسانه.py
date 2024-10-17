import os
import sys
import time
from datetime import datetime
import re

# Data:
photo_extentions = [".jpg", ".jpeg", ".png"]
video_extentions = [".mp4", ".avi", ".3gp", ".mpeg", ".mkv", ".wmv", ".mov"]

if __name__ == '__main__':
    src_folder = sys.argv[1]
    dst_folder = sys.argv[2]
    all_dir = list(os.walk(src_folder))
    all_files = list()

    # Collect all files with their modification year
    for address, _, files in all_dir:
        for f in files:
            file_address = os.path.join(address, f)
            # Use fromtimestamp to directly convert to a datetime object
            mtime = datetime.fromtimestamp(os.path.getmtime(file_address))
            year = str(mtime.year)
            all_files.append((file_address, year))

    # Process and copy files
    for address, year in all_files:
        curr_ads = os.path.join(dst_folder, year)
        
        # Check if it's a video file
        if any(address.lower().endswith(v) for v in video_extentions):
            video_name = os.path.basename(address)
            video_folder = os.path.join(curr_ads, "videos")
            os.makedirs(video_folder, exist_ok=True)
            video_file = os.path.join(video_folder, video_name)
            
            with open(address, "rb") as v_file:
                data = v_file.read()
                with open(video_file, "wb") as new_file:
                    new_file.write(data)

        # Check if it's a photo file
        elif any(address.lower().endswith(p) for p in photo_extentions):
            photo_name = os.path.basename(address)
            photo_folder = os.path.join(curr_ads, "photos")
            os.makedirs(photo_folder, exist_ok=True)
            photo_file = os.path.join(photo_folder, photo_name)

            with open(address, "rb") as p_file:
                data = p_file.read()
                with open(photo_file, "wb") as new_file:
                    new_file.write(data)

    print("File copy completed.")



import os
# import sys
# import time
# from datetime import datetime
# import re

# # data:
# photo_extentions = [".jpg", ".jpeg", ".png"]
# video_extentions = [".mp4", ".avi", ".3gp", ".mpeg", ".mkv", ".wmv", ".mov"]
# date_format = "%a %b %d %H:%M:%S %Y"


# if __name__ == '__main__':
#     # src_folder = sys.argv[1]
#     # dst_folder = sys.argv[2]
#     src_folder = "C:\\Users\\QOM_ASUS\\Desktop\\searcher"
#     dst_folder = "C:\\Users\\QOM_ASUS\\Desktop\\dst_folder"
#     all_dir = list(os.walk(src_folder))
#     all_files = list()
#     for address, _, files in all_dir:
#         for f in files:
#             file_address = address + os.sep + f
#             mtime = datetime.fromtimestamp(os.path.getmtime(file_address))
#             year = str(mtime.year)
#             # mtime_seconds = time.ctime(os.path.getmtime(file_address))
#             # year = str(datetime.strptime(mtime_seconds, date_format).year)
#             all_files.append((file_address, year))

#     for address, year in all_files:
#         curr_ads = os.path.join(dst_folder, year)
#         for v in video_extentions:
#             if re.search(f".*{v}$", address.lower()):
#                 # video_name = re.search(r"[^\\]+$", address).group()
#                 video_name = os.path.basename(address)
#                 video_folder = os.path.join(curr_ads, "videos")
#                 os.makedirs(video_folder, exist_ok=True)
#                 with open(address, "rb") as v_file:
#                     data = v_file.read()
#                     video_file = os.path.join(video_folder, video_name)
#                     with open(video_file, "wb") as new_file:
#                         new_file.write(data)

#     for address, year in all_files:
#         curr_ads = os.path.join(dst_folder, year)
#         for p in photo_extentions:
#             if re.search(f".*{p}$", address.lower()):
#                 # photo_name = re.search(r"[^\\]+$", address).group()
#                 photo_name = os.path.basename(address)
#                 photo_folder = os.path.join(curr_ads, "photos")
#                 os.makedirs(photo_folder, exist_ok=True)
#                 with open(address, "rb") as p_file:
#                     data = p_file.read()
#                     photo_file = os.path.join(photo_folder, photo_name)
#                     with open(photo_file, "wb") as new_file:
#                         new_file.write(data)
