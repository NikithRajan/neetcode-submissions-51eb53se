class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = set()
        temp = []
        
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1): 
                for k in range(j+1,len(nums)):
                    summ=nums[i] + nums[j] + nums[k]
                    if summ == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        triplet.add(tuple(temp))
        ans = [list(triple) for triple in triplet]
        return ans
        

                    
            
        