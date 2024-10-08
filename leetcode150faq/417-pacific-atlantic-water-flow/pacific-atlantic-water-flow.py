from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights), len(heights[0])
        visited_p = set()
        visited_a = set()
        row_col_list = [(1,0),(-1,0),(0,1),(0, -1)]
        set_p = set()
        set_a = set()
        que_p = deque()
        que_a = deque()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    set_p.add((r,c))
                    que_p.append((r, c, heights[r][c]))
                    visited_p.add((r,c))
                if r == rows - 1 or c == cols -1:
                    set_a.add((r,c))
                    que_a.append((r, c, heights[r][c]))
                    visited_a.add((r,c))
        while que_p:
            rqp, cqp, htqp = que_p.popleft()
            for rl, cl in row_col_list:
                rn = rqp + rl
                cn = cqp + cl
                if 0 <= rn < rows and 0 <= cn < cols and heights[rn][cn] >= htqp and (rn, cn) not in visited_p:
                    set_p.add((rn, cn))
                    que_p.append((rn, cn , heights[rn][cn]))
                    visited_p.add((rn, cn))
        while que_a:
            rqa, cqa, htqa = que_a.popleft()
            for rl, cl in row_col_list:
                rn = rqa + rl
                cn = cqa + cl
                if 0 <= rn < rows and 0 <= cn < cols and heights[rn][cn] >= htqa and (rn, cn) not in visited_a:
                    set_a.add((rn, cn))
                    que_a.append((rn, cn, heights[rn][cn]))
                    visited_a.add((rn ,cn))
        res = []
        for item in set_a:
            if item in set_p:
                res.append(list(item))
        return res

                
        