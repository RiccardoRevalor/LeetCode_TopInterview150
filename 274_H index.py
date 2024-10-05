class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_max = 0
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if i + 1 <= citations[i]: h_max = i+1
        
        return h_max
        

        





        
