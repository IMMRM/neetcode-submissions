from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)<1):
            return 0
        elif(len(s)<2):
            return 1
        
        l=0
        charSet=set()
        res=0
        for r in range(len(s)):
            while(s[r] in charSet):
                charSet.remove(s[l])
                l=l+1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res

        