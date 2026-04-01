from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp = {}
        for num in nums:
            mpp[num] = 1 + mpp.get(num,0)
        for freq in mpp.values():
            if freq > 1:
                return True
        return False