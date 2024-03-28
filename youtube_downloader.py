from pytube import YouTube
from moviepy.editor import *
import os

TEMP_VIDEO_MP4 = "temp_video.mp4"


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
                video.download(filename=TEMP_VIDEO_MP4)

                # Extract audio and save as MP3
                video_clip = VideoFileClip(TEMP_VIDEO_MP4)
                audio_clip = video_clip.audio
                audio_file_path = f'{name}.mp3'
                audio_clip.write_audiofile(audio_file_path)

                # Close the clips
                video_clip.close()
                audio_clip.close()

                os.remove(TEMP_VIDEO_MP4)