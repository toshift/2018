# pip install selenium
# Microsoft webdriver : Release 16299

from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Edge(executable_path='webdriver/MicrosoftWebDriver.exe')
    sleep(5)
except:
    pass
finally:
    if driver:
        driver.close()
exit(0)