class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp="".join(s.split(" "))
        new_temp=[c.lower() for c in temp if c.isalnum()]
        mid=(len(new_temp)//2)
        i=0
        while(i<mid):
            if(new_temp[i]==new_temp[-i-1]):
                i+=1
                continue
            else:
                return False
            
        return True

        
        