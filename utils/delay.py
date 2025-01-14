import time
import random
from datetime import datetime

def random_wait(min_wait=0.5, max_wait=1.1):
    """
    Creates a random wait time with a default minimum and maximum.
    Min and max can be adjusted to higher or lower depending on website
    elements loading times.
    """
    wait_time = random.uniform(min_wait, max_wait)
    time.sleep(wait_time)

def schedule_delay(start_time, time_format="%I:%M %p"):
    """
    Creates a delay equal to the amount of time between the end of execution
    of the previous function and the desired start time of the following
    functions.
    """
    now_datetime = datetime.now()
    target_time = datetime.strptime(start_time, time_format).time()
    target_datetime = datetime.combine(now_datetime.date(), target_time)
    wait_time = target_datetime - now_datetime
    wait_time_s = wait_time.total_seconds() - 0.04
    time.sleep(wait_time_s)
    
