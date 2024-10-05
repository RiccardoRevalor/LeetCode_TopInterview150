class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x: x[0])

        res = []

        for int in intervals:
            if len(res) == 0 or res[-1][1] < int[0]: #non-overlapping condition
                res.append(int)
            else:
                #merge
                res[-1][1] = max(res[-1][1], int[1])
        return res


            
        
