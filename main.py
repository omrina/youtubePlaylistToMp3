import sys
from pathlib import Path
from pytube import Playlist
from moviepy.editor import *


'''set to True when using this script through cmd/bash'''
is_run_with_cmd = False


def ensure_url_arg():
    if len(sys.argv) != 2:
        print('need a playlist url as 2nd argument')
        exit(1)


if is_run_with_cmd:
    ensure_url_arg()
    playlist_url = sys.argv[1]
else:
    playlist_url = 'https://www.youtube.com/watch?v=OJPLBUz3YVs&list=PLJJaZUDfc5LWYyV0T5i99Ef45UxVf8bcr'
    
mp3_output_folder = './mp3_songs'
Path(mp3_output_folder).mkdir(parents=True, exist_ok=True)

playlist = Playlist(playlist_url)
print(F'downloading: {playlist.title}')


for video in playlist.videos:
    print(F'downloading: {video.title}')
    video.streams.filter(only_audio=True).first().download(output_path=mp3_output_folder, filename=F"{video.title}.mp3")
