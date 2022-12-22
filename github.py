from githubUseInfo import username,password
from selenium import webdriver
import time
class Github:
             def__init__(self,username,password):
             self.browser=webdriver.Chrome()
             self.username=username
             self.password=password
             def signIn(self):
                self.browser.get("https://github.com/login")
                time.sleep(2)