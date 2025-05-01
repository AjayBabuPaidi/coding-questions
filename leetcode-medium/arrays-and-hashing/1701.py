# LeetCode Question 
    ## 1701. Average Waiting Time
# LeetCode Link
    ## https://leetcode.com/problems/average-waiting-time/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=2fN7uIgCIBA&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        completion_time = customers[0][0] + customers[0][1]
        n = len(customers)
        time = customers[0][1]
        for each_interval in customers[1:]:
            if completion_time > each_interval[0]:
                time = time + (completion_time - each_interval[0]) + each_interval[1]
            else:
                time = time + each_interval[1]

            if completion_time < each_interval[0]:
               completion_time = each_interval[0] + each_interval[1]
            else:
                completion_time = completion_time +  each_interval[1]

        return time / n
    
sol = Solution()

# Example 1
customers1 = [[1,2],[2,5],[4,3]]
print(sol.averageWaitingTime(customers1))

# Example 2
customers2 = [[5,2],[5,4],[10,3],[20,1]]
print(sol.averageWaitingTime(customers2))

        

        