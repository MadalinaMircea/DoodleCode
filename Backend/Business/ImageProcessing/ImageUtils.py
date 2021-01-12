import PIL.Image as Image
import io
from base64 import encodebytes, b64decode


class ImageUtils:
    def image_to_bytes(self, path):
        pilImg = Image.open(path, mode='r')  # reads the PIL image
        bytearr = io.BytesIO()
        pilImg.save(bytearr, format='JPEG')  # convert the PIL image to byte array
        encodedImg = encodebytes(bytearr.getvalue()).decode('ascii')  # encode as base64
        return encodedImg

    def bytes_to_image(self, bytearr, path):
        imgdata = b64decode(bytearr)
        with open(path, 'wb') as f:
            f.write(imgdata)

    def encode_bytes(self, bytearr):
        return encodebytes(bytearr.getvalue()).decode('ascii')
