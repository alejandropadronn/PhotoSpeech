import os

from api.google_cloud import VisualRecognition
from camera.camera import Camera

if __name__ == '__main__':
    # Prepare objects
    vr = VisualRecognition()
    camera = Camera()

    photo_path = '/home/pi/Desktop/PhotoSpeech/photo.jpg'
    camera.start(photo_path)

    # The name of the image file
    file = os.path.join(os.path.dirname(__file__), photo_path)
    # Prepare image for classification
    vr.load_image(file)
    # Get labels
    labels = vr.labels()
    for label in labels:
        print(label.description)