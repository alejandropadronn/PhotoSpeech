import os

from gtts import gTTS

class TTS(object):

    def __init__(self, path):
        self.path = path

    def play(self, text, language, slow=False):
          tts = gTTS(text=text, lang=language, slow=slow)
          tts.save(self.path)
          os.system('mpg321 '+ self.path)
          os.remove(self.path)
