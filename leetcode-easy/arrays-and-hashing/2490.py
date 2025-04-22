# LeetCode Question 
    ## 2490. Circular Sentence
# LeetCode Link
    ## https://leetcode.com/problems/circular-sentence/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=9Ty_eRjoDNM&ab_channel=NeetCodeIO



class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")
        if len(s) == 1:
            if s[0][0] == s[0][-1]:
                return True
            return False
        for i in range(1, len(s)):
            if s[i][0] != s[i-1][-1]:
                return False
        if s[-1][-1] != s[0][0]:
            return False
        return True
        

sol = Solution()

# Example 1
sentence1 = "leetcode exercises sound delightful"
print(sol.isCircularSentence(sentence1))

# Example 2
sentence2 = "eetcode"
print(sol.isCircularSentence(sentence2))

# Example 3
sentence3 = "Leetcode is cool"
print(sol.isCircularSentence(sentence3))

# Example 4
sentence4 = 'leetcode'
print(sol.isCircularSentence(sentence4))

# Example 5
sentence5 = "Leetcode eisc cool"
print(sol.isCircularSentence(sentence5))