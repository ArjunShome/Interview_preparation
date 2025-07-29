class UnionFind:
    def __init__(self):
        # Write your code here
        self.parent_map = {}
        self.parent_rank = {}
        pass

    def createSet(self, value):
        # Write your code here
        self.parent_map[value]= value
        self.parent_rank[value] = 0

    def find(self, value, search_dict = None):
        # Write your code here
        if not self.parent_map or value not in self.parent_map:
            return
        if search_dict is None:
            search_dict = dict(self.parent_map)

        for val, parent in search_dict.items():
            if val == value:
                if parent == value:
                    return parent
                value = parent
                break
        del search_dict[val]
        return self.find(value, search_dict)

    def union(self, valueOne, valueTwo):
        # Write your code here
        val_one_parent = self.find(valueOne)
        val_two_parent = self.find(valueTwo)
        if val_one_parent is not None and val_two_parent is not None:
            val_one_parent_rank = self.parent_rank[val_one_parent]
            val_two_parent_rank = self.parent_rank[val_two_parent]
            
            if val_one_parent_rank >= val_two_parent_rank:
                self.parent_map[val_two_parent] = val_one_parent
                self.parent_rank[val_one_parent] += 1
            else:
                self.parent_map[val_one_parent] = val_two_parent
                self.parent_rank[val_two_parent] += 1


if __name__ =='__main__':
    uf = UnionFind()
    uf.createSet(0)
    uf.createSet(1)
    uf.createSet(2)
    uf.createSet(3)
    uf.union(0,2)
    print(uf.find(0))
    print(uf.find(1))
    print(uf.find(2))
    print(uf.find(3))