import os
import PIL.Image as Image
import io
from base64 import encodebytes, b64decode
import numpy

def imageToBytes(path):
    pilImg = Image.open(path, mode='r')  # reads the PIL image
    bytearr = io.BytesIO()
    pilImg.save(bytearr, format='JPEG')  # convert the PIL image to byte array
    encodedImg = encodebytes(bytearr.getvalue()).decode('ascii')  # encode as base64
    return encodedImg


def bytesToImage(bytearr, path):
    imgdata = b64decode(bytearr)
    with open(path, 'wb') as f:
        f.write(imgdata)


def encodeBytes(bytearr):
    return encodebytes(bytearr.getvalue()).decode('ascii')