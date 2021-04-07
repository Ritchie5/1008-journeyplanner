from graph import Graph


class Backtracking:

    def find_path(self, graph1, start, end, path=[]):
        print(start)
        print(end)
        path = path + [start]
        if start == end:
            return path
        if start not in graph1:
            pass
        for node in graph1[start]:
            if node.destination not in path:
                new_path = self.find_path(Backtracking, graph1, node.destination, end, path)
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
                new_path = self.find_all_path(Backtracking, graph1, node.destination, end, path)
                if new_path is not None:
                    for new_path in new_path:
                        paths.append(new_path)
            if node.destination in path:
                pass
        return paths

    def find_shortest_path(self, graph1, start, end, time, path=[0]):
        path[0] += int(time)
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph1:
            pass
        shortest_path = None
        for node in graph1[start]:
            if node.destination not in path:
                time = node.time
                new_path = self.find_shortest_path(Backtracking, graph1, node.destination, end, time, path)
                if new_path is not None:
                    if shortest_path is None or new_path[0] < shortest_path[0]:
                        shortest_path = new_path
            if node.destination in path:
                pass
        return shortest_path

    def find_cost_path(self, graph1, start, end, time, cost, path=[0, 0]):
        path[0] += int(time)
        path[1] += float(cost)
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph1:
            pass
        shortest_path = None
        for node in graph1[start]:
            if node.destination not in path:
                time = node.time
                cost = node.cost
                new_path = self.find_cost_path(Backtracking, graph1, node.destination, end, time, cost, path)
                if new_path is not None:
                    if shortest_path is None or new_path[0] < shortest_path[0]:
                        shortest_path = new_path
            if node.destination in path:
                pass
        return shortest_path


if __name__ == '__main__':
    graph = Graph("C:/1008/graph.csv")
    back = Backtracking
    temp = back.find_cost_path(Backtracking, graph.adjList, "Simei", "Orchard", 0, 0)
    print(temp)
