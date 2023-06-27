# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
from datetime import datetime



def wait(seconds):
    time.sleep(seconds)


def my_sin(number):
    return math.sin(number)


def iso_now():
    now = datetime.now()
    iso_format = now.strftime("%Y-%m-%dT%H:%M")
    return iso_format
