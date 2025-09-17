

class DisjointSet:
    def __init__(self, length):
        self.n = length
        self.parent = list(range(self.n))
        self.size = [1] * self.n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        if self.size[px] < self.parent[py]:
            self.parent[px] = self.parent[py]
            self.size[py] += self.size[px]
        else:
            self.parent[py] = self.parent[px]
            self.size[px] += self.size[py]

if __name__ == "__main__":
    ds = DisjointSet(5)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(1, 3)
    ds.union(1, 4)
    m = 0