import secrets
from api.visual_recog import VisualRecog
from tts.tts import TTS
from camera.camera import Camera

if __name__ == '__main__':
    # Create the objects we need 
    vr = VisualRecog(secrets.IBM_API_KEY)
    camera = Camera()
    tts = TTS()
    tts.play('en', 'test', 'test.mp3')
    