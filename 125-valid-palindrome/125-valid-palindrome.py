class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
                
        return True if newStr == newStr[::-1] else False