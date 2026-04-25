# # תרגיל 1
for i in range (1,10000):
    if i % 7 == 0 or "7" in str(i):
        print("BOOM!")
    else:
        print(i)

# # # תרגיל 2
# # נתונים :
# # מחיר טוסט בסיסי: 15 ₪
# # תוספת: 3 ₪ לכל תוספת
# # שתייה (קולה / תפוזים): 8 ₪
# # הנחת נוער (גיל 15–18): 5 ₪ הנחה
# #
# # וצריך לחלק לפונקציות:
# # פונקציית גיל
# # פונקציית תוספות
# # פונקציית שתיה
#
# def get_age():
#     while True:
#         age = input("נא הקלד גיל: ")
#
#         if not age.isdigit():
#             print("יש להקליד מספרים בלבד")
#             continue
#
#         age = int(age)
#
#         if age < 5 or age > 100:
#             print("נא להקליד גיל תקני בין 5 ל 100")
#             continue
#
#         discount = 0
#         if 15 <= age <= 18:
#             discount = 5
#             print("התקבלה הנחה על סך 5 שקלים")
#
#         return discount
#
# def get_toppings():
#     answer = input("האם תרצה תוספות? (כן/לא): ")
#
#     if answer == "לא":
#         double_check = input("בטוח שלא בא לך משהו מעל? (כן/לא): ")
#         if double_check == "כן":
#             return 0
#
#     while True:
#         amount = input("כמה תוספות תרצה? ")
#
#         if not amount.isdigit():
#             print("נא להקליד מספרים בלבד")
#             continue
#
#         amount = int(amount)
#         return amount * 3
#
# def get_drink():
#     answer = input("האם תרצה שתייה? (כן/לא)" )
#
#     if answer == "לא":
#         return 0
#
#     while True:
#         drink = input("בחר מבין השניים (קולה/תפוזים)")
#
#         if drink == "קולה" or drink == "תפוזים":
#             return 8
#         else:
#             print("יש לבחור מבין השניים בלבד" )
#
# price = 15
#
# discount = get_age()
# toppings_price = get_toppings()
# drink_price = get_drink()
#
# total = price + toppings_price + drink_price - discount
# print(f"סהכ לתשלום :  {total} ")