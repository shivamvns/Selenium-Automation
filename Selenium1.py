#import the selenium library

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#set the path to the chromedriver is located
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#giving our desired url from scrapping
driver.get("https://techwithtim.net")

#Showing the title of the web page which we are scrapping
print(driver.title)

#Automate our chrome browser to open "Search box and search for word"test"
search = driver.find_element_by_name("s")


search.send_keys("test")
search.send_keys(Keys.RETURN)

#We can get the all content of our webpage
print(driver.page_source)

try:#Explicit waits handling 
    main = WebDriverWait(driver, 10).until(
        #in this code we are searching in our webpage by given id name
        EC.presence_of_element_located((By.ID, "main"))
    )
    #And after accessing the files in id=class we can loop it through for accessing each and every article in it
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
        #by this code we can able to move back to our previous steps on the page
        driver.back()
        driver.back()
        #
except:
    driver.quit()

driver.quit()