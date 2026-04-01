class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmapp = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevmapp:
                return [prevmapp[diff],i]
            prevmapp[nums[i]] = i 
            