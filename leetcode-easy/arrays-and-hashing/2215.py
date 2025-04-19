# LeetCode Question 
    ## 2215. Find the Difference of Two Arrays
# LeetCode Link
    ## https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=a4wqKR-znBE&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_not_in_nums2 = set()
        nums2_not_in_nums1 = set()
        for each_number in nums1:
            if each_number not in nums2:
                nums1_not_in_nums2.add(each_number)

        for each_number in nums2:
            if each_number not in nums1:
                nums2_not_in_nums1.add(each_number)
        return [list(nums1_not_in_nums2), list(nums2_not_in_nums1)]

sol = Solution()

# Example 1
nums11 = [1,2,3]
nums21 = [2,4,6]
print(sol.findDifference(nums11, nums21))

# Example 2
nums12 =[1,2,3,3]
nums22 = [1,1,2,2]
print(sol.findDifference(nums12, nums22))