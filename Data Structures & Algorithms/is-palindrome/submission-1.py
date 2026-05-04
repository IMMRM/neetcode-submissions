class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp="".join(s.split(" "))
        new_s=[ele.lower() for ele in temp if ele.isalnum()]
        mid=(len(new_s)//2)
        i=0
        while(i<mid):
            if(new_s[i]==new_s[-i-1]):
                i+=1
                continue
            return False
        return True
        