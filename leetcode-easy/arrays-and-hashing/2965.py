# LeetCode Question 
    ## 2965. Find Missing and Repeated Values
# LeetCode Link
    ## https://leetcode.com/problems/find-missing-and-repeated-values/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=LQGmWiDuTw8&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = {}
        n = len(grid)
        final = []
        for i in range(n):
            for j in range(n):
                d[grid[i][j]] = d.get(grid[i][j], 0) + 1
        
        for k,v in d.items():
            if v == 2:
                final.append(k)
                break
        for i in range(1, (n*n)+1):
            if i not in d:
                final.append(i)
                break
        return final
        

sol = Solution()

# Example 1
grid1 = [[1,3],[2,2]]
print(sol.findMissingAndRepeatedValues(grid1))

# Example 2
grid2 = [[9,1,7],[8,9,2],[3,4,6]]
print(sol.findMissingAndRepeatedValues(grid2))

