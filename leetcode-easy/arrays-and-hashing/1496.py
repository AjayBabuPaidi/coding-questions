# LeetCode Question 
    ## 1496. Path Crossing
# LeetCode Link
    ## https://leetcode.com/problems/path-crossing/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=VWRJBNP7uH8&ab_channel=NeetCodeIO


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = set()
        visited.add((x, y))
        for each_direction in path:
            if each_direction == 'N':
                y += 1
            elif each_direction == 'E':
                x += 1
            elif each_direction == 'S':
                y -= 1
            else:
                x -= 1
    
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False

sol = Solution()

# Example 1
path1 = "NESWW"
print(sol.isPathCrossing(path1))

# Example 2
path2 = "NES"
print(sol.isPathCrossing(path2))