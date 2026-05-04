class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return False
        memory_set=set()
        for i in nums:
            if(i in memory_set):
                return True
            memory_set.add(i)
        return False
         