class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x:x[0])
        n = len(points)
        count = 1
        prev = points[0]
        for i in range(1, len(points)):
            csp = points[i][0]
            cep = points[i][1]
            psp = prev[0]
            pep = prev[1]
        
            if csp > pep:
                count += 1
                prev = points[i]
            else:
                prev[0] = max(psp, csp)
                prev[1] = min(pep, cep)

        return count
        

        