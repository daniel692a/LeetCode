class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = { ")": "(", "]": "[", "}": "{" }
        stack = []
        for l in s:
            if ((l=="{") or (l=="(") or (l=="[")):
                stack.append(l)
            elif ((l=="]") or (l==")") or (l=="}")) and len(stack)==0:
                return False
            elif len(stack)>0:
                if ((l==")") and (stack[-1]=="(")):
                    stack.pop()
                elif ((l=="]") and (stack[-1]=="[")):
                    stack.pop()
                elif ((l=="}") and (stack[-1]=="{")):
                    stack.pop()
                else:
                    return False
        return False if len(stack)>0 else True
                  
                