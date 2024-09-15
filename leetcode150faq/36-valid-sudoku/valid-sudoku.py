class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            row_hashset = set()
            col_hashset = set()
            for col in range(9):
                cur_row_char = board[row][col]
                cur_col_char = board[col][row]
                if cur_row_char != ".":
                    if cur_row_char in row_hashset:
                        return False
                    else:
                        row_hashset.add(cur_row_char)
                if cur_col_char != ".":
                    if cur_col_char in col_hashset:
                        return False
                    else:
                        col_hashset.add(cur_col_char)

        box_hashmap = {}

        for row in range(9):
            for col in range(9):
                rk = row//3
                ck  = col//3
                cur_char = board[row][col]
                if cur_char != ".":
                    if (rk,ck) not in box_hashmap:
                        box_set = set()
                        box_set.add(cur_char)
                        box_hashmap[(rk,ck)] =  box_set
                    else:
                        box_set = box_hashmap[(rk, ck)]
                        if cur_char in box_set:
                            return False
                        else:
                            box_set.add(cur_char)
        
        return True


        




        