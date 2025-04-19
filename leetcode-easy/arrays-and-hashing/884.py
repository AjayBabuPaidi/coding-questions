# LeetCode Question 
    ## 884. Uncommon Words from Two Sentences
# LeetCode Link
    ## https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=24IYW1kQdYU&ab_channel=NeetCodeIO


from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d1 = Counter(s1.split(' '))
        d2 = Counter(s2.split(' '))
        final = []
        for k,v in d1.items():
            if v == 1 and k not in d2:
                final.append(k)
        for k,v in d2.items():
            if v == 1 and k not in d1:
                final.append(k)   
        return final
    

sol = Solution()

# Example 1
s11 = "this apple is sweet"
s21 = "this apple is sour"
print(sol.uncommonFromSentences(s11, s21))

# Example 2
s12 = "apple apple"
s22 = "banana"
print(sol.uncommonFromSentences(s12, s22))
