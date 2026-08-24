class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        box = {i: set() for i in range(9)}

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                number = board[r][c]
                
                b = (r//3) * 3 + c // 3
                
                if number in row[r] or number in col[c] or number in box[b]:
                    return False
                else:
                    row[r].add(number)
                    col[c].add(number)
                    box[b].add(number)
        return True


        