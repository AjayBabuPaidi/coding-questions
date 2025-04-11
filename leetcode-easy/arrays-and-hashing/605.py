# LeetCode Question 
    ## 605. Can Place Flowers
# LeetCode Link
    ## https://leetcode.com/problems/can-place-flowers/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=ZGxqqjljpUI&ab_channel=NeetCode




from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        le = len(flowerbed)
        new_flowerbed = [0] + flowerbed + [0]
        for i in range(1, le+1):
            if new_flowerbed[i] == 0 and new_flowerbed[i-1] == 0 and new_flowerbed[i+1] == 0:
                new_flowerbed[i] = 1
                n = n-1
        return n<=0
        
sol = Solution()

# Example 1
flowerbed1 = [1,0,0,0,1]
n1 = 1
print(sol.canPlaceFlowers(flowerbed1, n1))

# Example 2
flowerbed2 = [1,0,0,0,1]
n2 = 2
print(sol.canPlaceFlowers(flowerbed2, n2))