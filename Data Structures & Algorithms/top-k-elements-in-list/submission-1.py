from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for i in range(len(nums)+1)]
        for key,value in count.items():
            freq[value].append(key)
        res=[]
        for j in range(len(freq)-1,0,-1):
            for i in freq[j]:
                res.append(i)
                if(len(res)==k):
                    return res

        
        