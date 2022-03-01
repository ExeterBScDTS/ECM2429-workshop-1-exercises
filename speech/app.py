from record import record, speech_to_text

record("test.wav")
audio_data = open("test.wav", "rb").read()

print(len(audio_data))

response = speech_to_text(audio_data)

print(response)
print(response.content)