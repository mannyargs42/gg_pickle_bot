from selenium import webdriver
from selenium import By

"""
Use Selenium to automate browser interactions.

Use WebScraper class functions in order to navigate the target website and
book a court reservation.
* __init__: Instantiate Selenium ChromeDriver and open the web browser.
* navigator: Navigate to the web page for scheduling tennis/pickleball.
* login: Locate the "Log In" element of the webpage and click.
    Enter email and password.
    Click the login button.
    Locate and click "Pickleball and mini tennis reservations" from
        "Reservations" drop-down menu.
*choose_date_time: Find today's date and click to open calendar.
    Locate date (8 days from today) and click.
    Locate desired time option and click.
*finish booking: Change duration to "1 hour & 30 minutes" from drop-down.
    Click "Check to agree to above disclosure" box.
    Click "Save" to finish booking.


"""