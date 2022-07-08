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

    def find_path(self, s, d, paths=[]):
        paths = paths + [s]
        #paths.append(s)
        try:
            if s == d:
                print("It's done")
                return [paths]
            final_path = []
            for item in self.vertDict[s]:
                if item not in paths:
                    path = self.find_path(item, d, paths)
                for t in path:
                    final_path.append(t)
            return final_path
        except:
            pass

g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'E')
g.add_edge('C', 'E')
g.add_edge('B', 'F')
final_dic = g.add_edge('E', 'F')
print(final_dic)

path = g.find_path('A', 'F')
print(path)