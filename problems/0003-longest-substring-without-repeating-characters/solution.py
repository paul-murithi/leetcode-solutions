class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        seen = {}

        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right
            right += 1

            max_length = max(max_length, right - left)
        return max_length
