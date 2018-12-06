# https://pythonspot.com/selenium-click-button/
# https://www.techbeamers.com/handle-alert-popup-selenium-python/

# Python with selenium module - you need to have silenium and chromedriver for this to work'
# Opens chrome browser, clicks button, then clicks "ok" on alert that pops up - Ponzi

from selenium import webdriver
import time

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('http://www.echoecho.com/htmlforms12.htm')

submit_button = driver.find_elements_by_xpath("//input[@name='shorttext' and @value='Hit Me!']")[0]
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

driver.close
