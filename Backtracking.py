from graph import Graph


class Backtracking:
    # Find shortest path based on time
    def find_shortest_path(self, graph1, start, end, time, cost):
        paths = self.find_shortest_path1(graph1, start, end, time, cost)
        print(paths)
        # Format array
        arr = [0, 0]
        arr[0] = paths[0]
        arr[1] = paths[1]
        for x in range(2, len(paths), 3):
            arr.append(paths[x])

        return arr

    # Find Shortest possible path recursively
    def find_shortest_path1(self, graph, start, end, time, cost, shortestLength = 0, path=[0, 0]):
        print("called")
        path = path + [start, time, cost]
        path[0] = 0
        path[1] = 0
        for x in range(2, len(path), 3):
            path[0] += float(path[x + 1])
            path[1] += float(path[x + 2])
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node.destination not in path:
                time = node.time
                cost = node.cost
                if shortestLength == 0 or path[0] < shortestLength:
                    newpath = self.find_shortest_path1(graph, node.destination, end, time, cost, shortestLength, path)
                    if newpath:
                        if not shortest or path[0] < shortestLength:
                            shortest = newpath
                            shortestLength = newpath[0]
        return shortest


# if __name__ == '__main__':
#     tag = "MRTBUS"
#     graph = Graph("graph.csv",tag, "")
#     back_tracker = Backtracking
#     paths = back_tracker.find_shortest_path(graph.adjList, "Simei", "Bedok", 0, 0.0)
