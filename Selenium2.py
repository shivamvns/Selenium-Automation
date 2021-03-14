#importing necessary libraries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#set the path to the chromedriver is located
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

#this is a inbuilt function for handling lazyness of the websites
driver.implicitly_wait(6)
#feeding the desired section of he page for activating actiom
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for  i  in range(1,-1,-1)]




#performing action
actions = ActionChains(driver)
actions.click(cookie)


# giving our actionchain a max limit of 5000 clicks
for i in range(5000):
	actions.perform()
	count = cookie_count.text
	print(count)
	