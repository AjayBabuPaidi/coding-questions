# LeetCode Question 
    ## 1189. Maximum Number of Balloons
# LeetCode Link
    ## https://leetcode.com/problems/maximum-number-of-balloons/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=G9xeB2-7PqY&ab_channel=NeetCode



class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        req = "ballon"
        s = {"b", "a", "l", "o", "n"}
        for each_char in text:
            if each_char in s:
                d[each_char] = d.get(each_char, 0) + 1

        for each_char in req:
            if  each_char not in d:
                return 0

        d['l'] = d['l']//2
        d['o'] = d['o'] //2

        return min(d.values())
        

sol = Solution()

# Example 1
text1 = "nlaebolko"
print(sol.maxNumberOfBalloons(text1))

# Example 2
text2 = "loonbalxballpoon"
print(sol.maxNumberOfBalloons(text2))

# Example 3
text3 = "leetcode"
print(sol.maxNumberOfBalloons(text3))