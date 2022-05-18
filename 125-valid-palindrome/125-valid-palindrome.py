class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "" # space: O(n)
        for char in s: # time: O(n)
            if char.isalnum():
                newStr += char.lower()
                
        return newStr == newStr[::-1]