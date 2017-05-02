from gtts import gTTS
from time import sleep
import os
import pyglet

class TTS(object):
    
    def play(self, language, text, file_path):
        gtts = gTTS(text=text, lang=language) # set Text,Language, and speed settings here (can be set to speak slower)
        filename = file_path # temporary storage locaction for the .mp3 file
        gtts.save(filename) # saves the file with the indicated name, in our case 'filename' is the name we've chosen to give our file.

        music = pyglet.media.load(filename, streaming=False) # load the file and it's local AKA not streaming
        music.play() # pretty self explanitory although this will play the indicated .mp3 with the indicated Text
        sleep(music.duration) # will stop playing and go to sleep after music's .mp3 file has finished
        os.remove(filename) # will remove the indicated file, from your computer since we only wanted it there for a moment anyway.
