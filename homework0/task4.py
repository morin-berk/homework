from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    """
    Given four lists A, B, C, D of integer values, the func
    computes how many tuples (i, j, k, h)
    there are such that A[i] + B[j] + C[k] + D[h] is zero.
    """
    num_tuples = 0
    assert len(a) == len(b) == len(c) == len(d)
    for i in a:
        for j in b:
            for k in c:
                for h in d:
                    if i + j + k + h == 0:
                        num_tuples += 1
    return num_tuples
