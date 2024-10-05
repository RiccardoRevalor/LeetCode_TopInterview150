class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        res = 0
        right = -1
        for p in points:
            if right == -1:
                #new shoot!
                res += 1
                right = p[1]
            else:
                #can i burst other balloons w the previous shoot?
                if p[0] <= right:
                    right = min(right, p[1]) #right ogni volta è il minimo tra le right!!
                else:
                    #no: new shoot
                    res += 1
                    right = p[1]
        return res



        
        
