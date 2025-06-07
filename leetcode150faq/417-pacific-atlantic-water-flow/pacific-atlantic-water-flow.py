class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #we will use dfs
        #first_row/last_row -> pac/altan
        #frist_col/last_col -> pac/alan
        #find the matching
        row_len , col_len = len(heights), len(heights[0])
        pac, atl = set(), set()
        drs = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row, col, visited, prev_height):
            if (row, col) in visited or row < 0 or row >= row_len or col < 0 or col >= col_len or heights[row][col] < prev_height:
                return
            visited.add((row, col))
            for dr, dc in drs:
                dfs(row+dr, col+dc, visited, heights[row][col])

        #work on row
        for c in range(col_len):
            dfs(0,c,pac,heights[0][c])
            dfs(row_len-1, c , atl, heights[row_len-1][c])
        
        #work on col
        for r in range(row_len):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col_len-1, atl, heights[r][col_len-1])

        res = []
        for r in range(row_len):
            for c in range(col_len):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res


        

        