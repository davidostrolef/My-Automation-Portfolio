# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # # #
# # # # try:
# # # #     driver = webdriver.Chrome()
# # # #     print("webdriver עובד!")
# # # # except Exception as e:
# # # #     print(f"שגיאה ב webdriver: {e}")
# # #
# # #
# # # driver = webdriver.Chrome()
# # # driver.maximize_window()
# # # driver.get("http://www.google.com")
# # # driver.find_element(By.NAME, "q").send_keys("Israel")
# # # print(driver.current_url)
# # # print(driver.title)
# # #
# # # # time.sleep(6)
# # # # - פקודה להמתנה של זמן מוקצב
# # #
# # #
# # # input("press any key to continue")
# #
# #
# # *********תרגילים**********
#
# # תרגיל-1
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://danielauto.net/practice/newLocator/locator.html")
#
# # 1 – הזנת first name לפי ID
# first_name = driver.find_element(By.ID, "firstName")
# first_name.send_keys("hello")
#
# # 2 – לחיצה על הכפתור (נצבע באדום)
# button = driver.find_element(By.ID, "submit")
# button.click()
#
# # 3 – משיכת המילה hello בעזרת NAME
# hello_text = driver.find_element(By.NAME, "hello")
# print(hello_text.text)
#
# # 4 – משיכת המילה world בעזרת TAG NAME
# world_text = driver.find_element(By.TAG_NAME, "p")
# print(world_text.text)
#
# # הדפסת hello world
# print(hello_text.text + " " + world_text.text)
#
# # 5 – משיכת טקסט בעזרת CLASS NAME
# class_text = driver.find_element(By.CLASS_NAME, "class1")
# print(class_text.text)
#
# # 6 – שימוש ב XPATH
# xpath_text = driver.find_element(By.XPATH, "//*[contains(text(),'I got the text by XPATH')]")
# print(xpath_text.text)
#
# # לחיצה על לינק לפי LINK TEXT
# link = driver.find_element(By.LINK_TEXT, "Click me to check link text")
# link.click()
#
# time.sleep(2)
#
# print(driver.find_element(By.TAG_NAME, "h1").text)
#
# driver.back()
#
# # 7 – PARTIAL LINK TEXT
# partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# partial_link.click()
#
# time.sleep(2)
#
# print(driver.find_element(By.TAG_NAME, "h1").text)
#
# driver.back()
#
# # 8 – CSS SELECTOR
# css_button = driver.find_element(By.CSS_SELECTOR, "button")
# css_button.click()
#
# time.sleep(3)
#
# driver.quit()

# **************תרגיל אוטומציה********************
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://stackoverflow.com/tags")
#
# tags = driver.find_elements(By.XPATH,"//a[@rel='tag']")
# qu = driver.find_elements(By.XPATH,"//div[@class='mt-auto d-flex jc-space-between fs-caption fc-black-400']//div[@class='flex--item']")
#
# for tags, qu in zip(tags,qu):
#     number = qu.text.split(' ')
#     if int(number[0]) > 400000 :
#      print(f"in {tags.text} we have {qu.text}")

# ****************************************************************

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demoqa.com/webtables")
#
# name = "Daniel"
# age = "20"
#
# # חיפוש ושורה לעריכה
# driver.find_element(By.ID, "searchBox").send_keys("alden")
# driver.find_element(By.ID, "edit-record-2").click()
#
# driver.find_element(By.ID, "firstName").clear()
# driver.find_element(By.ID, "firstName").send_keys(name)
#
# driver.find_element(By.ID, "age").clear()
# driver.find_element(By.ID, "age").send_keys(age)
#
# driver.find_element(By.ID, "submit").click()
#
# time.sleep(1)
#
# # חיפוש השם החדש
# search_box = driver.find_element(By.ID, "searchBox")
# search_box.clear()
# search_box.send_keys(name)
#
# # מחכה עד שהשורה תופיע, עד 10 שניות
# found = False
# for i in range(10):
#     try:
#         name_cell = driver.find_element(By.XPATH, "//div[@class='rt-tbody']//div[@role='row'][1]//div[1]")
#         if name_cell.text == name:
#             found = True
#             break
#     except:
#         pass
#     time.sleep(1)
#
# if not found:
#     print("Row not found")
# else:
#     age_cell = driver.find_element(By.XPATH, "//div[@class='rt-tbody']//div[@role='row'][1]//div[3]")
#     if age_cell.text == age:
#         print("Test Passed")
#     else:
#         print("Test Failed")
#
# # הדפסת כותרות
# titles = driver.find_elements(By.XPATH, "//div[@class='rt-thead']//div[@role='columnheader']")
# for title in titles:
#     print(title.text)
#
# input("x")

