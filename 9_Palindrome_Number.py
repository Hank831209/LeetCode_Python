# Description
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        b = a[::-1]
        if a == b:
            return True
        else:
            return False


x = 121
Ans = Solution()
ans = Ans.isPalindrome(x)
print(ans)
