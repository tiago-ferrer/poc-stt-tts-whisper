from pydub import AudioSegment
import numpy as np
from whisperspeech.pipeline import Pipeline


# pipe = Pipeline(s2a_ref='collabora/whisperspeech:s2a-q4-small-en+pl.model')
# pipe = Pipeline(s2a_ref='collabora/whisperspeech:s2a-q4-tiny-en+pl.model')
pipe = Pipeline(s2a_ref='collabora/whisperspeech:s2a-q4-tiny-en+pl.model')

audio_tensor = pipe.generate("""
 Porque a primeira pergunta que surge em quando você fala de programação é qual é a melhor linguagem?
""", speaker="./testevoice.wav", lang="pt")

# generate uses CUDA if available; therefore, it's necessary to move to CPU before converting to NumPy array
audio_np = (audio_tensor.cpu().numpy() * 32767).astype(np.int16)

if len(audio_np.shape) == 1:
    audio_np = np.expand_dims(audio_np, axis=0)
else:
    audio_np = audio_np.T

print("Array shape:", audio_np.shape)
print("Array dtype:", audio_np.dtype)

try:
    audio_segment = AudioSegment(
        audio_np.tobytes(), 
        frame_rate=24000, 
        sample_width=2, 
        channels=1
    )
    audio_segment.export('output_audio.wav', format='wav')
    print("Audio file generated: output_audio.wav")
except Exception as e:
    print(f"Error writing audio file: {e}")