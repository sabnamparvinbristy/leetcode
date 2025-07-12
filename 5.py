class Solution:
    def longestPalindrome(self, s: str) -> str:
        a = 0
        b = 0

        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)       
            len2 = expandAroundCenter(s, i, i + 1)   

            len3 = max(len1, len2) 

            if len3 > b - a:
                a = i - (len3 - 1) // 2
                b = i + len3 // 2

        return s[a:b + 1]


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1
