
from appium import webdriver
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

class MobileScreen:
    def __init__(self, driver: webdriver.Remote) -> None:
        self.driver = driver
    def get_screenshot_numpy(self) -> np.ndarray:
        bytes = self.driver.get_screenshot_as_png()
        img = cv2.imdecode(np.frombuffer(bytes, np.uint8), -1)
        return img

    def save_screenshot_as_bmpfile(self) -> None:
        bytes = self.driver.get_screenshot_as_png()
        img = Image.open(BytesIO(bytes))
        img.save("screenshot.bmp")
        