import os

from barcode.writer import ImageWriter
from barcode import Code128
from loguru import logger

from configs.config import BASE_DIR


def parse(code: str):
    code128 = Code128(code, writer=ImageWriter())
    fullname = code128.save(filename=f"{code}", options={"module_width": 0.3})
    logger.info(f"{code}.png parse success.")
    path = os.path.join(BASE_DIR, fullname)
    return path
