from pytube import YouTube
from moviepy.editor import *
import os

class YouTubeDownloader:
    def __init__(self, videos):
        self.videos = videos

    def download_videos(self):
        for video in self.videos:
            name, url = video
            if url:
                print(f"Current directory: {os.getcwd()}")
                # Download the YouTube video
                youtube = YouTube(url)
                video = youtube.streams.first()
                video.download(filename="temp_video.mp4")

                print(f"Video downloaded: {os.path.exists('temp_video.mp4')}")
                print(f"Current directory: {os.getcwd()}")

                # Extract audio and save as MP3
                video_clip = VideoFileClip('temp_video.mp4')
                audio_clip = video_clip.audio
                audio_file_path = f'{name}.mp3'
                audio_clip.write_audiofile(audio_file_path)

                # Close the clips
                video_clip.close()
                audio_clip.close()

                print(f'The audio was saved as: {audio_file_path}')