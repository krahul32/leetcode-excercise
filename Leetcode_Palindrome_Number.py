"""


Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return 0
        else:
            y = str(x)
            y = y [::-1]
            if(x==int(y)):
                return 1
            else:
                return 0