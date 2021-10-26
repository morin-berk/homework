import hashlib
import random
import struct
import time
from multiprocessing import Pool, freeze_support


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def multiprocessing():
    """Running a func through multiprocessing module"""
    p = Pool(processes=45)
    result = p.map(slow_calculate, range(1, 501))
    p.close()
    p.join()
    return result


if __name__ == '__main__':
    freeze_support()
    print(sum(multiprocessing()))
