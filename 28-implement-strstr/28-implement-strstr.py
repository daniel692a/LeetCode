class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        elif len(needle)>len(haystack):
            return -1
        
        j = 0 # O(1)
        
        def isTheSame(a, b) -> bool:
            return a==b
        
        for i in range(len(haystack)-len(needle)+1): # O(n)
            
            while j < len(needle):
                if not isTheSame(needle[j], haystack[j+i]):
                    break
                j+=1

            if j==len(needle):
                    return i
            j=0
                
        return -1
        