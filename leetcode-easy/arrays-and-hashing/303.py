# LeetCode Question 
    ## 303. Range Sum Query - Immutable
# LeetCode Link
    ## https://leetcode.com/problems/range-sum-query-immutable/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=2pndAmo_sMA&ab_channel=NeetCodeIO


from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        _sum = 0
        for i in range(left, right+1):
            _sum = _sum + self.nums[i]
        return _sum
    


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0,2))