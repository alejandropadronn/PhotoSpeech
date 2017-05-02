import secrets
from api.visual_recog import VisualRecog
# from tts.tts import TTS
from camera.camera import Camera

if __name__ == '__main__':
    # Create the objects we need 
    vr = VisualRecog(secrets.IBM_API_KEY)
    camera = Camera()
    photo_path = "test.jpg"
    camera.start(photo_path)
    vr.classify(photo_path)
    # tts = TTS()
    # tts.play('en', 'test', 'test.mp3')
    