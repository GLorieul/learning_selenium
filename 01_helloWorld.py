
# This program just starts an instance of the browser, and closes it.
# This is helpful to make sure there are no issues in accessing the selenium
# package as well as starting the WebDriver

import time
from selenium import webdriver

#driver = webdriver.Chrome()
#driver = webdriver.WebKitGTK()
driver = webdriver.Firefox()
time.sleep(5)
driver.quit()


