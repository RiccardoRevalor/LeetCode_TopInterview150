class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        current = 0
        end = len(nums) - 1
        coverage = 0
        jumps = 0

        for i in range(len(nums)):
            coverage = max(coverage, nums[i] + i)

            if i == current:
                current = coverage
                jumps +=1

                if current >= end: return jumps
            




        
