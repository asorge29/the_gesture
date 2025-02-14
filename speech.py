from gtts import gTTS
tts = gTTS("", lang="en", tld="com.au")
tts.save("aus.mp3")