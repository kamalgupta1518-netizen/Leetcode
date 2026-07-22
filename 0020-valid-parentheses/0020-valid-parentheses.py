class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 !=0:
            return False
        stack=[]    
        map={')':'(','}':'{',']':'['} 
        for i in s:
            if i in map:
                top=stack.pop() if stack else '#'  
                if map[i] != top:
                    return False
            else:
                stack.append(i)      
        return len(stack)==0
    



        