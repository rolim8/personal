from pytube import YouTube

# Where it will save
SAVE_PATH = "C:/Users/Rolim/Videos"

# link of the video for download
link = "https://www.youtube.com/watch?v=2fGWX-jJyVY"

try:
    yt = YouTube(link)
except:
    print("Connection Error")

# download in MP4 extension
mp4files = yt.filter('mp4')

# name of the file
yt.set_filename('Video Test')

# video with extension and resolution
d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
try:
    # downloading the video
    d_video.download(SAVE_PATH)
except:
    print("******************")
    print("**     Ops!     **")
    print("There is any error")
    print("******************")

print('Successfully Downloaded!')