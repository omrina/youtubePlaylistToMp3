from pathlib import Path
from pytube import Playlist
from moviepy.editor import *
import string
import random

def downloadFile(title):
    video.streams.get_highest_resolution().download(output_path=mp4_output_folder, filename=f"{title}.mp4")
    videoClip = VideoFileClip(os.path.join(mp4_output_folder, f"{title}.mp4"))
    videoClip.audio.write_audiofile(os.path.join(mp3_output_folder, f"{title}.mp3"))

def generateTitle():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

playlist_url = "https://youtube.com/playlist?list=PLehZkrctaCJdOpWk3fgbrw-5M1mPUVoen"

mp3_output_folder = r"C:\Users\cgc\PycharmProjects\DiscBurn\mp3_songs_tuna_and_nechi"
mp4_output_folder = r"C:\Users\cgc\PycharmProjects\DiscBurn\mp4_videos_tuna_and_nechi"
Path(mp3_output_folder).mkdir(parents=True, exist_ok=True)

Path(mp4_output_folder).mkdir(parents=True, exist_ok=True)
playlist = Playlist(playlist_url)

print('downloading:', playlist.title)

for video in playlist.videos:
    print('downloading:', video.title)
    try:
        downloadFile(generateTitle())
    except Exception as e:
        print(e)
        # try:
        #     title = fixTitle()
        #     print('GENERATED', title)
        #     downloadFile(title)
        # except:
        #     print(video.title, "failed to download")