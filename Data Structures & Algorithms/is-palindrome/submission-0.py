class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for i in s:
            if i.isalnum():
                newstr += i.lower()
        if(newstr != newstr[::-1]):
            return False
        return True
        