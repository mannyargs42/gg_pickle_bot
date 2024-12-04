from utils.web_scraper import WebScraper
from utils.datetime_calculator import format_date, format_time

def main():
    """
    Orchestrates automated tasks from utils in order and books a reservation
    at the desired time +0, 0.5 or 1 hour.

    *url: GGP court reservation website.
    *email and password: for GGP court reservation website.
    *days_ahead: days ahead the the website will allow you to book.
    *desired_time: ideal time you want to reserve a court in format 'XX:XX XM'.
    """

    url = ""
    email = ""
    password = ""
    days_ahead = 
    desired_time = ""

    today, target_date = format_date(days_ahead)
    target_time = format_time(desired_time)
    scraper = WebScraper()
    scraper.navigator(url)
    scraper.login_to_reserve(email, password)
    scraper.choose_date_time(today, target_date, target_time)
    scraper.finish_booking()


if __name__ == "__main__":
    main()