class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        four_sides = [(0, -1), (0, 1), (1, 0), (-1, 0)] # (x, y)
        visited = {}
        length = len(grid)
        height = len(grid[0])
        def check_all_sides(r, c):
            queue = []
            for side in four_sides:
                x = r + side[0]
                y = c + side[1]
                if 0 <= x < length and 0 <= y < height:
                    if grid[x][y] == "1" and not visited.get((x,y)):
                        queue.append((x, y))
                        visited[(x, y)] = True
            return queue

        islands = 0
        for i in range(length):
            for j in range(height):
                if grid[i][j] == "1" and not visited.get((i, j)):
                    visited[(i, j)] = True
                    queue = check_all_sides(i, j)
                    while queue:
                        x, y = queue.pop()
                        more = check_all_sides(x, y)
                        queue.extend(more)
                    islands += 1
        
        return islands
