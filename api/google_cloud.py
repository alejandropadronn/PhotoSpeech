import io 
from google.cloud import vision

class VisualRecognition(object):
    def __init__(self):
        self.client = vision.Client()

    # Prepare image to be classified
    def load_image(self, file):
        # Loads the image into memory
        with io.open(file, 'rb') as image_file:
            content = image_file.read()
            self.image = self.client.image(content=content)
    
    # Get the labels for an image
    def labels(self):
        return self.image.detect_labels()
