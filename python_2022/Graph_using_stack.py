class Graph(object):
    def __init__(self):
        self.vertDict = {}
        self.final_path = []
        self.route = []

    def add_edge(self, v1, v2):
        if v1 in self.vertDict.keys():
            self.vertDict[v1].append(v2)
        else:
            self.vertDict[v1] = [v2]

        return self.vertDict

    def iterateGraph(self, start_point):
        if start_point not in self.vertDict.keys():
            print("Start Point is not valid")
            return
        stack = []
        visited = set()
        stack.append(start_point)
        if start_point not in visited:
            visited.add(start_point)
        while stack:
            try:
                element = stack.pop()
                if element in self.vertDict.keys():
                    for item in self.vertDict[element]:
                        if item not in visited:
                            stack.append(item)
                            visited.add(item)
                else:
                    stack.pop()
            except:
                continue
        return visited

g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'E')
g.add_edge('C', 'E')
g.add_edge('B', 'F')
final_dic = g.add_edge('E', 'F')

print(final_dic)
st = "Geek"
st.isalpha()
#import pdb;pdb.set_trace()
visited = g.iterateGraph('A')
#visited.sort()
print(visited)
#path = g.find_path('A', 'F')
#print(path)