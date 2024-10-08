class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        res = [0]*l
        for i in range(l):
            new_index = (i+k)%l
            res[new_index] = nums[i]

        nums[:] = res
        
