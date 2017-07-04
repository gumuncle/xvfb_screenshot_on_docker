import unittest

from selenium import webdriver
from xvfbwrapper import Xvfb


xvfb = Xvfb(width=1366, height=786)
#self.addCleanup(self.xvfb.stop)
xvfb.start()
browser = webdriver.Firefox()

browser.get('http://www.tenki.jp/forecast/3/16/4410/13104-daily.html')
browser.get_screenshot_as_file("/host/cal.png")
e = browser.find_element_by_id("townWeatherBox")
h = e.size["height"]
w = e.size["width"]

x1 = e.location["x"]
y1 = e.location["y"]
print (x1, y1, w, h)

from PIL import Image
img = Image.open("/host/cal.png")
box = (x1, y1, x1+w, y1+h)
area = img.crop(box)
area.save("/host/rim", "png")
browser.quit()
