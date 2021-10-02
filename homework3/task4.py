def is_armstrong(number: int) -> bool:
    """
    Checking whether a num is an Armstrong num
    """
    sep_num = list(map(int, list(str(number))))
    check = list(map(lambda x: x**len(sep_num), sep_num))
    return sum(check) == number
