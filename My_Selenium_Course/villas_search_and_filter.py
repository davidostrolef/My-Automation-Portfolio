import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.vila4u.com")
time.sleep(2)

cookie_y = driver.find_element(By.CLASS_NAME, "cookiesApprove").click()
time.sleep(1)

# ------------------------------------------------------------------------------------------------------------------------
# א. בשדה אזור רשמו "וילות בצפון"
siteSearch = driver.find_element(By.ID, "siteSearch")
siteSearch.send_keys("וילות בצפון")

sleep(1)
# ------------------------------------------------------------------------------------------------------------------------
# ב. בקטגוריות בחר ו וילה לזוג

category = driver.find_element(By.ID, "realCategory")
category.click()
sleep(2)

category_dropdown = driver.find_element(By.ID, "realCategory")
select_category = Select(category_dropdown)
select_category.select_by_visible_text("וילה לזוג")

print("הקטגוריה 'וילה לזוג' נבחרה")
sleep(2)
# ------------------------------------------------------------------------------------------------------------------------
# ג. באבזור בחרו בריכה מחוממת ופינת מנגל

accessory_menu = driver.find_element(By.CLASS_NAME, "selectB")
accessory_menu.click()
print("תפריט אבזור נפתח")
sleep(2)


pool_option = driver.find_element(By.XPATH, "//*[contains(text(),'בריכה מחוממת')]")
pool_option.click()
print("נבחרה בריכה מחוממת")
sleep(1)


try:
    mangal_option = driver.find_element(By.XPATH, "//*[contains(text(),'מנגל')]")
    mangal_option.click()
    print("נבחר מנגל")
except:
    accessory_menu.click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[contains(text(),'מנגל')]").click()
    print("נבחר מנגל (אחרי פתיחה חוזרת)")

sleep(1)
# ------------------------------------------------------------------------------------------------------------------------
# ד. בכמות חדרים ביחרו 9+

rooms = driver.find_element(By.ID, "selRooms")
rooms.click()
sleep(2)

rooms_9_plus = driver.find_element(By.XPATH, "//*[contains(text(),'9+')]")
rooms_9_plus.click()
print("נבחרו 9+ חדרים")
sleep(2)
# ------------------------------------------------------------------------------------------------------------------------
# לחצו על חפש
search = driver.find_element(By.CLASS_NAME, "submitSearch")
search.click()
print("התבצע חיפוש")
sleep(3)
# ------------------------------------------------------------------------------------------------------------------------
# הדפיסו את שמות הווילות )בלבד( שענו על התוצאות. )יש לשים לב להדפיס רק את
# התוצאות ולא ווילות שמופיעות כפרסומות או כהמלצות (

all_villas = driver.find_elements(By.CLASS_NAME, "vilaName")


for villa in all_villas:
    name = villa.text


    if name.strip():
        print(name)

sleep(2)
# ------------------------------------------------------------------------------------------------------------------------