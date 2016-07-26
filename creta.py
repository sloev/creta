__author__ = "johannes valbjorn"
__license__ = "MIT"
__VERSION__ = "0.0.1"

import time
from contextlib import contextmanager

default_format = "[{taken_min:>02.0f}:{taken_sec:>02.0f} < {left_min:>02.0f}:{left_sec:>02.0f}]"
class Creta():
    def __init__(self, n, average_len=10, format=default_format, strict=False):
        """ Iterator class that predicts iteration end time

        examples:
        eta = Creta(10)
        print next(eta)
        >>> [00:00 < 00:00]
        time.sleep(1)
        print next(eta)
        >>> [00:01 < 00:09]

        :param n: total iterations
         :type n: int
        :param average_len: how many items to use as basis for average
         :type average_len: int
        :param format: which print format to use, if None then iterator only yields None
         :type format: string or None
        :param strict: if StopIteration should be raised when self.num==n
         :type strict: bool
        """
        self.n = n
        self.average_len = average_len
        self.format = format
        self.strict = strict

        self.num = 0
        self.last_time = time.time() 
        self.times = []
        self.time_taken = 0
        self.time_left = 0 
    
    def __iter__(self):
        return self
    
    #python 3 compat
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            current_time = time.time()
            self.times.append(current_time - self.last_time)
            last_time = current_time
            average_index = max(self.num-self.average_len, 0) or self.num
            if average_index:
                average = sum(self.times[average_index:]) / average_index
                self.time_taken = average * self.num
                self.time_left = (self.n * average) - self.time_taken
            self.num += 1
        elif self.strict:
            raise StopIteration()

        if self.format is not None:
            return self.format.format(
                    taken_min=self.time_taken // 60,
                    taken_sec=self.time_taken % 60,
                    left_min=self.time_left // 60,
                    left_sec=self.time_left % 60
                    )

    def update(self, n=1):
        val = None
        for i in range(n):
            val = self.next()
        return val


@contextmanager
def ETA(total_iterations, **kwargs):
    """Manages and yields a Creta instance
    
    example:
    n = 5
    with ETA(n, strict=True) as eta:
        for i in eta:
            print i
            time.sleep(1)
    >>> [00:00 < 00:00]
    >>> [00:01 < 00:08]
    >>> [00:02 < 00:08]
    >>> [00:03 < 00:07]
    ...

    :param total_iterations: how many iterations
     :type total_iterations: int
    """
    creta = Creta(total_iterations, **kwargs)
    yield creta
    del creta
