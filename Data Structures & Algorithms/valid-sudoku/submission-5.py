class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[r])):
                i = board[r][c]
                box = (r // 3, c // 3)
                #if i is blank
                if i == ".":
                    continue
                
                if i in rows[r] or i in cols[c] or i in boxes[box]:
                    return False
                
                rows[r].append(i)
                cols[c].append(i)
                boxes[box].append(i)
        
        return True
        







        