class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        l = 0 ; r = len(nums) - 1
        minval = nums[-1]
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] <= minval:
                minval = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        return minval
