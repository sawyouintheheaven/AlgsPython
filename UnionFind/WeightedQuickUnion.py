class WeightedQuickUnion():
    __count = int()     #number of components
    __parent = list()   #__parent[i] parent of i
    __size = list()     #size[i] number of sites in subtree rooted at i
    #Each site is initially in its own component
    def __init__(self, N):
        self.__count = N
        for i in range(0, self.__count):
            self.__parent.append(i)
            self.__size.append(1)
    #Return the component identifier for the component containing site
    def find(self, p):
        self.validate(p)
        while (p != self.__parent[p]):
            p = self.__parent[p]
        return p
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    #Merges the component containig site p with
    #the component containing site q
    def union(self, p, q):
        rootP=self.find(p)
        rootQ=self.find(q)
        if (rootP == rootQ):
            return
        if (self.__size[rootP] < self.__size[rootQ]):
            self.__parent[rootP] = rootQ
            self.__size[rootQ] += self.__size[rootP]
        else:
            self.__parent[rootQ] = rootP
            self.__size[rootP] += self.__size[rootQ]
        self.__count-=1
    def validate(self, p):
        n = len(self.__parent)
        if (p < 0 or p >= n):
            raise ValueError("index", p, "is not between 0 and", (n - 1))
    def traversal(self):
        for i in self.__parent:
            print(i, end=' ')
WQU = WeightedQuickUnion(12)
WQU.union(0, 1)
WQU.union(1, 2)
WQU.union(3, 4)
WQU.union(4, 5)
WQU.union(5, 2)
WQU.union(6, 7)
WQU.union(7, 8)
WQU.union(9, 10)
WQU.union(10, 11)
WQU.union(11, 8)
WQU.union(11, 2)
print(WQU.connected(2, 8))
WQU.traversal()