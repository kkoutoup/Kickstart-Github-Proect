from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def github_init():
  print("\n=> Launching browser...")
  browser = webdriver.Firefox()
  browser.get("https://stackoverflow.com/questions/31147660/importerror-no-module-named-selenium")