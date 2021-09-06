from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Given a list of integers numbers "nums", the func finds
    a sub-array with length equal to "k", with maximal sum.
    It returns the sum of this sub-array.
    """
    def sum_of_el(k_list):
        sum_el = 0
        for el in k_list:
            sum_el += el
        return sum_el

    assert len(nums) >= k, 'The length of the list is smaller than k'

    max_value = sum_of_el(nums[:k])

    while len(nums) > k:
        nums = nums[1:]
        max_value1 = sum_of_el(nums[:k])
        if max_value1 > max_value:
            max_value = max_value1
    return max_value
