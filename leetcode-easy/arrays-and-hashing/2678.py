# LeetCode Question 
    ## 2678. Number of Senior Citizens
# LeetCode Link
    ## https://leetcode.com/problems/number-of-senior-citizens/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=l6_wwKzFmVo&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for each_string in details:
            age = int(each_string[11:13])
            if age > 60:
                count += 1
        return count


sol = Solution()

# Example 1
details1 = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(sol.countSeniors(details1))

# Example 2
details2 = ["1313579440F2036","2921522980M5644"]
print(sol.countSeniors(details2))
