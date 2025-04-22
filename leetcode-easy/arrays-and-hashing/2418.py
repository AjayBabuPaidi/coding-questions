# LeetCode Question 
    ## 2418. Sort the People
# LeetCode Link
    ## https://leetcode.com/problems/sort-the-people/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=Zv_gXqqslbw&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lt = zip(names, heights)
        final = []
        sorted_list = list(sorted(lt, key = lambda x: x[1], reverse = True))
        for each_item in sorted_list:
            final.append(each_item[0])
        return final
        

sol = Solution()

# Example 1
names1 = ["Mary","John","Emma"]
heights1 = [180,165,170]
print(sol.sortPeople(names1, heights1))

# Example 2
names2 = ["Alice","Bob","Bob"]
heights2 = [155,185,150]
print(sol.sortPeople(names2, heights2))