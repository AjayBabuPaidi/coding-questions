# LeetCode Question 
    ## 929. Unique Email Addresses
# LeetCode Link
    ## https://leetcode.com/problems/unique-email-addresses/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=TC_xLIWl7qY&ab_channel=NeetCode



from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final = set()
        for each_mail in emails:
            final.add(self.is_valid_email(each_mail))
        return len(final)


    def is_valid_email(self, email):
        email, domain = email.split("@")
        email_plus_split = email.split("+")[0]
        corrected_mail = "".join(email_plus_split.split("."))
        return corrected_mail+"@"+domain
    

sol = Solution()

# Example 1
emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(sol.numUniqueEmails(emails1))

# Example 2
emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(sol.numUniqueEmails(emails2))