class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set) # key (r//3, c//3)

        for r in range(9):
            for c in range(9):
                cur_val = board[r][c]
                if cur_val == ".":
                    continue
                if cur_val in rows[r] or cur_val in cols[c] or cur_val in square[(r//3, c//3)]:
                    return False
                rows[r].add(cur_val)
                cols[c].add(cur_val)
                square[(r//3, c//3)].add(cur_val)

        return True
        