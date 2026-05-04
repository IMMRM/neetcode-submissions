from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_table=defaultdict(int)
        for i in range(len(nums)):
            res=target-nums[i]
            if(res in freq_table):
                return [freq_table[res],i]
            else:
                freq_table[nums[i]]=i
        

        