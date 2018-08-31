class QuickUnion():
    #pre define a array
    __parent = list()
    def __init__(self,N):
        for i in range(0,N):
            #initial the list:
            #the __id[i] save i's root
            #so, default to itself
            self.__parent.append(i)
    #locate i's root
    def root(self,i):
        #locate from bottom to top
        self.validate(i)
        while i != self.__parent[i]:
            i = self.__parent[i]
        return i
    def connected(self,p,q):
        return self.root(p) == self.root(q)
    def union(self,p,q):
        i = self.root(p)
        j = self.root(q)
        self.__parent[i] = j
    def traversal(self):
        for i in self.__parent:
            print(i,end=' ')
    def validate(self,p):
        n = len(self.__parent)
        if p<0 or p>=n:
            raise ValueError("index",p,"is not between 0 and",(n-1))
Qu = QuickUnion(8)
Qu.union(0,1)
Qu.union(2,1)
Qu.union(2,4)
Qu.union(3,7)
print(Qu.connected(0,4))
Qu.traversal()


