"""
Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring
case.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_gen = ""
        for i in s:
            if i.isalnum():
                str_gen += i.lower()
        return str_gen == str_gen[::-1]
    
    def isPalindromeTwoPointers(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left+=1
            while right > left and not s[right].isalnum():
                right-=1
            
            if s[left].lower() != s[right].lower():
                return False

            left+=1
            right-=1
        
        return True