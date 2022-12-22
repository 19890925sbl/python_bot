from selenium import webdriver
driver=webdriver.Chrome()
url="http://github.com"
driver.get(url)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")
url="https://github.com/19890925sbl"
driver.get(url)
print(driver.title)
if "19890925sbl" in driver.title:
    driver.save_screenshot("github-19890925sbl.png")
time.sleep(2)
driver.back()
driver.close()