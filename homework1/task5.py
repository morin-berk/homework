from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Given a list of integers numbers "nums", the func finds
    a sub-array with length less or equal to "k", with maximal sum.
    It returns the sum of this sub-array.
    """
    if k > len(nums):
        k = len(nums)
    final_max_value = nums[0]
    index_counter = 1
    for el in range(k + 1):
        first_el, last_el = 0, index_counter
        while last_el <= len(nums) and index_counter <= k:
            curr_max_value = sum((nums[first_el:last_el]))
            first_el += 1
            last_el += 1
            if curr_max_value > final_max_value:
                final_max_value = curr_max_value
        last_el = index_counter + 1
        index_counter = last_el
    return final_max_value
