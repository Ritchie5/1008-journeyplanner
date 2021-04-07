from graph import Graph


class Backtracking:
    # Find shortest path based on time
    def find_shortest_path(self, graph1, start, end, time, cost):
        paths = self.find_all_path(graph1, start, end, time, cost)

        shortest_time = paths[0][0]
        shortest_path = 0
        for x in range(1, len(paths)):
            if shortest_time > paths[x][0]:
                shortest_time = paths[x][0]
                shortest_path = x

        return paths[shortest_path]

        # Find all possible paths
    def find_all_path(self, graph1, start, end, time, cost):
        paths = self.find_all_path1(graph1, start, end, time, cost)
        # Format paths
        arr = [[0, 0] for j in range(len(paths))]
        for x in range(0, len(paths)):
            for y in range(0, len(paths[x]), 3):
                arr[x].append(paths[x][y])
                arr[x][0] += float(paths[x][y + 1])
                arr[x][1] += float(paths[x][y + 2])

        return arr

    # Find all possible paths
    def find_all_path1(self, graph1, start, end, time, cost, path=[]):
        path = path + [start, time, cost]
        # Reached destination
        if start == end:
            return [path]
        # Went out of Graph
        if start not in graph1:
            path[0] = 0
            path[1] = 0
            pass
        all_paths = []              # Array to contain all paths

        # Check all edges of graph
        for node in graph1[start]:
            # If the destination not already in path, find path
            if node.destination not in path:
                time = node.time
                cost = node.cost
                new_path = self.find_all_path1(graph1, node.destination, end, time, cost, path)
                if new_path is not None:
                    # append all new paths to all_path array
                    for new_path in new_path:
                        all_paths.append(new_path)
            elif node.destination in path:
                pass
        # Return all paths
        return all_paths


if __name__ == '__main__':
    graph = Graph("graph.csv")
    back_tracker = Backtracking
    paths = back_tracker.find_shortest_path(graph.adjList, "Simei", "Bedok", 0, 0.0)
    print(paths)
