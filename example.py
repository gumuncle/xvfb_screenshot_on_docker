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
        self.browser.get('http://www.aozora.gr.jp/cards/000148/files/789_14547.html')
        self.assertIn('夏目漱石 吾輩は猫である', self.browser.title)
        self.browser.get_screenshot_as_file("/host/aozora_wagahai.png")

if __name__ == '__main__':
    unittest.main(verbosity=2)
