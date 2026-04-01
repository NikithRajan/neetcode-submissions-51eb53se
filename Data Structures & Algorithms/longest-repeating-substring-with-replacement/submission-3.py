class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        maxlen = 0
        seen = {}
        while r < len(s):
            seen[s[r]] = 1 + seen.get(s[r] , 0)
            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            maxlen = max(maxlen , r - l + 1)
            r += 1
        return maxlen