from instagramUserInfo import email,password
from selenium import webdriver
import time

class Instagram:
    def__init__(self,email,password)
    self.browser=webdriver.Chrome()
    self.email=email
    self.password=password

    def signIn(self):
        self.browser.get("https://https://www.instagram.com/explore/")
        time.sleep(4)
emailInput=self.browser.find_element_by_xpath("//*[@id='mount_0_0_SH']/div/div/div/div[1]/div/div/div/div[1]/div[1]")
passwordInput=self.browser.find_element_by_xpath("")