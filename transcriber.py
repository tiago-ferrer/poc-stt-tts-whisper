from googletrans import Translator
from TTS.api import TTS
import torch
import whisper

class Transcriber:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
        self.translator = Translator()

    def transcribe_audio_to_srt(self, audio_path, model_name="tiny", output_file_path="output.txt"):
        model = whisper.load_model(model_name)
        result = model.transcribe(audio_path)
        texts = []

        print(self.device)

        with open(output_file_path, "w") as srt_file:
            for i, segment in enumerate(result["segments"], start=1):
                start_time = self.format_timestamp(segment["start"])
                end_time = self.format_timestamp(segment["end"])

                srt_file.write(f"{i}\n")
                srt_file.write(f"{start_time} --> {end_time}\n")
                srt_file.write(f"{segment['text']}\n")
                srt_file.write("\n")
                t = segment['text'].replace(".","")
                print(t)

    def format_timestamp(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = (seconds - int(seconds)) * 1000
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds):03}"