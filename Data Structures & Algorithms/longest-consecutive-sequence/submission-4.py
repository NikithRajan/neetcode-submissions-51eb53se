class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in res:
                streak = 1
                while (n + streak) in res:
                    streak += 1
                longest = max(longest , streak)
        return longest
        


        