from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.testportal.net/')
time.sleep(10)
title=driver.title

# verify the title
Expected_title = "Testportal: Online assessment platform | Create your own tests, quizzes and exam"

if title == Expected_title:
    print("Title verification is successful")
else:
    print(f"title verification failed. Expected '{Expected_title}', but we got '{title}'")


driver.close()


