import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://pythonbasics.org'

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
print(S('Height'))
print(S('Width'))
driver.set_window_size(1920,1080) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()