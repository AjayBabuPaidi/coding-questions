# LeetCode Question 
    ## 49. Group Anagrams
# LeetCode Link
    ## https://leetcode.com/problems/group-anagrams/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=vzdNOK2oB2E&ab_channel=NeetCode


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            s1 = "".join(sorted(strs[i]))
            if s1 in d:
                d[s1].append(strs[i])
            else:
                d[s1] = [strs[i]]
        return list(d.values())

        
sol = Solution()

# Example 1
strs1 = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs1))

# Example 2
strs2 = [""]
print(sol.groupAnagrams(strs2))

# Example 3
strs3 = ["a"]
print(sol.groupAnagrams(strs3))