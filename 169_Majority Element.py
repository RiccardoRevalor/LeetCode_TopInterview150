class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        app = {}
        cond = len(nums) / 2
        for num in nums:
            if num in app:
                app[num] +=1
            else: app[num] = 1
        for key in app:
            if app[key] > cond: return key
