# LeetCode Question 
    ## 2053. Kth Distinct String in an Array
# LeetCode Link
    ## https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=1KOnvGPv9Mo&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        final = ""
        i = 1
        for each in arr:
            d[each] = d.get(each, 0) + 1
        
        for each in arr:
            if d[each] == 1 and i == k:
                final = each
                return final
            if d[each] == 1 and i != k:
                i += 1
        return final
            

sol = Solution()

# Example 1
arr1 = ["d","b","c","b","c","a"]
k1 = 2
print(sol.kthDistinct(arr1, k1))

# Example 2
arr2 = ["aaa","aa","a"]
k2 = 1
print(sol.kthDistinct(arr2, k2))

# Example 3
arr3 = ["a","b","a"]
k3 = 3
print(sol.kthDistinct(arr3, k3))
