class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle)>len(haystack):
            return -1
        n_ptr, h_ptr = 0, 0
        
        for i in range(len(haystack)):
            
            if haystack[i]==needle[0]:
                h_ptr = i
                while n_ptr<len(needle):
                    if (h_ptr < len(haystack) and (n_ptr == len(needle)-1) and (needle[n_ptr] == haystack[h_ptr])):
                        return i
                    elif ((h_ptr < len(haystack)) and (needle[n_ptr] == haystack[h_ptr])):
                        h_ptr+=1
                        n_ptr+=1
                    else:
                        n_ptr=0
                        break

        return -1
        