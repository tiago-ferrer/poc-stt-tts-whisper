import os

from gemini import Gemini
from transcriber import Transcriber
from youtube_downloader import YouTubeDownloader

videos = [
    ("git","https://www.youtube.com/watch?v=DqTITcMq68k")
]

downloader = YouTubeDownloader(videos)
downloader.download_videos()

# Usage
gemini = Gemini(os.getenv('GOOGLE_API_KEY'), 'gemini-pro')

for video in videos:
    name, url = video
    Transcriber().transcribe_audio_to_srt(audio_path=f'{name}.mp3',output_file_path=f'{name}.txt')
    gemini.generateAbstract(f'{name}.txt', f'{name}-resumo.txt')
    os.remove(f'{name}.mp3')
    os.remove(f'{name}.txt')
