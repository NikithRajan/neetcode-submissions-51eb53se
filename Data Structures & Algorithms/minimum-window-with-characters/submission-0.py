class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #your code goes here
        n = len(s)
        m = len(t)
        sIndex = -1
        minVal = float('inf')

        for i in range(n):
            hash = [0] * 256
            for c in t:
                hash[ord(c)] +=1
            count = 0

            for j in range(i,n):
                if hash[ord(s[j])] > 0:
                    count +=1
                hash[ord(s[j])] -=1

                if count == len(t):
                    if j-i+1<minVal:
                        minVal = j-i+1
                        sIndex = i
        if sIndex != -1:
            return s[sIndex : sIndex + minVal]
        else:
            return ""
        

        

