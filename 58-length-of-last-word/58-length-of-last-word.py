class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_last = 0 # O(1)
        if len(s)==0 and s[0]!=" ":
            return 1
        for i in range(len(s)-1, -1, -1): # O(n)
            # print(i)
            if len_last > 0 and s[i]==" ":
                return len_last
            elif s[i]!=" ":
                len_last += 1
        return len_last