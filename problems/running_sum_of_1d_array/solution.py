class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        running_sum = []

        for num in nums:
            total += num
            running_sum.append(total)
        return running_sum