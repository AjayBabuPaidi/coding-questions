# LeetCode Question 
    ## 2264. Largest 3-Same-Digit Number in String
# LeetCode Link
    ## https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=vcrOpJQHsSE&ab_channel=NeetCodeIO


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        _max = -1
        for i in range(2, len(num)):
            if (num[i] == num[i-1] ==  num[i-2]):
                temp_num = int(num[i] + num[i-1] + num[i-2])
                if temp_num > _max:
                    _max = temp_num
        if _max == -1:
            return ""
        return str(_max).zfill(3)
    
sol = Solution()

# Example 1
num1 = "6777133339"
print(sol.largestGoodInteger(num1))

# Example 2
num2 = "2300019"
print(sol.largestGoodInteger(num2))

# Example 3
num3 = "42352338"
print(sol.largestGoodInteger(num3))

        


