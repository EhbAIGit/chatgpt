from openai import OpenAI
client = OpenAI()

audio_file= open("vandaagIsEenHeelMooieDag.m4a", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print (transcript)