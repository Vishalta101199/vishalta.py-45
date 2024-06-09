from selenium import webdriver
from selenium.webdriver.common.by import By

# --- Configuration ---
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
output_file = "webpage_task_11.txt"

# --- Start the browser ---
driver = webdriver.Chrome()  # You'll need a ChromeDriver executable for this
driver.get(url)

# --- Login ---
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

# --- Extract information ---
page_title = driver.title
current_url = driver.current_url
page_source = driver.page_source

print("Page Title:", page_title)
print("Current URL:", current_url)

# --- Save to file ---
with open(output_file, "w", encoding="utf-8") as file:
    file.write(page_source)

# --- Close the browser ---
driver.quit()