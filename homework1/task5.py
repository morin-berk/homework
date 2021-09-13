from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Given a list of integers numbers "nums", the func finds
    a sub-array with length less or equal to "k", with maximal sum.
    It returns the sum of this sub-array.
    """
    if k > len(nums):
        k = len(nums)
    max_value = sum(nums[:k])
    for el in range(k + 1):
        i, n = 0, el
        while len(nums) >= n:
            max_value1 = sum((nums[i:n]))
            i += 1
            n += 1
            if max_value1 > max_value:
                max_value = max_value1
    return max_value
