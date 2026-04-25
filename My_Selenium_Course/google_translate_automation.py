import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# כניסה לגוגל טרנסלייט בעברית
driver.get("https://translate.google.com/?hl=iw")
sleep(5)

# הזנת טקסט (שם המזהה נשאר textarea בדרך כלל)
input_box = driver.find_element(By.XPATH, "//textarea")
input_box.send_keys("שלום, שמי Gemini")
sleep(2)

languages = ["אנגלית", "ערבית", "רוסית", "צרפתית", "לטינית"]

for lang in languages:
    print(f"\n--- מתרגם לשפה: {lang} ---")

    try:
        # 1. לחיצה על כפתור בחירת שפת היעד
        # בממשק עברי, הכפתור נקרא "בחירת שפת יעד"
        target_btn = driver.find_element(By.XPATH, "//button[@aria-label='בחירת שפת יעד']")
        target_btn.click()
        sleep(2)

        # 2. חיפוש השפה בתיבה שנפתחה
        search_input = driver.find_element(By.XPATH, "//input[@aria-label='חיפוש שפות']")
        search_input.clear()
        search_input.send_keys(lang)
        sleep(2)

        # 3. בחירת השפה מהרשימה
        # אנחנו מחפשים div שבו מופיע שם השפה
        lang_choice = driver.find_element(By.XPATH, f"//div[@role='option']//span[text()='{lang}']")
        lang_choice.click()
        sleep(3)

        # 4. בדיקת השמעה
        try:
            # בממשק עברי, הכפתור נקרא "הקשבה"
            # אנחנו מחפשים את הכפתור השני של ההקשבה (זה של התרגום)
            listen_btns = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'הקשבה')]")

            # אם יש יותר מרמקול אחד, האחרון הוא התרגום. אם יש אחד, זה הוא.
            listen_btns[-1].click()
            print(f"בוצעה השמעה בשפה {lang}")
            sleep(4)
        except:
            print(f"בשפה {lang} לא ניתן לבצע השמעה")

    except Exception as e:
        print(f"לא הצלחתי להחליף לשפת {lang}. בדוק אם נפתח חלון קופץ שמסתיר.")

print("\nהתרגיל הסתיים!")