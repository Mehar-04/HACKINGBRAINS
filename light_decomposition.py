from typing import List, Optional, Tuple

class SegmentTree:
    # Segment tree supporting range sum and range update (lazy propagation)
    def __init__(self,  List[int]) -> None:
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def _push(self, v: int, l: int, r: int) -> None:
        if self.lazy[v] != 0:
            self.tree[v] += (r-l) * self.lazy[v]
            if v < self.size:
                self.lazy[2*v] += self.lazy[v]
                self.lazy[2*v+1] += self.lazy[v]
            self.lazy[v] = 0

    def _update(self, v: int, l: int, r: int, ql: int, qr: int, val: int) -> None:
        self._push(v, l, r)
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self.lazy[v] += val
            self._push(v, l, r)
            return
        m = (l + r) // 2
        self._update(2*v, l, m, ql, qr, val)
        self._update(2*v+1, m, r, ql, qr, val)
        self.tree[v] = self.tree[2*v] + self.tree[2*v+1]

    def update(self, l: int, r: int, val: int) -> None:
        self._update(1, 0, self.size, l, r, val)

    def _query(self, v: int, l: int, r: int, ql: int, qr: int) -> int:
        self._push(v, l, r)
        if qr <= l or r <= ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[v]
        m = (l + r) // 2
        return self._query(2*v, l, m, ql, qr) + self._query(2*v+1, m, r, ql, qr)

    def query(self, l: int, r: int) -> int:
        return self._query(1, 0, self.size, l, r)

class HeavyLightDecomposition:
    def __init__(self, n: int, edges: List[Tuple[int, int]], values: List[int]) -> None:
        self.n = n
        self.edges = edges
        self.adj: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.parent = [-1] * n
        self.depth = [0] * n
        self.size = [1] * n
        self.heavy = [-1] * n
        self.chain_head = [None] * n
        self.pos_in_base = [0] * n
        self.base_array: List[int] = []
        self.values = values
        self._dfs(0)
        self.ptr = 0
        self._decompose(0, 0)
        self.seg = SegmentTree(self.base_array)

    def _dfs(self, u: int, p: int = -1) -> int:
        max_size = 0
        for v in self.adj[u]:
            if v == p:
                continue
            self.parent[v] = u
            self.depth[v] = self.depth[u] + 1
            self.size[v] = self._dfs(v, u)
            if self.size[v] > max_size:
                max_size = self.size[v]
                self.heavy[u] = v
            self.size[u] += self.size[v]
        return self.size[u]

    def _decompose(self, u: int, head: int) -> None:
        self.chain_head[u] = head
        self.pos_in_base[u] = self.ptr
        self.base_array.append(self.values[u])
        self.ptr += 1
        if self.heavy[u] != -1:
            self._decompose(self.heavy[u], head)
            for v in self.adj[u]:
                if v != self.parent[u] and v != self.heavy[u]:
                    self._decompose(v, v)

    def _query(self, u: int, v: int) -> int:
        res = 0
        while self.chain_head[u] != self.chain_head[v]:
            if self.depth[self.chain_head[u]] < self.depth[self.chain_head[v]]:
                u, v = v, u
            head = self.chain_head[u]
            res += self.seg.query(self.pos_in_base[head], self.pos_in_base[u]+1)
            u = self.parent[head]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res += self.seg.query(self.pos_in_base[u], self.pos_in_base[v]+1)
        return res

    def query_sum(self, u: int, v: int) -> int:
        return self._query(u, v)

    def update_path(self, u: int, v: int, val: int) -> None:
        while self.chain_head[u] != self.chain_head[v]:
            if self.depth[self.chain_head[u]] < self.depth[self.chain_head[v]]:
                u, v = v, u
            head = self.chain_head[u]
            self.seg.update(self.pos_in_base[head], self.pos_in_base[u]+1, val)
            u = self.parent[head]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        self.seg.update(self.pos_in_base[u], self.pos_in_base[v]+1, val)

# Example usage:
# n = 7
# edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
# values = [10, 20, 30, 40, 50, 60, 70]
# hld = HeavyLightDecomposition(n, edges, values)
# print(hld.query_sum(3, 6))  # Path sum from node 3 to node 6
# hld.update_path(3, 4, 5)    # Add 5 to all nodes on the path from 3 to 4
