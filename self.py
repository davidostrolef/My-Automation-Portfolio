import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# מחכה עד שהשדה של החיפוש יופיע
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

print("העמוד נטען, אפשר לבצע חיפוש")

time.sleep(5)  # רק בשביל לראות את הדף

driver.quit()
