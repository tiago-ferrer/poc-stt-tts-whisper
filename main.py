from transcriber import Transcriber
from youtube_downloader import YouTubeDownloader

videos = [
    ("fiapDemo","https://www.youtube.com/watch?v=UC7WaqrIY2U")
]

downloader = YouTubeDownloader(videos)
downloader.download_videos()

for video in videos:
    name, url = video
    Transcriber().transcribe_audio_to_srt(audio_path=f'({name}.mp3)',output_file_path=f'({name}.txt)')
