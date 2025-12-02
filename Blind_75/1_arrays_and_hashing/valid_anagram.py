"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tab_1 = {}
        tab_2 = {}

        for i in range(len(s)):
            tab_1[s[i]] = tab_1.get(s[i],0) + 1
            tab_2[t[i]] = tab_2.get(t[i],0) + 1
    
        for k,v in tab_1.items():
            if k in tab_2.keys() and tab_2.get(k,-1) == v:
                continue
            return False 

        return True