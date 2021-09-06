""" Check: is the number a power of two """


def check_power_of_2(a: int) -> bool:
    if a != 0 and a not in [True, False]:
        return not bool(a & (a - 1))
    return False
