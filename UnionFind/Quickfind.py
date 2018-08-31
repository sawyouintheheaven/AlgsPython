class QuickFind():
    #define a arr
    __id=list()
    def __init__(self,N):
        for i in range(0,int(N)):
            #initial the id arr
            self.__id.append(i)
    def find(self,i):
        #quick find:use i to index it's id in the arr
        self.validate(i)
        return self.__id[i]
    def connected(self,p,q):
        #if they got same id,then they are connected
        return self.find(p)==self.find(q)
    #union p,q;change p's id to q 's one
    def union(self,p,q):
        #firstly,get the value of __id[p] and __id[q]
        #otherwise id[p] keep changing
        pid=self.find(p)
        qid=self.find(q)
        for i in range(0,len(self.__id)):
            #change all element's __id to q's one
            #which are same with previous p
            if self.find(i)==pid:
                self.__id[i]=qid
    def traversal(self):
        for i in self.__id:
            print(i,end=' ')
    def validate(self,p):
        n = len(self.__id)
        if (p<0 or p>=n):
            raise ValueError("index",p,"is not between 0 and",(n-1))
UF = QuickFind(8)
UF.union(0,1)
UF.union(0,4)
UF.union(3,7)
print(UF.connected(1,4))
UF.traversal()




