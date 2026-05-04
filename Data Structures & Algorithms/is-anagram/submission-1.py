class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if(len(s)!=len(t)):
        return False
       A=[0]*26
       for i,n in enumerate(s):
        A[ord(n)-97]+=1
       for j,n in enumerate(t):
        if(A[ord(n)-97]==0):
            return False
        A[ord(n)-97]-=1
       return True
        