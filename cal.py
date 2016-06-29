import unittest

from selenium import webdriver
from xvfbwrapper import Xvfb


class TestPages(unittest.TestCase):

    def setUp(self):
        self.xvfb = Xvfb(width=1366, height=786)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)


    def testNatsumeSouseki(self):
        self.browser.get('http://counting.hatelabo.jp/count/')
        self.browser.get_screenshot_as_file("/host/cal.png")


        from PIL import Image
        img = Image.open("/host/cal.png")
        box = (199, 63, 199+514, 63+265)
        area = img.crop(box)
        area.save("/host/rim", "png")

if __name__ == '__main__':
    unittest.main(verbosity=2)
