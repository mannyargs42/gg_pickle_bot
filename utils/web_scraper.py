from selenium import webdriver
from selenium import By

"""
Use Selenium to automate browser interactions.

Use WebScraper class functions in order to navigate the target website and
book a court reservation.
* __init__: Instantiate Selenium ChromeDriver and open the web browser.
* navigator: Navigate to the web page for scheduling tennis/pickleball.
* login_to_reserve: Locate the "Log In" element of the webpage and click.
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

class WebScraper:
    def __init__(self):
        """
        Instantiate Selenium ChromeDriver and open web browser.
        """
        self.driver = webdriver.Chrome()

    def navigator(self, url):
        """
        Navigate to the web page for scheduling tennis/pickleball.
        'url' may change, so it is best to pass the variable from main.py
        """
        self.driver.get(url)

    def login_to_reserve(self, email, password):
        """
        Coordinate the following steps in succession:
        Locate the "Log In" element of the webpage and click.
        In the login page, locate email and password input boxes.
        Locate login button.
        Enter email and password into input fields.
        Click the login button.
        Locate and click "Pickleball and mini tennis reservations" from
        "Reservations" drop-down menu.
        """
        login_button = self.driver.find_element(By.LINK_TEXT, 'LOG IN')
        login_button.click()
        enter_email = self.driver.find_element(By.ID, 'UserNameOrEmail')
        enter_password = self.driver.find_element(By.ID, 'Password')
        login_button = self.driver.find_element(By.LINK_TEXT, 'Login')
        enter_email.send_keys(email)
        enter_password.send_keys(password)
        login_button.click()
        pickle_res_button = self.driver.find_element(By.LINK_TEXT, 'Pickleball & Mini Tennis Court Reservations')
        pickle_res_button.click()

    def choose_date_time(self, date, optimal_time):
        """
        Find today's date and click to open calendar.
        Locate date (8 days from today) and click.
        Locate desired time option and click.
        """


