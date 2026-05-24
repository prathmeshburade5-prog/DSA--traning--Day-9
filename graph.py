import sys
class graph:
    def __init__(self):
        self.nodes=[]
        self.graph=[]
        self.nodecount=0
    def addnode(self):
        if v in self.nodes:
            print(v,"is already present")
        else:
            self.nodecount+=1
            self.nodes.append(v)
            for x in self.graph:
                x.append(0)
            temp=[]
            for x in range(self.nodecount):
                temp.append(0)
            self.graph.append(temp)
            print(v, "is added")
                
    def addEdge_undirected_unweighted(self,v1,v2):
        if v1 not in self.nodes:
            print(v1,"not present")
            return
        if v2 not in self.nodes:
            print(v2,"not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=1
        self.graph[index2][index1]=1
        print("Edge Added")
        
        
    def addEdge_undirected_weighted(self,v1,v2,weight):
        if v1 not in self.nodes:
            print(v1,"not present")
            return
        if v2 not in self.nodes:
            print(v2,"not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=weight
        self.graph[index2][index1]=weight
        print("Edge Added")
        
    def addEdge_directed_weighted(self,v1,v2,weight):
        if v1 not in self.nodes:
            print(v1,"not present")
            return
        if v2 not in self.nodes:
            print(v2,"not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=weight
        
        print("Edge Added")
        
    def printGraph(self):
        print(*self.nodes)
        for i in range(self.nodecount):
            for j in range(self.nodecount):
                print(self.graph[i][j],end=" ")
            print()
            
    def deleteGraph(self, v):
        if v not in self.nodes:
            print(v, "not present")
        else:
            index1 = self.nodes.index(v)
            self.nodes.pop(index1)
            self.graph.pop(index1)
            for x in self.graph:
                x.pop(index1)

            self.nodecount -= 1

            print(v, "is deleted")
        
    

if __name__ == '__main__':
    obj=graph()
    while True:
        print("\n 1. (Insertion) add a node using adjacency matrix representation")
        print("2. (Insertion) add a edge using adjacency matrix representation")
        print("3. (Insertion) add a edge using undirected weighted graph")
        print("4. (Insertion) add a edge using directed weighted graph")
        print("5. print graph")
        print("6. Delete operation")
        print("0. Exit\n")
        n=int(input("Enter any choice:"))
        if n==1:
            v=input("Enter Vertex:")
            obj.addnode()
        elif n==2:
            v1=input("Enter Vertex1:")
            v2=input("Enter Vertex2:")
            obj.addEdge_undirected_unweighted(v1,v2)
        elif n==3:
            v1=input("Enter Vertex1:")
            v2=input("Enter Vertex2:")
            w=input("Enter weight:")
            obj.addEdge_undirected_weighted(v1,v2,w)
        elif n==4:
            v1=input("Enter Vertex1:")
            v2=input("Enter Vertex2:")
            w=input("Enter weight:")
            obj.addEdge_directed_weighted(v1,v2,w)
        elif n==5:
            obj.printGraph()
        elif n==6:
            v=input("Enter Vertex:")
            obj.deleteGraph(v)
        elif n==0:
            sys.exit(0)