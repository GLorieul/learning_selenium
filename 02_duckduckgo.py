
# This script submits a query to DuckDuckGo and plays a bit with it

# Heavily inspired by https://www.techbeamers.com/selenium-webdriver-python-tutorial/

import time
from selenium import webdriver

#driver = webdriver.Chrome()
#driver = webdriver.WebKitGTK()
driver = webdriver.Firefox()

print("Maximizing the window")
driver.maximize_window()

print("Loading the DuckDuckGo welcome page")
driver.get("https://duckduckgo.com/")

print("Submiting a query to DuckDuckGo")
searchField = driver.find_element_by_id("search_form_input_homepage")
#searchField = driver.find_element_by_name("q") #Also works
searchField.send_keys("Does that work?")
searchField.submit()

#Required otherwise no results are found
#because they haven't had the time to be displayed.
#Note: results seem to be displayed by javascript (?)
print("Waiting 5 seconds for the results to show…")
time.sleep(5)
resultsLinks = driver.find_elements_by_class_name("result__a")
nbResults = len(resultsLinks)
print(f"{nbResults} results displayed")

# Horrible XPath obtained using BugZilla's "Right click > Copy > Copy XPath"
print("Clicking on the \"More results\" button")
moreResultsButton = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[3]/div/div[1]/div[5]/div[11]/a")
moreResultsButton.click()

# A better XPath that will be a lot more robust to change:
# look for a button called "More results"
# However, in the case of DuckDuckGo, there is one "More results" button at
# the bottom of each page. Hence Selenium behaves as if there were several
# "More results" button existing, but only one visible.
print("Waiting 5 seconds for the results to show…")
time.sleep(5)
print("Clicking on the \"More results\" button")
moreResultsButton = driver.find_elements_by_xpath("//div[a='More results']/a")
for button in moreResultsButton:
    if button.is_displayed():
        button.click()
        break
#print("altMoreResultsButton = ", altMoreResultsButton)

print("Waiting 5 seconds for the results to show…")
time.sleep(5)
resultsLinks = driver.find_elements_by_class_name("result__a")
nbResults = len(resultsLinks)
print(f"{nbResults} results displayed")

print("Opening the first result")
resultsLinks[0].click()
print("Waiting 15 seconds for the page to load…")
time.sleep(15)

print("End of script reached, waiting 5 seconds before quiting driver…")
time.sleep(5)
print("Quiting driver now")
driver.quit()

