import whisper
import subprocess
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# def convert_video_to_mp3(input_video_path, output_audio_path, speed=1.0, bitrate="32k"):
#     # Monta o comando FFmpeg
#     ffmpeg_command = [
#         'ffmpeg',
#         '-i', input_video_path,
#         '-filter:a', f'atempo={speed},asetrate=44100*{speed}',
#         '-ab', bitrate,
#         output_audio_path
#     ]
#     # Executa o comando
#     subprocess.run(ffmpeg_command, check=True)
#     print(f"Áudio extraído e convertido para MP3: {output_audio_path}")
# def transcribe_audio_with_timestamps(audio_path, model_name="medium"):
#     # Carrega o modelo do Whisper baseado no nome especificado
#     model = whisper.load_model(model_name)
#     # Realiza a transcrição com detalhamento dos segmentos
#     result = model.transcribe(audio_path, verbose=False)
#     translator = Translator()
   
    
#     segments_with_timestamps = []
#     for segment in result["segments"]:
#         start_time = segment["start"]
#         end_time = segment["end"]
#         text = segment["text"]
#         translated_text = translator.translate(text, src='en', dest='pt')
#         segments_with_timestamps.append(f"{start_time} - {end_time}: {translated_text.text}")
    
#     return segments_with_timestamps

# def save_transcription(segments_with_timestamps, file_path="transcription_with_timestamps.txt"):
#     # Salva a transcrição com timestamps em um arquivo
#     with open(file_path, "w") as file:
#         for segment in segments_with_timestamps:
#             file.write(segment + "\n")
#     print(f"Transcrição salva em: {file_path}")


def transcribe_audio_to_srt(audio_path, model_name="tiny", output_file_path="output.txt"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    translator = Translator()
    texts = []

    print(device)
    
    with open(output_file_path, "w") as srt_file:
        for i, segment in enumerate(result["segments"], start=1):
            # Converte os tempos de início e fim para o formato SRT
            start_time = format_timestamp(segment["start"])
            end_time = format_timestamp(segment["end"])
            
            # Escreve o índice do segmento
            srt_file.write(f"{i}\n")
            # Escreve os tempos de início e fim
            srt_file.write(f"{start_time} --> {end_time}\n")
            # Escreve o texto do segmento
            # translated_text = translator.translate(, src='en', dest='pt')
            srt_file.write(f"{segment['text']}\n")
            # Escreve uma linha em branco após cada segmento
            srt_file.write("\n")
            t = segment['text'].replace(".","")
            print(t)
            tts.tts_to_file(text=t, speaker_wav="./testevoice.wav", language="pt", file_path=f"{i}.wav") 

    #tts.tts_to_file(text="".join(texts).replace(".", ""), speaker_wav="./testevoice.wav", language="pt", file_path="teste.wav")        
           
def format_timestamp(seconds):
    """Converte segundos para o formato de tempo SRT (HH:MM:SS,MS)"""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = (seconds - int(seconds)) * 1000
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds):03}"



# Exemplo de uso da função
# convert_video_to_mp3('teste2.mp4', 'output_audio.mp3')

# Transcreve o áudio, incluindo os tempos das falas
# result = transcribe_audio_with_timestamps("output_audio.mp3")



# Salva a transcrição com os tempos das falas
# save_transcription(result)

transcribe_audio_to_srt("teste.mp3")