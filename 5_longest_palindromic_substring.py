from typing import List

class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        longestSequence = ""
        longestSequenceLength = 0
        
        for i in range(len(s)):
            # if len(s) is odd
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                tempLength = right - left + 1
                if tempLength > longestSequenceLength:
                    longestSequence = s[left:right + 1]
                    longestSequenceLength = tempLength
                left -= 1
                right += 1
                
            # if len(s) is odd
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                tempLength = right - left + 1
                if tempLength > longestSequenceLength:
                    longestSequence = s[left:right + 1]
                    longestSequenceLength = tempLength
                left -= 1
                right += 1
        
        return longestSequence

if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print(solution.longestPalindrome(s))