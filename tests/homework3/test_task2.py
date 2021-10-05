import time

from homework3.task2 import multiprocessing


def test_multiprocessing_work_time():
    """
    Testing if multiprocessing
    takes up no more than a minute
    """
    start_time = time.time()
    sum(multiprocessing())
    total_time = time.time() - start_time
    assert total_time < 60.0
