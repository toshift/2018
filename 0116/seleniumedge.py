# pip install selenium
# Microsoft webdriver : Release 16299

from selenium import webdriver
from time import sleep

driver =  webdriver.Edge(executable_path='webdriver/MicrosoftWebDriver.exe')
sleep(5)
driver.close()
exit(0)