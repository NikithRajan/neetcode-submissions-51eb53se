class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        result=[]

        for s in strs:
            sorted_s = tuple(sorted(s))
            res[sorted_s].append(s)
        
        for value in res.values():
            result.append(value)
        
        return result
        