# ****************************************************************
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.tiran-bank.co.il/conversion-calculator/")
#
# time.sleep(1)
# #לחיצה לפתיחת הטאב
# driver.find_element(By.ID, "NewTab").click()
# time.sleep(1)
# #פקודה שמכניסה לרשימה את כל הטאסים לפי מספרים מ 0
# tabs = driver.window_handles
# #היינו על 0 ורוצים לעבור ל 1
# driver.switch_to.window(tabs[1])
# print(driver.current_url)
# #אחרי שסיימתי את כל הבדיקות שאני רוצה סוגרים את טאב הזה שנמצאים בו
# driver.close()
# #ואז חוזרים למה שהיינו או הבא אחרת נקבל שגיאה
# driver.switch_to.window(tabs[0])
#
# input("x")


#אם לא בטוח איזה טאב חדש נפתח (יכול להיות יותר מטאב אחד פתוח), אפשר להשתמש בלולאה כדי למצוא את הטאב החדש

# original_tab = driver.current_window_handle
# driver.find_element(By.ID, "NewTab").click()
# time.sleep(1)
#
# for tab in driver.window_handles:
#     if tab != original_tab:
#         driver.switch_to.window(tab)
#         break

# ****************************************************
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.tiran-bank.co.il/conversion-calculator/")
#
# driver.find_element(By.ID, "SelectCurrencyAmount").send_keys("50")
# driver.find_element(By.ID, "widgetcalcsubmit").click()
# time.sleep(10)
# *****************************************************


# --------------------------------------------------------
# driver.switch_to.frame(iframe)  # נכנסים ל-“חלון הקטן”
# driver.find_element(...)         # עכשיו אפשר לגשת לאלמנטים שבתוך ה-iframe
# # driver.switch_to.default_content()  # חוזרים לדף הראשי
# # ---------------------------------------------------------

# *************** תרגיל **************
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://www.tiran-bank.co.il/conversion-calculator/")
#
# wait = WebDriverWait(driver, 15)
#
# try:
#     # מחכה שהעמוד יטען
#     time.sleep(2)
#
#     # אם האלמנט נמצא בתוך iframe – מנסה קודם לעבור אליו
#     iframes = driver.find_elements(By.TAG_NAME, "iframe")
#     if len(iframes) > 0:
#         print(f"נמצא {len(iframes)} iframe, מנסה לעבור לזה הראשון...")
#         driver.switch_to.frame(iframes[0])  # נכנס ל‑iframe הראשון
#         time.sleep(1)
#
#     # מחכה לשדה ה‑input של הסכום
#     amount_input = wait.until(EC.presence_of_element_located((By.ID, "SelectCurrencyAmount")))
#     amount_input.clear()
#     amount_input.send_keys("50")
#
#     # לוחץ על כפתור החישוב
#     calc_button = wait.until(EC.element_to_be_clickable((By.ID, "widgetcalcsubmit")))
#     calc_button.click()
#
#     print("הזן סכום ולחץ לשקלול בוצעו.")
#
# except Exception as e:
#     print("אירעה שגיאה:", e)
#
# finally:
#     time.sleep(5)  # מאפשר לראות את התוצאה
#     driver.quit()

# ___________________________________________________________________________________


# *************** alerts **************


# ישנם שלושה סוגים עיקריים של אלרטים:
#
# Simple Alert: מציג הודעה וכפתור "אישור" (OK) בלבד.
#
# Confirmation Alert: מציג הודעה ומבקש מהמשתמש לבחור בין "אישור" ל"ביטול" (Cancel).
#
# Prompt Alert: מבקש מהמשתמש להקליד טקסט בתוך תיבה.

# from selenium.webdriver.common.alert import Alert
#
# # 1. מעבר אל האלרט (Switch to)
# alert = driver.switch_to.alert
#
# # 2. לחיצה על "אישור" (Accept)
# alert.accept()
#
# # 3. לחיצה על "ביטול" (Dismiss)
# alert.dismiss()
#
# # 4. קריאת הטקסט שמופיע באלרט
# print(alert.text)
#
# # 5. כתיבת טקסט בתוך התיבה (במקרה של Prompt)
# alert.send_keys("הטקסט שלי")
# alert.accept()


