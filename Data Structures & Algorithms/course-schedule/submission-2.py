class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
        adj_list = dict()

        for course, prereq in prerequisites:
            if adj_list.get(course) != None:
                adj_list[course].append(prereq)
            else:
                adj_list[course] = [prereq]
                
        state = [0] * numCourses # 0 - unvisited, 1 - visiting, 2 - visited
        
        def dfs(u):
            state[u] = 1
            for v in adj_list.get(u, []):
                if state[v] == 1:
                    return False
                if state[v] == 0:
                    if not dfs(v):
                        return False
            state[u] = 2
            return True
        
        for node in adj_list.keys():
            if state[node] == 0:
                if not dfs(node):
                    return False
        return True

