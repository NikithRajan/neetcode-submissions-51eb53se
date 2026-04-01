class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup = set()
        for num in nums:
            if num in nodup:
                return True
            else:
                nodup.add(num)
        return False
        