# # --------------------------------------------------------------------------------------------------
# *************** צילומי מסך **************
#
# # צילום מסך של כל חלון הדפדפן הנוכחי
# driver.save_screenshot("screenshot.png")
#
# # צילום אלמנט ספציפי: לפעמים לא מעניין אותנו כל הדף, אלא רק כפתור מסוים או טבלה.
# element = driver.find_element(By.ID, "submit-button")
# element.screenshot("button_look.png")
#
# # שמירה כבינארי (Binary Data): שימושי אם אתה רוצה לשלוח את התמונה לבסיס נתונים או לעבד אותה בזיכרון בלי לשמור קובץ פיזי.
# screenshot_as_bytes = driver.get_screenshot_as_png()
#
# # טיפים לשימוש חכם בצילומים:****************
# # שמות קבצים דינמיים: מומלץ להוסיף חותמת זמן (Timestamp) לשם הקובץ כדי שלא תדרוס צילומים קודמים:
# import time
# filename = f"error_{time.strftime('%Y%m%d-%H%M%S')}.png"
# driver.save_screenshot(filename)
# #שימוש הכי נפוץ הוא לצלם מסך ברגע שנוצרת שגיאה (Exception). כך, כשאתה בא לבדוק למה הטסט נכשל בלילה, יש לך תמונה של מה שהדרייבר ראה באותו רגע.
# # שים לב! אם יש Alert פתוח על המסך, פקודת save_screenshot לרוב תיכשל או תזרוק שגיאה. אתה חייב קודם לטפל באלרט (לאשר או לבטל אותו) ורק אז תוכל לצלם את הדף.
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import WebDriverException, NoAlertPresentException
#
#
# def capture_failure_screenshot(driver, folder_name="failures"):
#     # יצירת תיקייה לצילומים אם היא לא קיימת
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#
#     # יצירת שם קובץ ייחודי עם תאריך ושעה
#     timestamp = time.strftime("%Y%m%d-%H%M%S")
#     file_path = os.path.join(folder_name, f"failure_{timestamp}.png")
#
#     try:
#         driver.save_screenshot(file_path)
#         print(f"צילום מסך נשמר בכתובת: {file_path}")
#     except Exception as e:
#         print(f"לא ניתן היה לצלם מסך: {e}")
#
#
# # הגדרת הדרייבר
# driver = webdriver.Chrome()
#
# try:
#     driver.get("https://www.google.com")
#
#     # ננסה למצוא אלמנט שלא קיים כדי לעורר שגיאה בכוונה
#     search_box = driver.find_element(By.ID, "non-existent-id")
#     search_box.send_keys("Selenium")
#
# except Exception as e:
#     print(f"הטסט נכשל: {e}")
#
#     # בדיקה אם יש אלרט פתוח (כי אי אפשר לצלם מסך כשיש אלרט)
#     try:
#         alert = driver.switch_to.alert
#         print(f"נמצא אלרט עם הטקסט: {alert.text}. סוגר אותו לפני צילום...")
#         alert.dismiss()
#     except NoAlertPresentException:
#         pass  # אין אלרט, אפשר להמשיך לצילום
#
#     # קריאה לפונקציית הצילום שלנו
#     capture_failure_screenshot(driver)
#
# finally:
#     driver.quit()

# -------------------------------------------------------------------------------------------------
# *************** צ'ק בוקס **************

# פעולות מרכזיות עם Checkboxes
# כדי לעבוד נכון, אנחנו משתמשים במתודות של אובייקט ה-WebElement:
#
# is_selected(): מחזירה True אם התיבה מסומנת ו-False אם לא. זהו הכלי החשוב ביותר כדי להימנע מסימון כפול (שיבטל את הסימון).
#
# is_enabled(): בודקת אם התיבה ניתנת ללחיצה או שהיא אפורה (Disabled).
#
# is_displayed(): לוודא שהתיבה בכלל נראית על המסך לפני שמנסים ללחוץ.
#
# דוגמת קוד מעשית
# נניח שיש לנו תיבת סימון של "אני מסכים לתנאי השימוש":

# from selenium.webdriver.common.by import By
#
# # מציאת התיבה
# checkbox = driver.find_element(By.ID, "terms-of-service")
#
# # בדיקה: אם היא לא מסומנת - סמן אותה
# if not checkbox.is_selected():
#     checkbox.click()
#     print("התיבה סומנה בהצלחה.")
# else:
#     print("התיבה כבר הייתה מסומנת.")
#
# # בדיקה נוספת: לוודא שהסימון אכן נקלט
# assert checkbox.is_selected() == True

