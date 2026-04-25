import time
from time import sleep

from pyautogui import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://my.weekend.co.il/reviews.aspx?id=3094&lang=he")
time.sleep(2)

# close_cookies = driver.find_element(By.CLASS_NAME, "button")
# close_cookies.click()
# sleep(2)

# ------------------------------------------------------------------------------------------------------------------------
# אספו את כל ציוני חוות הדעת שהושארו לצימר והדפס אותם. )שימו לב לטעינת
# תוצאות נוספות

print("מתחיל בטעינת כל חוות הדעת...")

while True:
    try:
        load_more_btn = driver.find_element(By.XPATH, "//button[contains(., 'חוות דעת') and (contains(., 'הצג') or contains(., 'נוספות'))]")

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", load_more_btn)
        sleep(1)

        driver.execute_script("arguments[0].click();", load_more_btn)

        print("נטענו תוצאות נוספות, ממשיך...")
        sleep(2)  # זמן טעינה לשרת

    except:
        print("סיימנו לטעון את כל חוות הדעת (או שהכפתור לא נמצא).")
        break

all_scores = driver.find_elements(By.CSS_SELECTOR, "[class*='score']")

print(f"\n--- נמצאו {len(all_scores)} ציונים בסך הכל ---\n")

for i, score in enumerate(all_scores, 1):
    rating = score.text.strip()
    if rating:
        print(f"{i}. ציון: {rating}")
# ------------------------------------------------------------------------------------------------------------------------
# *********************************** |||||||||||מצאתי באג||||||||||| *************************************************

web_total_score = driver.find_element(By.CLASS_NAME, "details_total-comments__7ZPQw")
web_total_text = web_total_score.text

import re
declared_number = int(re.findall(r'\d+', web_total_text)[0])

actual_number = len(all_scores)

if actual_number != declared_number:
    print(f" מצאתי באג! קיימת אי התאמה:")
    print(f"כמות באתר: {declared_number}")
    print(f"כמות בפועל: {actual_number}")
    print(f"הפרש: {abs(actual_number - declared_number)}")
else:
    print(f" תקין: כמות הציונים ({actual_number}) תואמת להצהרת האתר.")
# ------------------------------------------------------------------------------------------------------------------------
# ב. הדפסו את ממוצע הציונים של הצימר
# ג. הדפס ו את הממוצע בפורמט הבא #.## )2 ספרות בלבד אחרי הנקודה(

total_sum = 0
count = 0

for score in all_scores:
    try:
        rating_value = float(score.text.strip())
        total_sum += rating_value
        count += 1
    except ValueError:

        continue


if count > 0:
    average = total_sum / count


    print(f"\n--- חישוב ממוצע ---")
    print(f"סך הכל נקודות: {total_sum}")
    print(f"מספר ציונים שחושבו: {count}")
    print(f"ממוצע הציונים: {average:.2f}")

else:
    print("לא נמצאו ציונים תקינים לחישוב ממוצע.")