# LeetCode Question 
    ## 1684. Count the Number of Consistent Strings
# LeetCode Link
    ## https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=d-ulaeRBA64&ab_channel=NeetCodeIO



from collections import Counter
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        count = 0
        for each_string in words:
            c = Counter(each_string)
            flag = True
            for each_key in c.keys():
                if each_key not in s:
                    flag = False
                    break
            if flag == True:
                count += 1
        return count
            
        
sol = Solution()

# Example 1
allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]
print(sol.countConsistentStrings(allowed1, words1))

# Example 2
allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]
print(sol.countConsistentStrings(allowed2, words2))


# Example 3
allowed3 = "cad"
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]
print(sol.countConsistentStrings(allowed3, words3))