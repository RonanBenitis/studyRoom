# documentation in https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Start setion
driver = webdriver.Chrome()

# 2. Take action on browser
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 3. Request browser information
title = driver.title
assert title == "Web form"

# 4. Establish Waiting Strategy
driver.implicitly_wait(0.5)

# 5. Find an element
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# 6. Take action on element
text_box.send_keys("Selenium")
submit_button.click()

# 7. Request element information
message = driver.find_element(by=By.ID, value="message") # Esse faz parte do step 5
value = message.text
assert value == "Received!"

# End the session
driver.quit()