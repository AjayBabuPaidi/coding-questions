# LeetCode Question 
    ## 1122. Relative Sort Array
# LeetCode Link
    ## https://leetcode.com/problems/relative-sort-array/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=OPvcR1e4lfg&ab_channel=NeetCodeIO


from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq_arr1 = Counter(arr1)
        s = set()
        final1 = []
        final2 = []
        for each_number in arr2:
            if each_number in freq_arr1 and each_number not in s:
                final1.extend([each_number] * freq_arr1[each_number])
                s.add(each_number)
        
        for each_number in arr1:
            if each_number not in s:
                final2.extend([each_number] * freq_arr1[each_number])
                s.add(each_number)
        return final1 + list(sorted(final2))

sol = Solution()

# Example 1
arr11 = [2,3,1,3,2,4,6,7,9,2,19]
arr21 = [2,1,4,3,9,6]
print(sol.relativeSortArray(arr11, arr21))

# Example 2
arr12 = [28,6,22,8,44,17]
arr22 = [22,28,8,6]
print(sol.relativeSortArray(arr12, arr22))