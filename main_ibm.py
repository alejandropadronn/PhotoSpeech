import secrets
from api.ibm import VisualRecog
# from tts.tts import TTS
from camera.camera import Camera
# from espeak import espeak

if __name__ == '__main__':
    # Create the objects we need 
    vr = VisualRecog(secrets.IBM_API_KEY)
    camera = Camera()
    # tts = TTS()

    # Wait on photo
    photo_path = "/home/pi/Desktop/PhotoSpeech/photo.jpeg"
    camera.start(photo_path)
    # Classify photo
    classfied = vr.classify(photo_path)
    pprint(classfied)
    # espeak.synth(classfied)
    # Play the text
    # tts.play('en', , 'test.mp3')
    