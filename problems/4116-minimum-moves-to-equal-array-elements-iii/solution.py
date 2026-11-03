
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        maximum_element = max(nums)

        for num in nums:
            target_add = maximum_element - num
            if num != maximum_element:
                num += target_add
                moves += target_add
        return moves
