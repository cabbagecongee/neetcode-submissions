class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n = len(word)
        def backtrack(row, col, i, visited):
            # two traversal choices; either go right or down
            if i == self.n:
                return True
            if 0 > row or row >= len(board) or 0 > col or col >= len(board[0]):
                return False
            
            if board[row][col] == word[i]:
                choices = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
                for choice in choices:
                    if choice not in visited:
                        r = backtrack(choice[0], choice[1], i+1, visited + [(choice[0], choice[1])])
                        if r:
                            return True
            
            return False
        
        if self.n == 0:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = backtrack(i, j, 0, [(i, j)])
                    if res:
                        return True
        return False

