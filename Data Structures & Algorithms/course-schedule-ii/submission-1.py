class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            deg[crs] += 1
            adj[pre].append(crs) 

        q = deque()

        for i in deg:
            if deg[i] == 0:
                q.append(i)
        
        result = []
        while q:
            pre = q.popleft()
            result.append(pre)
            for crs in adj[pre]:
                deg[crs] -=1
                if deg[crs] == 0:
                    q.append(crs)
        
        if len(result) == numCourses:
            return result
        else:
            return []


        