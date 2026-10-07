class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            result_sum = numbers[left] + numbers[right]

            if result_sum == target:
                break
            elif result_sum > target:
                right -= 1
            elif result_sum < target:
                left += 1
        return [left + 1, right + 1]