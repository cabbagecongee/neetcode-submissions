from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for first, second in edges:
            if adj.get(first):
                adj[first].append(second)
            else:
                adj[first] = [second]
            
            if adj.get(second):
                adj[second].append(first)
            else:
                adj[second] = [first]
        
        visited = set()
        visited.add(0)
        queue = deque([(0, -1)])

        while queue:
            curr, parent = queue.popleft()

            for neighbor in adj.get(curr, []):
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                    
                visited.add(neighbor)
                queue.append((neighbor, curr))
        return len(visited) == n
    
