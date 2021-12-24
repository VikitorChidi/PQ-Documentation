class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:

            # check if the list is blank
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        # edge case1: start and end are the same
        if start == end:
            return [path]

        # edge case2: start not in graph dictionary
        if start not in self.graph_dict:
            return []

        paths = []
        # edge case3: use recursion to explore all the routes
        for node in self.graph_dict[start]:
            # check if node has been visited
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                # append all possible paths
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            # check if node has been visited
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    start = "Paris"
    end = "New York"
    print(f"shortest path between {start} and {end}:",
          route_graph.get_shortest_path(start, end))
