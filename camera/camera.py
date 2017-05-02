from picamera import PiCamera
from time import sleep
from gpiozero import Button

class Camera(object):
    def __init__(self):
        self.button = Button(17)
        self.camera = PiCamera()

    def start(self, save_to_file):
        print('Ready to take Photo press button...')
        self.button.wait_for_press()
        print('Button pressed, taking photo!')
        self.camera.capture(save_to_file)
