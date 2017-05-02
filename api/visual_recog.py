from watson_developer_cloud import VisualRecognitionV3
from os.path import join, dirname
from pprint import pprint

class VisualRecog(object):
    def __init__(self, api_key):
        self.visual_rec = VisualRecognitionV3(VisualRecognitionV3.latest_version, api_key=api_key)

    def classify(self, file_location):
        with open(join(dirname(__file__), file_location), 'rb') as image_file:
            img = self.visual_rec.classify(images_file=image_file)
            pprint(img)
