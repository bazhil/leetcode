class Solution:

    def get_sudoku_butch(self, board):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = []
                for i in range(3):
                    square.extend(board[row + i][col:col + 3])
                yield square

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return False
        for line in board:
            if len(line) != 9:
                return False
            for el in line:
                if el != '.' and not el.isdigit():
                    return False

        for lst in self.get_sudoku_butch(board):
            for el in lst:
                if el != '.' and not el.isdigit():
                    return False
            nums = [el for el in lst if el.isdigit()]
            if not nums:
                return False
            if len(nums) > len(set(nums)):
                return False

        return True
