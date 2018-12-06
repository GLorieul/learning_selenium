
# Learned from http://www.marinamele.com/selenium-tutorial-web-scraping-with-selenium-and-python

import time
from selenium import webdriver

#driver = webdriver.Chrome()
driver = webdriver.WebKitGTK()
#driver = webdriver.Firefox()
time.sleep(5)
driver.quit()

