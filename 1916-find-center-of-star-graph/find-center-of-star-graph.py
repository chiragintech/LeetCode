class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        h = {}
        for u,v in edges:
            if u not in h:
                h[u] = 1
            else:
                h[u] += 1
            if v not in h:
                h[v] = 1
            else:
                h[v] += 1
        for i in h:
            if h[i] == len(edges):
                return i
        return -1
           