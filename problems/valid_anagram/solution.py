class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_count = {}

        for char in s:
            seen_count[char] = seen_count.get(char, 0) + 1

        for char in t:
            if char not in seen_count:
                return False
            seen_count[char] -= 1

        return all(count == 0 for count in seen_count.values())