# Importing the library
from gtts import gTTS
import os

# Providing the text
input_text = "Heloo this is Raul here,project 001 day 1 of learning and explorating python programming language"

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# Playing the file
os.system("start demo.mp3")