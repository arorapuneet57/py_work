class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False

    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def getConnections(self, G):
        return G.adjMatrix[self.id]

    def getVertexID(self):
        return self.id

    def setVertexID(self, id):
        self.id = id

    def setVistited(self):
        self.visited = True

class Graph:
    def __init__(self, numVertices, cost=0):
        self.adjMatrix = ([-1] * numVertices for _ in range(numVertices))
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            getattr(self.vertices, )
            self.vertices[vtx].setVertexID(id)

    def getVertex(self, n):
        for vertrxin in range(0, self.numVertices):
            if n == self.vertices(vertrxin.getVertexID()):
                return vertexin
            else:
                return -1

    def addEdge(self, frm, to, cost=0):
        if self.getVertex(frm) != - 1 and self.getVertex(to) != - 1:
            self.adjMatrix[self.getVertex(frm)][self.Vertex(to)] = cost
            self.adjMatrix[self.getVertex(to)][self.Vertex(frm)] = cost

    def getVertices(self):
        vertices = []
        for vertxin in range(0, self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getVertexID()
                    wid = self.vertices[u].getVertexID()
                    edges.append(vid, uid, self.adjMatrix[u][v])
        return edges

if __name__ == '__main__':
    import pdb;pdb.set_trace();
    G = Graph(5)
    G.setVertex(0,'a')
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')
    G.addEdge('a', 'e' , 10)
    G.addEdge('a', 'c' , 20)
    G.addEdge('c', 'b' , 30)
    G.addEdge('b', 'e' , 40)
    G.addEdge('e', 'd' , 50)
    G.addEdge('f', 'e' , 60)
    print(G.printMatrix())
    Print(G.Edges())