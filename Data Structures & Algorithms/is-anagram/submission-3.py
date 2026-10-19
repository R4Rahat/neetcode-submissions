class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj = {}
        if len(s) != len(t):
            return False
        else:
            for i in s:
               if i in obj:
                obj[i] += 1 
               else:
                obj[i] = 1
            for j in t:
                if j in obj:
                    obj[j] -= 1
                else:
                    obj[j] = 1
        
       
        
        for value in obj.values():
            if value != 0:
                return False
            
        
        return True
                