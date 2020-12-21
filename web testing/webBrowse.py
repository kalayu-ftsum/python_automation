from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

messageHello=driver.find_element_by_xpath('//*[@id="user-message"]')
messageHello.send_keys("Helo world")

showbutton=driver.find_element_by_xpath('//*[@id="get-input"]/button')
showbutton.click()