class Solution:
    def jumpR(self, current, end, jump, nums):
        if current >= end: return True
        if jump == 0: return False

        for ch in range(1, jump + 1):
            if current + ch >= end: return True
            if self.jumpR(current + ch, end, nums[current + ch], nums): return True

        return False



    def canJumpRicorsiva(self, nums: List[int]) -> bool:
        return self.jumpR(0, len(nums) - 1, nums[0], nums)

    def canJumpGreedy(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        final_dest = len(nums) - 1
        current_pos = len(nums) - 2

        while final_dest > 0:
            if current_pos < 0: return False
            jumps = nums[current_pos]
            if current_pos + jumps >= final_dest:
                #sposta final_dest all'indietro 
                final_dest = current_pos
            current_pos -=1

        return True

    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpGreedy(nums)
        
        
