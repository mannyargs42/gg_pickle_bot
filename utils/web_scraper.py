from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from utils.delay import random_wait, schedule_delay
from utils.datetime_calculator import format_time

"""
Use Selenium to automate browser interactions.

Use WebScraper class functions in order to navigate the target website and
book a court reservation.

random_waits is imported to create random delays to simulate human behavior.
At 0.5-1.1 and current settings: max total time is 15.7s, min time is 7.5s.

"""

class WebScraper:
    def __init__(self):
        """
        Instantiate Selenium ChromeDriver and open web browser.
        Instantiate the time_button as it is used in >1 method.
        """
        self.driver = webdriver.Chrome()
        self.today = None
        self.target_date = None
        self.target_time = None

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
        --
        Navigating the new page requires hovering over elements to expose
        the ones we need to click into. Selenium's execute_script method
        lets us execute JS code to interact with dynamic elements, as in
        this in this order:
        Locate the "Reservations" hover element.
        Locate the "Pickleball and mini tennis reservations" from the
        "Reservations" drop-down menu.
        Use execute_script to hover and then click into pickleball reservations.
        """
        random_wait()
        login_button = self.driver.find_element(By.LINK_TEXT, "LOG IN")
        login_button.click()
        random_wait()
        enter_email = self.driver.find_element(By.ID, "UserNameOrEmail")
        enter_password = self.driver.find_element(By.ID, "Password")
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Login']")
        enter_email.send_keys(email)
        enter_password.send_keys(password)
        random_wait()
        login_button.click()

    def go_to_calendar(self, slot_time):
        schedule_delay(slot_time)
        hover_res_element = self.driver.find_element(By.XPATH, "//div//span[text()='Reservations']")
        pickle_res_button = hover_res_element.find_element(By.XPATH, "//div//span[text()='Pickleball & Mini Tennis Court Reservations']")
        random_wait()
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('mouseover')); arguments[1].click();", hover_res_element, pickle_res_button)

    def choose_date_time(self, today, target_date, target_time):
        """
        Find today's date and click to open calendar.
        Locate date (8 days from today) and click.
        Locate desired time option and click.
        """
        self.today = today
        self.target_date = target_date
        self.target_time = target_time
        random_wait()
        calendar_button = self.driver.find_element(By.XPATH, f"//div//span[contains(text(), '{self.today}')]")
        calendar_button.click()
        random_wait()
        date_button = self.driver.find_element(By.XPATH, f"//a[contains(@title, '{self.target_date}')]")
        date_button.click()
        random_wait(min_wait=1, max_wait=2)
        max_tries = 10
        while max_tries > 0:
            try:
                time_button = self.driver.find_element(By.XPATH, f"//a[contains(@data-href, '{self.target_time}')]")
            except NoSuchElementException:
                print(f"NoSuchElementException {max_tries}, {self.target_time}")
                self.target_time = self.target_time.replace("&end", "")
                self.target_time = self.target_time.replace("%20", " ")
                self.target_time = self.target_time.lstrip()
                self.target_time = format_time(self.target_time, time_changes=[0.5])
                max_tries -= 1
            else:
                break
        time_button.click()

    def finish_booking(self):
        """
        Change duration to "1 hour & 30 minutes" from drop-down.
        Click "Check to agree to above disclosure" box.
        Click "Save" to finish booking.
        """
        max_tries = 5
        wait_time = 3
        while max_tries > 0:
            try:
                duration_button = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable((By.XPATH, "//div//span[contains(text(), '1 hour')]"))
                )
            except TimeoutException:
                print(f"TimeoutException {max_tries}")
                self.driver.refresh()
                self.choose_date_time(self.target_date, self.target_date, self.target_time)
                wait_time += 2
                max_tries -= 1
            else:
                break
        duration_button.click()
        random_wait(min_wait=1, max_wait=2)
        newtime_button = self.driver.find_element(By.XPATH, "//li//span[contains(text(), '1 hour & 30 minutes')]")
        self.driver.execute_script("arguments[0].click();", newtime_button)
        checktoagree_button = self.driver.find_element(By.XPATH, "//div//span//label[contains(text(), 'Check to agree to above disclosure')]")
        checktoagree_button.click()
        random_wait()
        save_button = self.driver.find_element(By.XPATH, "//div//button[contains(text(), 'Save')]")
        save_button.click()
        print("made it all the way")
