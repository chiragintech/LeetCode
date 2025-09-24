from collections import defaultdict
import collections
class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
class LL:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0, self.left)
        self.left.next = self.right
        self.map = {}
    def length(self):
        return len(self.map)
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            nxt = node.next
            prev = node.prev
            nxt.prev = prev
            prev.next = nxt
            self.map.pop(val, None)
    def pushRight(self, val):
        node = Node(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node
    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res
    def update(self, val):
        self.pop(val)
        self.pushRight(val)
class LFUCache:

    def __init__(self, capacity: int):
        self.lfuCnt = 0
        self.cap = capacity
        self.valMap = {}
        self.countMap = collections.defaultdict(int)
        self.listMap = collections.defaultdict(LL)
    

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1
    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)
        self.valMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)