from datetime import datetime, timedelta

# =========================================================
# Question 1: Print current date and time in Python
# Expected Output:
# Current date and time (example): 2026-01-06 00:15:30
# =========================================================

current_datetime = datetime.now()
print("Q1 Output:", current_datetime)


# =========================================================
# Question 2: Convert string into a datetime object
# Given:
# date_string = "Feb 25 2020 4:20PM"
# Expected Output:
# 2020-02-25 16:20:00
# =========================================================

date_string = "Feb 25 2020 4:20PM"
date_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print("Q2 Output:", date_object)


# =========================================================
# Question 3: Subtract a week (7 days) from a given date
# Given:
# given_date = datetime(2020, 2, 25)
# Expected Output:
# 2020-02-18
# =========================================================

given_date = datetime(2020, 2, 25)
new_date = given_date - timedelta(days=7)
print("Q3 Output:", new_date.date())


# =========================================================
# Question 4: Print a date in the following format
# Format:
# Day_name Day_number Month_name Year
# Given:
# given_date = datetime(2020, 2, 25)
# Expected Output:
# Tuesday 25 February 2020
# =========================================================

given_date = datetime(2020, 2, 25)
formatted_date = given_date.strftime("%A %d %B %Y")
print("Q4 Output:", formatted_date)


# =========================================================
# Question 5: Find the day of the week of a given date
# Given:
# given_date = datetime(2020, 7, 26)
# Expected Output:
# Sunday
# =========================================================

given_date = datetime(2020, 7, 26)
day_name = given_date.strftime("%A")
print("Q5 Output:", day_name)


# =========================================================
# Question 6: Add a week (7 days) and 12 hours to a given date
# Given:
# given_date = datetime(2020, 3, 22, 10, 0, 0)
# Expected Output:
# 2020-03-29 22:00:00
# =========================================================

given_date = datetime(2020, 3, 22, 10, 0, 0)
new_date = given_date + timedelta(days=7, hours=12)
print("Q6 Output:", new_date)


# =========================================================
# Question 7: Print current time in milliseconds
# =========================================================

current_time_ms = int(datetime.now().timestamp() * 1000)
print("Q7 Output:", current_time_ms)


# =========================================================
# Question 8: Convert the following datetime into a string
# Given:
# given_date = datetime(2020, 2, 25)
# Expected Output:
# "2020-02-25 00:00:00"
# =========================================================

given_date = datetime(2020, 2, 25)
date_string = given_date.strftime("%Y-%m-%d %H:%M:%S")
print("Q8 Output:", date_string)


# =========================================================
# Question 9: Calculate the date 4 months from the current date
# Given:
# given_date = datetime(2020, 2, 25).date()
# Expected Output:
# 2020-06-25
# =========================================================

given_date = datetime(2020, 2, 25).date()
new_month = given_date.month + 4
new_date = given_date.replace(month=new_month)
print("Q9 Output:", new_date)


# =========================================================
# Question 10: Calculate number of days between two given dates
# Given:
# date_1 = datetime(2020, 2, 25)
# date_2 = datetime(2020, 9, 17)
# Expected Output:
# 205 days
# =========================================================

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

difference = date_2 - date_1
print("Q10 Output:", difference.days)

# ==================== COMPLETED ======================= #