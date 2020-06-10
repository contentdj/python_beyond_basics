import datetime
import itertools
import random
import time

class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        return random.random()

sensor = Sensor()
# None is never returned from datetime.datetime.now. This generates an infinite sequence
timestamps = iter(datetime.datetime.now, None)

# https://docs.python.org/2/library/itertools.html#itertools.islice
for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
    print(stamp, value)
    time.sleep(1)
