class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def matrix_to_list(isConnected):
            graph = {i : [] for i in range(len(isConnected))}
            for i in range(len(isConnected)):
                for j in range(len(isConnected)):
                    if i != j and isConnected[i][j] == 1:
                        graph[i].append(j)
            return graph
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        graph = matrix_to_list(isConnected)
        visited = set()
        p = 0
        # for i in range(len(isConnected)):
        #     if i not in visited:
        #         visited.add(i)
        #         dfs(i)
        #         p += 1
        # return p 

        for i in range(len(isConnected)):
            if i not in visited:
                p += 1
                q = deque([i])
                visited.add(i)
                while q:
                    node = q.popleft()
                    for neigh in graph[node]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
        return p

        # visited = [False] * (len(isConnected) + 1)
        # visited[0] = True
        # q = collections.deque([0])
        # count = 0
        # while q:
        #     node = q.popleft()
        #     for neigh in isConnected[node]:
        #         if isConnected[node][neigh] and not visited[neigh]:
        #             count += 1
        #             visited[neigh] = True
        #             q.append(neigh)
        # return count
        def dfs(graph, node, visited, count):
            visited[node] = True
            for neigh in graph[node]:
                if graph[node][neigh] and not visited[neigh]:
                    return dfs(graph, neigh, visited, count)
                    
        graph = isConnected
        visited = [False]* (len(isConnected) + 1)
        visited[0] = True
        count = 0
        for i in range(len(isConnected)):
            if visited[i] == False:
                count += 1
                dfs(isConnected, 0, visited, count)
                
        return count