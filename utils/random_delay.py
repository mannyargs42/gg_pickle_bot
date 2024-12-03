import time
import random

def random_wait(min_wait=0.5, max_wait=1.1):
    """
    Creates a random wait time with a default minimum and maximum.
    Min and max can be adjusted to higher or lower depending on website
    elements loading times.
    """
    wait_time = random.uniform(min_wait, max_wait)
    time.sleep(wait_time)