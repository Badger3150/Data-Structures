# Name: Ruoling Yu
# Student Number: 500976267
# implement of a minimal spanning tree

class Edge(object):
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class WeightGraph(object):
    """ implement of a weight graph"""
    def __init__(self, verticeNum, edgeNum):
        self.verticeNum = verticeNum
        self.edgeNum = edgeNum
        self.edges = []
    
    def setEdgeWeight(self):
        """
            User could input the vertice connection and weight
        """
        for i in range(self.edgeNum):
            print("For the edge {}: ".format(i + 1))
            start = int(input("From vertice: "))
            while (start > self.verticeNum):
                start = int(input("Input is invalid, please enter again, from vertice: "))
            end = int(input("To vertice: "))
            while (end > self.verticeNum or start == end):
                end = int(input("Input is invalid, please enter again, to vertice: "))
            weight = int(input("The weight of this edge is: "))
            while (weight <= 0):
                weight = int(input("The weight of this edge is: "))
            edge = Edge(start, end, weight)
            self.edges.append(edge)

    def sortWeight(self):
        self.heapSort(self.edges)
    
    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def heapify(self, arr, length, parent):
        minest = parent
        lson = parent * 2 + 1
        rson = parent * 2 + 2
        if (lson < length and arr[lson].weight > arr[minest].weight):
            minest = lson
        if (rson < length and arr[rson].weight > arr[minest].weight):
            minest = rson
        if (parent != minest):
            self.swap(arr, parent, minest)
            self.heapify(arr, length, minest)

    def heapSort(self, arr):
        length = len(arr)
        # Make the heap
        for i in range(length // 2, -1, -1):
            self.heapify(arr, length, i)
        # Sort the heap
        for i in range(length - 1, 0, -1):
            self.swap(arr, i, 0)
            length -= 1
            self.heapify(arr, length, 0)
    
    def Kruskal(self):
        edges = self.edges
        # Sort the edges by their weight in ascending order
        self.sortWeight()
        connected = [0 for i in range(self.verticeNum)] # record vertice connection
        mst = [] # store the final minimal spanning tree
        for i in range(self.edgeNum):
            # the index and vertices num are not the same, so we need to -1
            startConnect = self.findConnect(connected, edges[i].start - 1)
            endConnect = self.findConnect(connected, edges[i].end - 1)
            # if they are not equal, it proves that if connect this edge, the tree will not become a circle
            if (startConnect != endConnect):
                # change the start index and the value is end index, it means from this index connect to the other 
                connected[startConnect] = endConnect
                mst.append(Edge(edges[i].start, edges[i].end, edges[i].weight))
        return mst

    def findConnect(self, list, vertice):
        while list[vertice] > 0:
            # when the value greater than zero, it means the vertice is connected to the other one, so we would like to continue check its connections and return the last one
            vertice = list[vertice]
        return vertice

verticeNum = int(input("How many vertices in the graph? "))
edgeNum = int(input("How many edges in the graph? "))
graph = WeightGraph(verticeNum, edgeNum)

# Set the weight of each edge
graph.setEdgeWeight()
# print the input graph
print("Input graph:")
print("There are {} vertices and {} edges".format(verticeNum, edgeNum))
print("  {}\t{}".format("Vertices","Weight"))
for edge in graph.edges:
    print("  {:<4}{:<4}\t{:>6}".format(edge.start, edge.end, edge.weight))
mst = graph.Kruskal()
# print the minimal spanning tree
print("Minimal spanning tree:")
print("There are {} vertices and {} edges".format(verticeNum, len(mst)))
print("  {}\t{}".format("Vertices","Weight"))
sumWeight = 0
for edge in mst:
    print("  {:<4}{:<4}\t{:>6}".format(edge.start, edge.end, edge.weight))
    sumWeight += edge.weight
# print the total weight of the spanning tree
print("The total weight of the spanning tree is {}".format(sumWeight))
