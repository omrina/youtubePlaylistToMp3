import sys
from pathlib import Path
from pytube import Playlist
from moviepy.editor import *


def ensure_url_arg():
    if len(sys.argv) != 2:
        print('need a playlist url as 2nd argument')
        exit(1)


# ensureUrlArg()
# playlist_url = sys.argv[1]

mp3_output_folder = './mp3_songs'
playlist_url = 'https://www.youtube.com/playlist?list=PLAv3wwZw7pE2-CvBZZUe2sCu0p50dPUCW'
Path(mp3_output_folder).mkdir(parents=True, exist_ok=True)

playlist = Playlist(playlist_url)
print(F'downloading: {playlist.title}')


for video in playlist.videos:
    print(F'downloading: {video.title}')
    video.streams.filter(only_audio=True).first().download(output_path=mp3_output_folder, filename=F"{video.title}.mp3")


'''
1 - pip uninstall -y numpy
2 - pip uninstall -y setuptools
3 - pip install setuptools
4 - pip install numpy
'''