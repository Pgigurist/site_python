import os, sys
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processor import ResizeToFit, Adjust, ResizeToFill

class Jobseeker(models.Model):
    def getfile_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join("images", filename)

def getImageByPath(path):
    im = Image.open(path)
    print("IMAGE correct")
