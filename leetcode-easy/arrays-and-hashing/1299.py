# LeetCode Question 
    ## 1299. Replace Elements with Greatest Element on Right Side
# LeetCode Link
    ## https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=ZHjKhUjcsaU&ab_channel=NeetCode


from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        length = len(arr)
        curr_max = arr[length-1]
        n = length - 2
        while(n >= 0):
            temp = arr[n]
            arr[n] = curr_max
            if temp > curr_max:
                curr_max = temp
            n = n -1
        arr[-1] = -1
        return arr
        

sol = Solution()

# Example 1
arr1 = [17,18,5,4,6,1]
print(sol.replaceElements(arr1))

# Example 2
arr2 = [400]
print(sol.replaceElements(arr2))