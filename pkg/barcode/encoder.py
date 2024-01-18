import base64

from PIL import Image


def encode(path: str):
    with open(path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read())
        return base64_image.decode("utf-8")
