class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        arr_grid = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr_grid.append(grid[i][j])

        xor = 0;
        for i in range(len(arr_grid)):
            xor = xor^arr_grid[i]
            xor = xor^(i+1)
        bit=0
        while xor & 1<<bit == 0:
            bit += 1
        
        zeros = 0;
        ones = 0;
        for i in range(len(arr_grid)):
            res_n = i+1 & 1<<bit
            res_arr = arr_grid[i] & 1<<bit
            if res_arr != 0:
                ones = ones ^ arr_grid[i]
            else:
                zeros = zeros ^ arr_grid[i]
            if res_n != 0:
                ones = ones ^ i+1
            else:
                zeros = zeros ^ i+1
        count = 0
        for i in range(len(arr_grid)):
            if ones == arr_grid[i]:
                count += 1
        
        if count == 2:
            return [ones, zeros]
        else:
            return [zeros, ones]




        

