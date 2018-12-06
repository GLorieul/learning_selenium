
# This script computes the sum of two numbers using calculator.net

# Heavily inspired by https://www.tutorialspoint.com/selenium/selenium_webdriver.htm


def composeNumber(number):
    nbStr = str(number)
    for digit in nbStr:
        command = 'r(' + digit + ')'
        xPath = "//span[@onclick=\"" + command + "\"]"
        button = driver.find_element_by_xpath(xPath)
        button.click()
        time.sleep(0.3)

import time
from selenium import webdriver


# PARSE INPUT
import argparse
description = ( 'Add two numbers: A + B'
              + 'Example input: python3 03_calculator.py 2145 35602')
parser = argparse.ArgumentParser(description=description)
parser.add_argument('numberA', type=int, nargs=1, help='Number A')
parser.add_argument('numberB', type=int, nargs=1, help='Number B')
args = parser.parse_args()
a =  args.numberA[0]
b =  args.numberB[0]


#driver = webdriver.Chrome()
#driver = webdriver.WebKitGTK()
driver = webdriver.Firefox()

print("Maximizing the window")
driver.maximize_window()

print("Loading the calculator page")
driver.get("https://www.calculator.net/")

print("Composing number A")
composeNumber(a)

print("Pressing '+'")
button = driver.find_element_by_xpath("//span[@onclick=\"r('+')\"]")
button.click()
time.sleep(0.3)

print("Composing number B")
composeNumber(b)

print("Pressing '='")
button = driver.find_element_by_xpath("//span[@onclick=\"r('=')\"]")
button.click()
time.sleep(0.3)

print("Reading result:")
result = driver.find_element_by_id("sciOutPut")
print(f"\t{a} + {b} = {result.text}")

print("End of script reached, waiting 5 seconds before quiting driver…")
time.sleep(5)
print("Quiting driver now")
driver.quit()

