from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    """
    Given four lists A, B, C, D of integer values, the func
    computes how many tuples (i, j, k, h)
    there are such that A[i] + B[j] + C[k] + D[h] is zero.
    """
    sum_zero = 0
    sum_first_two = [(el1 + el2) for el1 in a for el2 in b]
    sum_second_two = [(el3 + el4) for el3 in c for el4 in d]
    for sum1 in sum_first_two:
        for sum2 in sum_second_two:
            if sum1 + sum2 == 0:
                sum_zero += 1
    return sum_zero
