from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_list=defaultdict(list)
        for i in range(len(strs)):
            count_key=[0]*26
            for j in range(0,len(strs[i])):
                count_key[ord(strs[i][j])-ord('a')]+=1
            freq_list[tuple(count_key)].append(strs[i])
        return freq_list.values()
            



        
        