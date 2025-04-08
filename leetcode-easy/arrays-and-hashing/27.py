# LeetCode Question 
    ## 27. Remove Element
# LeetCode Link
    ## https://leetcode.com/problems/remove-element/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=Pcd1ii9P9ZI&ab_channel=NeetCode


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        temp = []
        count = 0
        for each in nums:
            if each != val:
                count += 1
                temp.append(each)
        j = 0
        for i in range(len(temp)):
            nums[j] = temp[i]
            j += 1

        return count
        

sol = Solution()

# Example 1
nums1 = [3,2,2,3]
val1 = 3
print(sol.removeElement(nums1, val1))

# Example 2
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(sol.removeElement(nums2, val2))