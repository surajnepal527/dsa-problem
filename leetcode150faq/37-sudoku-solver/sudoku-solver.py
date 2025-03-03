class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [[set() for _ in range(3)] for _ in range(3)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    row_sets[r].add(num)
                    col_sets[c].add(num)
                    box_sets[r//3][c//3].add(num)
                else:
                    empty_cells.append((r,c))
        
        def solve(idx:int):
            if idx == len(empty_cells):
                return True
            row, col = empty_cells[idx]
            box = box_sets[row//3][col//3]

            for num in map(str, range(1,10)):
                if num not in row_sets[row] and num not in col_sets[col] and num not in box:
                    board[row][col] = num
                    row_sets[row].add(num)
                    col_sets[col].add(num)
                    box.add(num)

                    if solve(idx+1):
                        return True
                    board[row][col] = "."
                    row_sets[row].remove(num)
                    col_sets[col].remove(num)
                    box.remove(num)

            return False

        solve(0)