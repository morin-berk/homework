import time
import struct
import random
import hashlib
from multiprocessing import Process, freeze_support


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    print(sum(struct.unpack('<' + 'B' * len(data), data)), end=' ')


def multiprocessing():
    """Running a func through multiprocessing module"""
    if __name__ == '__main__':
        start = time.perf_counter()
        freeze_support()
        processes = []

        for el in range(500):
            a = Process(target=slow_calculate, args=(el,))
            processes.append(a)

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        finish = time.perf_counter()

        print(f'Finished in {round(finish-start, 2)} second(s)')
