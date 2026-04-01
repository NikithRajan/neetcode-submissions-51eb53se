class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i , j , maxlen = 0 , 0 , 0
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            j +=1 
            maxlen = max(maxlen , j - i)
        return maxlen