from graph import Graph


class Backtracking:
    # Find shortest path based on time
    def find_shortest_path(self, graph1, start, end, time, cost):
        paths = self.find_shortest_path1(graph1, start, end, time, cost)

        # Format array
        arr = [0, 0]
        arr[0] = paths[0][0]
        arr[1] = paths[0][1]
        for x in range(2, len(paths[0]), 3):
            arr.append(paths[0][x])

        return arr

    # Find Shortest possible path recursively
    def find_shortest_path1(self, graph1, start, end, time, cost, path=[0.0, 0.0]):
        path = path + [start, time, cost]
        path[0] = 0
        path[1] = 0
        for x in range(2, len(path), 3):
            path[0] += float(path[x + 1])
            path[1] += float(path[x + 2])
        # Reached destination
        if start == end:
            return [path]
        # Went out of Graph
        if start not in graph1:
            pass
        shortest = None  # Array to contain all paths

        # Check all edges of graph
        for node in graph1[start]:
            # If the destination not already in path, find path
            if node.destination not in path:
                time = node.time
                cost = node.cost
                if shortest is None or path[0] < shortest[0][0]:
                    new_path = self.find_shortest_path1(graph1, node.destination, end, time, cost, path)
                    if new_path is not None:
                        # append all new paths to all_path array
                        shortest = new_path
                        return shortest
            elif node.destination in path:
                pass

        # Return all paths
        return shortest


if __name__ == '__main__':
    tag = "MRTBUS"
    graph = Graph("graph.csv",tag, "")
    back_tracker = Backtracking
    paths = back_tracker.find_shortest_path(graph.adjList, "Simei", "Bedok", 0, 0.0)
