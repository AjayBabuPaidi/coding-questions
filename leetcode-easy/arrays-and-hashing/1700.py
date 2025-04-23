# LeetCode Question 
    ## 1700. Number of Students Unable to Eat Lunch
# LeetCode Link
    ## https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=d_cvtFwnOZg&t=1s&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(1):
            if len(students) == 0 and len(sandwiches) == 0:
                return 0
            if students[0] == sandwiches[0]:
                students = students[1:len(students)]
                sandwiches = sandwiches[1:len(sandwiches)]
            else:
                if sandwiches[0] not in students[1:len(students)]:
                    return len(students)
                else:
                    students = students[1:len(students)] + [students[0]]
        
            
                
sol = Solution()

# Example 1
students1 = [1,1,0,0]
sandwiches1 = [0,1,0,1]
print(sol.countStudents(students1, sandwiches1))

# Example 2
students2 = [1,1,1,0,0,1]
sandwiches2 = [1,0,0,0,1,1]
print(sol.countStudents(students2, sandwiches2))

