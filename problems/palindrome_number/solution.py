class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        left = 0
        right = len(num_str) - 1

        while left < right:
            if num_str[left] != num_str[right]:
                return False
            if num_str[left] == num_str[right]:
                left += 1
                right -= 1
        return True
            
        