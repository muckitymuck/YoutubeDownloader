#from pytube import YouTube
import pytube

SAVE_PATH = 'C:/ Place to save the video'
try:
    link = "https://www.youtube.com/URL for YT Video"
    yt = pytube.YouTube(link)
except:
    print("Connection Error")
stream = yt.streams.first()
try:
    stream.download(SAVE_PATH)
except:
    print("Error Occurred")

print("Task Complete")





