from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\ishita_nigam\\IdeaProjects\\chromedriver.exe")
driver.maximize_window()
driver.get('http://gh-srvapp04/murmur/#/overview')

#driver.find_element_by_name('name').send_keys('Ishita')
driver.find_element_by_css_selector("input[name = 'name']").send_keys('Ishita')
driver.find_element_by_name('email').send_keys('ishitademo@gmail.com')
driver.find_element_by_id('exampleCheck1').click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@id='inlineRadio2']").click()
find = driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name('alert-success').text

print(message)

