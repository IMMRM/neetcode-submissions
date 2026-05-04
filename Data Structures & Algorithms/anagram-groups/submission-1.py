from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)
        for i in strs:
            key=[0]*26
            for j in range(len(i)):
                a=97-ord(i[j])
                key[a]+=1
            hash_map[tuple(key)].append(i)
        return hash_map.values()



        