class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## search for the value in a set or something
        ## if you don't find it, add it to the list and keep going
        ## find it and return false
        ## if you get to the end, return true

        ## Questions - how do you add it to the list and how do you search for it?

        ## idea - 27 different arrays grouped into 3 groups of 9 subarrays
        ## you search for the number in the row, col, and square that it's in
        ## if you don't find it, then you add it to each so the next search yields it

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                box = i//3 + (j // 3) * 3
                if board[i][j] != ".":
                    if number in rows[i] or number in cols[j] or number in squares[box]:
                        return False
                    rows[i].add(number)
                    cols[j].add(number)
                    squares[box].add(number)
        return True

