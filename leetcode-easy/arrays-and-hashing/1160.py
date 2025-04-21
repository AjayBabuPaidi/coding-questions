# LeetCode Question 
    ## 1160. Find Words That Can Be Formed by Characters
# LeetCode Link
    ## https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=EQ5jTZdEn8Y&ab_channel=NeetCodeIO


from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        _sum = 0
        for each_word in words:
            flag = False
            s = Counter(chars)
            for each_char in each_word:
                if each_char in s and s[each_char] >= 1:
                    s[each_char] = s[each_char] - 1
                    continue
                else:
                    flag = True
                    break

            if flag == False:
                _sum = _sum + len(each_word)
        return _sum
    

sol = Solution()

# Example 1
words1 = ["cat","bt","hat","tree"]
chars1 = "atach"
print(sol.countCharacters(words1, chars1))

# Example 1
words2 = ["hello","world","leetcode"]
chars2 = "welldonehoneyr"
print(sol.countCharacters(words2, chars2))