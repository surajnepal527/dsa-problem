class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # Initialize the result with the first row
        
        for n in range(1, numRows):
            prev = res[n-1]  # Get the last row
            tmp = [1]  # Start the new row with 1
            for i in range(1, n):
                # Each element is the sum of the two elements directly above it
                tmp.append(prev[i - 1] + prev[i])
            tmp.append(1)  # End the new row with 1
            res.append(tmp)
        
        return res
