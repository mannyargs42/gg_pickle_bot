from datetime import datetime, timedelta
import random

"""
format_date and format_time help prepare the variables that will specify
what date and time to book a court reservation, so that they are in the
specific format necessary for find_element.
"""

def format_date(num_days_ahead):
    """
    Takes a variable for the number of days from today.
    Returns a formatted string that can be read by Selenium find_element to
    interact with the site calendar in web_scraper.py.

    num_days_ahead must be a positive integer.

    Expected output for today should look like: "Wednesday, November 27, 2024"
    Expected output for days_from_today should be the same format.
    """
    date_today = datetime.now()
    day_today = date_today.day
    formatted_date_today = date_today.strftime(f"%A, %B {day_today}, %Y")
    future_date = date_today + timedelta(days=num_days_ahead)
    future_day = future_date.day
    formatted_future_date = future_date.strftime(f"%A, %B {future_day}, %Y")
    return formatted_date_today, formatted_future_date

def format_time(target_time, time_format="%I:%M %p"):
    """
    Converts a target time to a time option +0, 0.5 or 1 hour, in format to
    match find_element on website.

    Args:
        target_string(str): A time string
    Returns:
        Expected output for time in format: "%207:30%20AM&end"
    """
    datetime_obj = datetime.strptime(target_time, time_format)
    random_timeaddn = random.choice([0, 0.5, 1])
    new_target = datetime_obj + timedelta(hours=random_timeaddn)
    new_target_str = new_target.strftime(time_format)
    zeroless_target = new_target_str.lstrip("0")
    halfformat_time = zeroless_target.replace(" ", "%20")
    formatted_time = "%20" + halfformat_time + "&end"
    return formatted_time