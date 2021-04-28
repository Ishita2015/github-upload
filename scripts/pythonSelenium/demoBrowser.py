from selenium import webdriver

# browser exposes on an exe file
# Through Selenium test, we need to invoke the exe file which will then invoke actual browser
#driver = webdriver.Chrome(executable_path="C:\\Users\\ishita_nigam\\IdeaProjects\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Users\\ishita_nigam\\IdeaProjects\\geckodriver.exe")
driver.maximize_window()
# get method to hit url on browser
driver.get("https://www.cerence.com/home")
driver.get("https://www.nuance.com/omni-channel-customer-engagement/voice-and-ivr/text-to-speech.html#!")
print(driver.title)
print(driver.current_url)
driver.get("https://www.cerence.com/about")
#driver.minimize_window()
driver.back()
driver.forward()
driver.refresh()
driver.quit()
