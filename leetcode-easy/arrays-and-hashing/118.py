# LeetCode Question 
    ## 118. Pascal's Triangle
# LeetCode Link
    ## https://leetcode.com/problems/pascals-triangle/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=nPVEaB3AjUM&ab_channel=NeetCode



from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        temp = [1]
        final = [temp]
        while(numRows-1 > 0):
            next_row = self.generate_next_row(temp)
            final.append(next_row)
            temp = next_row
            numRows = numRows-1
        return final


    def generate_next_row(self, arr):
        if len(arr) == 1:
            return [1, 1]
        i = 0
        j = 1
        k = len(arr)-1
        final = []
        while(i < k):
            final.append(arr[i] + arr[j])
            i += 1
            j += 1
        return [1] + final + [1]
        


sol = Solution()

# Example 1
numRows1 = 5
print(sol.generate(numRows1))

# Example 2
numRows1 = 1
print(sol.generate(numRows1))