class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # Initialize the result with the first row
        
        for n in range(1, numRows):
            prev_row = res[-1]  # Get the last row
            new_row = [1]  # Start the new row with 1
            for i in range(1, n):
                # Each element is the sum of the two elements directly above it
                new_row.append(prev_row[i - 1] + prev_row[i])
            new_row.append(1)  # End the new row with 1
            res.append(new_row)
        
        return res
