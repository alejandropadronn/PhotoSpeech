from picamera import PiCamera
from time import sleep
from gpiozero import Button

class Camera(object):
    def __init__(self):
        self.button = Button(17)
        self.camera = PiCamera()
    
    def start_camera(self, save_to_file):
        self.button.wait_for_press()
        self.camera.capture(save_to_file)
