class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            
            while queue:
                
                row, col = queue.popleft()
                movements = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in movements:
                    r, c = row+dr, col+dc
                    if(r in range (rows) and
                        c in range(columns) and
                       grid[r][c]=="1" and
                       (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=="1" and (r, c) not in visited:
                    bfs(r, c)
                    islands+=1
                    
        return islands