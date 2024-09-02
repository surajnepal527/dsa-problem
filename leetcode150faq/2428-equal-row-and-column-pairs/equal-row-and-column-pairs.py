class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        row_map = {} #Dictionary row
        col_map = {} #Dictionary col
        for i in range(row):
            row_hash_arr = []
            for j in range(col):
                row_hash_arr.append(str(grid[i][j]))         
            row_hash = "_".join(row_hash_arr)
            row_map[row_hash] = row_map.get(row_hash, 0) + 1
        
        for j in range(col):
            col_hash_arr = []
            for i in range(row):
                col_hash_arr.append(str(grid[i][j]))
            col_hash = "_".join(col_hash_arr)
            col_map[col_hash] = col_map.get(col_hash, 0) + 1

        ans = 0
        for row_hash_key in row_map.keys():
            if row_hash_key in col_map:
                ans += row_map.get(row_hash_key) * col_map.get(row_hash_key)
        
        return ans

        
