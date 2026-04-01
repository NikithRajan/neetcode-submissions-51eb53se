class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        longest = 1
        if nums==[]:
            return 0
        for i in range(len(nums)):
            st.add(nums[i])
        for it in st:
            if it-1 not in st:
                cnt = 1
                x = it
                while x+1 in st:
                    x+=1
                    cnt+=1
                longest = max(longest,cnt)
        return longest
                


        