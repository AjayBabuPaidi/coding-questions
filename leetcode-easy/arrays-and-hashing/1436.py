# LeetCode Question 
    ## 1436. Destination City
# LeetCode Link
    ## https://leetcode.com/problems/destination-city/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=Hi8vMnnTZHE&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        s = set()
        for each_pair in paths:
            d[each_pair[0]] = d.get(each_pair[0], []) + [each_pair[1]]
            s.add(each_pair[1])
        for each in s:
            if each not in d.keys():
                return each
            
            
sol = Solution()

# Example 1
paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sol.destCity(paths1))

# Example 2
paths2 = [["B","C"],["D","B"],["C","A"]]
print(sol.destCity(paths2))

# Example 3
paths3 = [["A","Z"]]
print(sol.destCity(paths3))
        