# ------------------------------------------------------------------------------------------------------------
# *************** ס ט ו פ ר **************


# # מדידת זמן ביצוע (סטופר בסיסי)
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# # התחלת הסטופר
# start_time = time.time()
#
# driver.get("https://www.google.com")
#
# # עצירת הסטופר
# end_time = time.time()
#
# # חישוב ההפרש
# duration = end_time - start_time
# print(f"הדף נטען תוך {duration:.2f} שניות")
#
# driver.quit()


# 2. הגדרת "פסק זמן" (Timeout) לדף
# הגדרת מקסימום 10 שניות לטעינת דף
# driver.set_page_load_timeout(10)
#
# try:
#     driver.get("https://www.slow-website.com")
# except Exception:
#     print("האתר איטי מדי! עברו 10 שניות והוא לא נטען.")

# שימוש ב-Wait (הסטופר החכם)
# זה ה"סטופר" הכי חשוב בסלניום. במקום לחכות זמן קבוע (כמו time.sleep(5) שזה נחשב הרגל רע), אנחנו משתמשים ב-WebDriverWait. זהו סטופר שבודק כל חצי שנייה אם תנאי מסוים התקיים:


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# # סטופר חכם: חכה עד 15 שניות שהכפתור יופיע
# wait = WebDriverWait(driver, 15)
# button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
# button.click()

# ----------------------------------------------------------------------------------------

# *************** Action Chains **************

# סלניום, אנחנו עוברים מהפעולות הפשוטות (כמו לחיצה רגילה) לפעולות מורכבות יותר שמדמות התנהגות אנושית אמיתית עם העכבר והמקלדת.

# זהו כלי חיוני כשצריך לבצע פעולות כמו גרירה והשלכה (Drag and Drop), ריחוף (Hover), או לחיצה על המקש הימני.

# איך עובדים עם ActionChains?
# כדי להשתמש בזה, צריך לייבא את המחלקה ActionChains. הרעיון הוא שאתה "בונה" שרשרת של פעולות ובסוף נותן להן פקודה להתבצע בעזרת המתודה .perform().
#
# 1. ריחוף עם העכבר (Mouse Hover)
# שימוש נפוץ בתפריטים שנפתחים רק כשמניחים עליהם את העכבר.

# from selenium.webdriver import ActionChains
#
# actions = ActionChains(driver)
# menu = driver.find_element(By.ID, "main-menu")
#
# # ריחוף מעל האלמנט
# actions.move_to_element(menu).perform()

# גרירה והשלכה (Drag and Drop)**************
# source = driver.find_element(By.ID, "draggable")
# # target = driver.find_element(By.ID, "droppable")
# #
# # # גרירה מנקודה א' לנקודה ב'
# actions.drag_and_drop(source, target).perform()
#
# # לחיצה ימנית ודאבל-קליק
# button = driver.find_element(By.ID, "my-button")
#
# # לחיצה ימנית (Context Click)
# actions.context_click(button).perform()
#
# # לחיצה כפולה
# actions.double_click(button).perform()
#
# # פעולות מקלדת מתקדמות
# # אקשן צ'יינס מאפשר גם לשלוט במקלדת בצורה מורכבת, כמו לחיצה על צירופי מקשים (למשל Ctrl+A):
# from selenium.webdriver.common.keys import Keys
#
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
#
# # שרשור פעולות: אתה יכול לבצע כמה פעולות ברצף:
# actions.move_to_element(elem).click().send_keys("hello").perform()

# ------------------------------------------------------------------------------------------------
# # *************** sliders **************
#
# action.drag_and_drop_by_offset(element,100,100).perform()
# ------------------------------------------------------------------------------------------------
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://danielauto.net/practice/usefull/useful1.html")
time.sleep(2)
driver.find_element(By.ID,"myFile").click()


input("x")

#"D:\image.png"

# def multiply_by_two(x):
#     return x * 2
#
# numbers_input = input(" הכנס מספרים מופרדים ברווח:  ")
#
# numbers = (map(int, numbers_input.split()))
#
# # שימוש ב-map בלי lambda
# doubled = map(multiply_by_two, numbers)
#
# new_list  = list(doubled)
# print("רשימה כפול 2:", new_list)

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://danielauto.net/practice/usefull/useful1.html")
time.sleep(2)
driver.find_element(By.ID,"myFile").click()


input("x")