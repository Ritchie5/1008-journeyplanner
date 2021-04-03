class Backtracking:

    def find_path(self, graph1, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph1:
            pass
        for node in graph1[start]:
            if node.destination not in path:
                new_path = self.find_path(graph1, node.destination, end, path)
                if new_path is not None:
                    return new_path
            if node.destination in path:
                pass

    def find_all_path(self, graph1, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph1:
            pass
        paths = []
        for node in graph1[start]:
            if node.destination not in path:
                new_path = self.find_all_path(graph1, node.destination, end, path)
                if new_path is not None:
                    for new_path in new_path:
                        paths.append(new_path)
            if node.destination in path:
                pass
        return paths

    def get_shortest_path(self, graph1, start, end, time, path=[0]):
        path[0] += int(time)
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph1:
            pass
        shortest_path = None
        for node in graph1[start]:
            if node.destination not in path:
                time = node.weight
                new_path = self.find_shortest_path(graph1, node.destination, end, time, path)
                if new_path is not None:
                    if shortest_path is None or new_path[0] < shortest_path[0]:
                        shortest_path = new_path
            if node.destination in path:
                pass
        return shortest_path
