from collections import OrderedDict
class Graph(object):
    def __init__(self, routes):
        #self.dic = OrderedDict()
        self.dic = {}

        for route, route1 in routes:
            if route in self.dic:
                self.dic[route].append(route1)
            else:
                self.dic[route] = [route1]
        print(f'dic',self.dic)

    def find_all_paths(self, start, end, path=[]):

        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.dic[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
        return paths

    def getpath(self, source, destination, li=[]):
        #li.append(source)
        li = li + [source]
        #li.append(source)
        try:
            if source == destination:
                return [li]
            paths = []
            for values in self.dic[source]:
                if values not in li:
                    path = self.getpath(values, destination, li)
                for t in path:
                    paths.append(t)
            return paths
        except:
            pass



if __name__ == '__main__':
    routes = [("mumbai", "paris"),
              ("mumbai", "dubai"),
              ("paris", "dubai"),
              ("paris", "new york"),
              ("dubai", "new york"),
              ("new york", "delhi")]

    route_graph = Graph(routes)

    paths = route_graph.getpath("mumbai", "new york")
    print(paths)
    paths = route_graph.find_all_paths("mumbai", "new york")
    print(paths)