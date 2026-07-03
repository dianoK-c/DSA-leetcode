class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = [c.lower() for c in s if c.isalnum()]
        cleaned = ''.join(cleaned)
        return self.check(cleaned, 0, len(cleaned))
    
    def check(self, s, i, n):
        if i >= n - i - 1:
            return True
        if s[i] != s[n - i - 1]:
            return False
        return self.check(s, i + 1, n)