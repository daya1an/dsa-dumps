class Graph:
    def __init__(self,routes):
        self.graph_dict = {}
        for s,e in routes:
            if s in self.graph_dict:
                self.graph_dict[s].append(e)
            else:
                self.graph_dict[s] = [e]
        print(self.graph_dict)

    def getAllPaths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.getAllPaths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def getShortestPaths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.getShortestPaths(node, end, path)
                for p in new_paths:
                    # paths.append(p)
                    if len(paths) == 0 or len(p) < len(paths[0]):
                        paths = [p]

        return paths

if __name__ == '__main__':

    # routes = [
    #     ("chennai","tindivanam"),
    #     ("tindivanam", "pondy"),
    #     ("tindivanam", "trichy"),
    #     ("trichy", "dindugal"),
    #     ("dindugal","madurai"),
    #     ("dindugal", "kodai"),
    #     ("chennai","pondy")
    # ]

    # routes = [
    #     ("Mumbai", "Pune"),
    #     ("Mumbai", "Surat"),
    #     ("Surat", "Bangaluru"),
    #     ("Pune", "Hyderabad"),
    #     ("Pune", "Mysuru"),
    #     ("Hyderabad", "Bangaluru"),
    #     ("Hyderabad", "Chennai"),
    #     ("Mysuru", "Bangaluru"),
    #     ("Chennai", "Bangaluru")
    # ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ", route_graph.getAllPaths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.getShortestPaths(start, end))
