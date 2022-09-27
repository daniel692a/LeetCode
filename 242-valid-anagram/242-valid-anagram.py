class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        chars1, chars2 = {}, {} # O(n)
        for i in range(len(s)): # O(n)
            if not (s[i] in chars1):
                chars1[s[i]]=0
            else:
                chars1[s[i]] += 1
            
            if not (t[i] in chars2):
                chars2[t[i]] = 0
            else:
                chars2[t[i]] += 1
        
        for key in chars1: # O(k) k -> keys or characters
            if key in chars2:
                if chars2[key] != chars1[key]:
                    return False
            else:
                return False
        return True