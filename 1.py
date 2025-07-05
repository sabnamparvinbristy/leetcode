from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = i

        for i in range(len(nums)):
            b = target - nums[i]
            if b in a and a[b] != i:
                return [i, a[b]]