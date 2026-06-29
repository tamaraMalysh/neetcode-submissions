class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        squares = set()

        for i in range(9):
            for j in range(9):
                char = board[i][j]

                if char == '.':
                    continue

                row = f'{i} {char}'
                col = f'{j} {char}'
                square = f'{i // 3} {j // 3} {char}'
            
                if row in rows or col in columns or square in squares:
                    return False
                
                rows.add(row)
                columns.add(col)
                squares.add(square)
        
        return True