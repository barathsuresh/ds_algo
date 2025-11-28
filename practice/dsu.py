class DisjointSetUnion:
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}
        for i in vertices:
            self.parent[i] = i
        self.rank = dict.fromkeys(vertices,0)
    
    def find(self,item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self,set1,set2):
        x = self.find(set1)
        y = self.find(set2)

        if x==y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x]+=1