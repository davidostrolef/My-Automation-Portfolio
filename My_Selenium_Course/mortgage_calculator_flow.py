import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.supermarker.themarker.com")
time.sleep(2)

#נאשר עוגיות
cookie_y = driver.find_element(By.ID, "acceptAll").click()
time.sleep(1)
# -----------------------------------------------------------------------------------
#א. חפשו בשדה החיפוש "מחשבון" ובחר מההשלמה האוטומטית את "מחשבון משכנתא"

# search = driver.find_element(By.ID, "txtSearch")
# search.send_keys("מחשבון")
# time.sleep(3)

# mashkanta = driver.find_element(By.XPATH, "//li[contains(., 'מחשבון משכנתא')]")
# mashkanta.click()
# time.sleep(3)
#לא עבד

# search = driver.find_element(By.ID, "txtSearch")
# search.send_keys("מחשבון משכנתא")
# time.sleep(3)
#
# search.send_keys(Keys.ENTER)
# time.sleep(3)
#תוצאה לא רצויה

search = driver.find_element(By.ID, "txtSearch")
search.send_keys("מחשבון מש")
time.sleep(3)

search.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
search.send_keys(Keys.ENTER)
# ---------------------------------------------------------------------------------------
# ב. וודאו שבשדה "חשב לפי" החזר חודשי נבחר )הדפס לconsole שזו אכן המציאות(

monthly_return = driver.find_element(By.ID, "rblSelectCalcType_0")
if monthly_return.is_selected():
    print("שדה 'החזר חודשי' נבחר")
else:
    monthly_return.click()
    print("שדה 'החזר חודשי'לא היה נבחר")
sleep(3)

# ------------------------------------------------------------------------------------------
# ג. בשדה "בחר שיטת החזר" – הדפס את הטקסט שמופיע בסימן שאלה )כשעומדים עליו
# עליו עם העכבר מוצג טקסט (

question_mark = driver.find_element(By.CLASS_NAME, "titleImg")
actions = ActionChains(driver)
actions.move_to_element(question_mark).perform()

text_title = question_mark.get_attribute("title")
text_alt = question_mark.get_attribute("alt")

if text_title:
    print("הטקסט בסימן השאלה (title) הוא:", text_title)
elif text_alt:
    print("הטקסט בסימן השאלה (alt) הוא:", text_alt)
else:
    print("האלמנט נמצא, אך הטקסט מוחבא במקום אחר.")
sleep(2)
# --------------------------------------------------------------------------------------------
# ד. בשדה "בחר שיטת החזר" בחרו ב"קרן שווה"

return_type = driver.find_element(By.XPATH, "//label[contains(.,'קרן שווה')]")
if return_type.is_selected():
    print("שדה 'שווה' נבחר")
else:
    return_type.click()
    print("שדה 'שווה'לא היה נבחר")
sleep(3)
# -----------------------------------------------------------------------------------------------
# בשדה "הצמדה למדד" בחר ו "ללא הצמדה"

no_hatzmada = driver.find_element(By.XPATH, "//*[@id='rblMadad']//label[contains(.,'ללא הצמדה')]")
if no_hatzmada.is_selected():
    print("שדה 'ללא הצדמה' נבחר")
else:
    no_hatzmada.click()
    print("שדה 'ללא הצמדה'לא נבחר ועכשיו כן")
sleep(3)
# ---------------------------------------------------------------------------------------------------
# הקלד ו בשדה " סכום המשכנתא" 500000 ₪

mashkanta_input = driver.find_element(By.XPATH, "//*[@id='txtLoanAmount']")
mashkanta_input.clear()
mashkanta_input.send_keys("500000")
print("הוקלד סכום: 500,000")
sleep(2)
# -----------------------------------------------------------------------------------------------------
# ז. הזז ועל ידי המכוון ל20 שנה בתקופת המשכנתא

year_spend_slider = driver.find_element(By.XPATH, "//*[@id='sliderTerm']/span")
year_spend_slider.click()

for i in range(5):
    year_spend_slider.send_keys(Keys.ARROW_RIGHT)
    sleep(0.5)
print("נבחרה משכנתא ל20 שנה")

sleep(2)
# --------------------------------------------------------------------------------------------------------
# הקלד ו בשדה הריבית 3.75 אחוז

ribit = driver.find_element(By.XPATH, "//*[@id='txtInterest']")
ribit.clear()
ribit.send_keys("3.75")
print("הוקלדה ריבית של 3.75")
sleep(2)
# ----------------------------------------------------------------------------------------------------------
# לחצו על חשב. קחו את סכום ההלוואה )שמופיע ראשון בטבלה "לקחת הלוואה על סך"( והדבקו אותו לשדה מייל שבטופס הצור קשר בצד שמאל

calculate = driver.find_element(By.ID, "ibCalc")
calculate.click()
sleep(2)

loan_element = driver.find_element(By.ID, "keren")
loan_text = loan_element.text
print(f"סכום ההלוואה: {loan_text}")

contact_by_mail = driver.find_element(By.ID, "txtEmail")
contact_by_mail.clear()
contact_by_mail.send_keys(loan_text)

print("סכום ההלוואה הודבק למייל")
sleep(2)
# ----------------------------------------------------------------------------------------------------------------
# הזינו בטופס צור קשר שם

contact_name = driver.find_element(By.ID, "txtShemPrati")
contact_name.clear()
contact_name.send_keys("דוד הגבר")

print("הוזן שם תקני ביצירת קשר")
sleep(2)
# ------------------------------------------------------------------------------------------------------------------
# בדקו האם הצ'קבוקס של " קראתי את תקנון האתר " מסומן. אם לא סמנו אותו ולחצו על
# כפתור " בדיקה להוזלת הריבית"

terms_and_conditions = driver.find_element(By.ID, "cbTnaim")
if terms_and_conditions.is_selected():
    print("הצ'קבוקס כבר מסומן")
else:
    print("הצ'קבוקס לא היה מסומן - מסמן אותו עכשיו")
    terms_and_conditions.click()

sleep(1)

check_ribit_discount = driver.find_element(By.ID, "btnSendLid")
check_ribit_discount.click()

print("בוצעה לחיצה על כפתור בדיקה להוזלת הריבית")
sleep(2)
# ---------------------------------------------------------------------------------------------------------------------
# ביד קו שמופיעות הודעות שגיאה תקינות. א. יש להזין כתובת מייל ב. יש להזין מספר טלפון.
try:
    email_error = driver.find_element(By.ID, "txtEmail-error")
    if email_error.is_displayed():
        print("הודעת שגיאה למייל מופיעה:", email_error.text)
except:
    print("לא נמצאה הודעת שגיאה לשדה המייל")

try:
    phone_error = driver.find_element(By.ID, "txtTelephone-error")
    if phone_error.is_displayed():
        print("הודעת שגיאה לטלפון מופיעה:", phone_error.text)
except:
    print("לא נמצאה הודעת שגיאה לשדה הטלפון")
# -----------------------------------------------------------------------------------------------------------------------
