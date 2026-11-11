class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, 1], [0,-1]]
        length = len(heights)
        width = len(heights[0])
        pacific = set() # visited, (r, c)
        atlantic = set()

        # pacific = first row (heights[0][i]), first column (heights[i][0])
        # atlantic = last row (heights[-1][i]), last column (heights[i][-1])

        def dfs(r, c, visited): # given curr row, col, can it reach pacific and atlantic?
            visited.add((r,c))
            for d in directions:
                x = r + d[0] # coords
                y = c + d[1] # coords
                
                if x < 0 or x >= length or y < 0 or y >= width:
                    continue
                curr_v = heights[r][c]
                next_v = heights[x][y]
                if (x, y) not in visited and next_v >= curr_v:
                    dfs(x, y, visited)

        # mark the horizontal border
        for j in range(width):
            dfs(0, j, pacific)
            dfs(length-1, j, atlantic)
        # mark vertical border
        for i in range(length):
            dfs(i, 0, pacific)
            dfs(i, width-1, atlantic)
        
        res = []
        for r in range(length):
            for c in range(width):
                if (r,c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res


        

            

            
        
