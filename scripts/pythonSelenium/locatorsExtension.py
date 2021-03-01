from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\ishita_nigam\\IdeaProjects\\chromedriver.exe')
driver.maximize_window()
driver.get('https://login.salesforce.com/')
driver.find_element_by_id('username').send_keys('Ishita')
driver.find_element_by_css_selector('#password').send_keys('demo')
driver.find_element_by_xpath("//input[@name='rememberUn']").click()
# driver.find_element_by_name('Login').click()
driver.find_element_by_link_text('Forgot Your Password?').click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
driver.find_element_by_xpath("//form[@name='login']/div[1]/label")
