# LeetCode Question 
    ## 2073. Time Needed to Buy Tickets
# LeetCode Link
    ## https://leetcode.com/problems/time-needed-to-buy-tickets/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=cVmS9N6kf2Y&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        d = {}
        _cnt = 0
        for i in range(len(tickets)):
            d[i] = tickets[i]
        while(1):
            if d[k] == 0:
                return _cnt
            first_key = next(iter(d))
            if d[first_key] == 0:
                d.pop(first_key)
                continue
            d[first_key] = d[first_key] - 1
            value = d[first_key]
            d.pop(first_key)
            d[first_key] = value
            _cnt += 1
    

sol = Solution()

# Example 1
tickets1 = [2,3,2]
k1 = 2
print(sol.timeRequiredToBuy(tickets1, k1))

# Example 2
tickets2 = [5,1,1,1]
k2 = 0
print(sol.timeRequiredToBuy(tickets2, k2))