# https://pythonspot.com/selenium-click-button/
# https://www.techbeamers.com/handle-alert-popup-selenium-python/

# Python with selenium module - you need to have silenium and chromedriver for this to work'
# Uses local html file, for testing selenium - Ponzi

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('file:///home/mthomas/python_progs/selenium_playground/html_testit/seltest.html')

time.sleep(2)
print("click on radio button")
# click radio button
python_button = driver.find_elements_by_xpath("//input[@name='bugs' and @value='Wasp']")[0]
python_button.click()

time.sleep(1)

submit_button = driver.find_elements_by_xpath("//input[@name='a_box' and @value='Alert Box']")[0]
submit_button.click()

time.sleep(3)

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg = obj.text
print("Alert shows following message: "+ msg )

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

print("Clicked on the OK Button in the Alert Window")

time.sleep(2)

print("Writing to text area")

text_area = driver.find_element_by_id('daText')
text_area.send_keys("This text is sent using Python code.")

time.sleep(3)

print("selecting from dropdown")

time.sleep(2)

obj = Select(driver.find_element_by_id("daColors"))
obj.select_by_index(2)

time.sleep(3)

print("click on web link to Ponzi's python site")

driver.find_element(By.LINK_TEXT, "PonzisPython").click();

time.sleep(4)

# Closes web page
driver.close()
