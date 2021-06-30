from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://192.168.11.103')
driver.save_screenshot('screen_103.png')
