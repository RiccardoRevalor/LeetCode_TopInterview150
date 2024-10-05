class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = []
        if not nums:  # Caso base: lista vuota
            return r
        
        start = end = 0  # Inizializza 'start' ed 'end'
        
        while start < len(nums):
            # Muoviamo 'end' fino a che i numeri sono consecutivi
            end = start
            while end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1
            
            # Se 'start' ed 'end' sono uguali, è un numero singolo
            if start == end:
                r.append(str(nums[start]))
            else:
                r.append(f"{nums[start]}->{nums[end]}")
            
            # Muoviamo 'start' al prossimo numero da considerare
            start = end + 1
        
        return r
