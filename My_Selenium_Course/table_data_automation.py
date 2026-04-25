import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://danielauto.net/practice/tabls/tables.html")

rows = driver.find_elements(By.XPATH, "//tbody//tr")
cols = driver.find_elements(By.XPATH, "//tbody//tr[1]//td")
print(f"Number of rows: {len(rows)}")
print(f"Number of cols: {len(cols)}")

g_a = g_b = g_c = 0
prices = []
total_change = 0.0

print("\n--- Companies starting with A ---")

for row in rows:
    name = row.find_element(By.XPATH, "./td[1]").text
    group_name = row.find_element(By.XPATH, "./td[2]").text
    price_val = row.find_element(By.XPATH, "./td[3]").text
    change_val = row.find_element(By.XPATH, "./td[5]").text

    if group_name == "A": g_a += 1
    elif group_name == "B": g_b += 1
    elif group_name == "C": g_c += 1

    prices.append(float(price_val.replace(',', '')))
    total_change += float(change_val.replace('%', ''))

    if name.lower().startswith("a"):
        print(f"Company: {name}")
        if group_name == "C":
            print(f"^^ Found in Group C: {name}")

print(f"\nGroups: A={g_a}, B={g_b}, C={g_c}")
print(f"Max Price: {max(prices)}")
print(f"Total Change: {total_change:.2f}%")

print("\n--- Last cells in irregular table ---")
driver.get("https://danielauto.net/practice/tabls/tables2.html")
last_cells = driver.find_elements(By.XPATH, "//tr/td[last()]")

for cell in last_cells:
    print(cell.text)

time.sleep(2)
driver.quit()