class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for word in s:
            if word.isalnum():
                new += word.lower()
        if new != new[::-1]:
            return False
        return True
            
        