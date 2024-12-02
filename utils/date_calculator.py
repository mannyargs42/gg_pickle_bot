from datetime import datetime, timedelta

"""
Takes a variable for the number of days from today.
Returns a formatted string that can be read by Selenium find_element to
interact with the web calendar in web_scraper.py.

num_days_ahead must be a positive integer.

Expected output for today should look like: "Wednesday, November 27, 2024"
Expected output for days_from_today should be: "4" or ...
"""

date_today = datetime.now()
formatted_date_today = date_today.strftime("%A, %B %d, %Y")
print(formatted_date_today)