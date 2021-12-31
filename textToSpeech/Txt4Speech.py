from gtts import gTTS

import os

mytext = 'Hello World'

language = 'pt'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("eae.mp3")
