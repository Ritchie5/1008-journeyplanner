from graph import Graph


class Backtracking:
    # Find shortest path based on time
    def find_shortest_path(self, graph1, start, end, time, cost, path=[0, 0]):
        path[0] += int(time)        # First element of array will contain time
        path[1] += float(cost)      # Second element of array will contain cost
        path = path + [start]       # Third element onwards will contain path
        # Reached destination
        if start == end:
            return [path]
        # Went out of Graph
        if start not in graph1:
            return None
        shortest_path = None

        # Check all edges of graph
        for node in graph1[start]:
            # If the destination not already in path, find path
            if node.destination not in path:
                time = node.time
                cost = node.cost
                new_path = self.find_shortest_path(Backtracking, graph1, node.destination, end, time, cost, path)
                if new_path is not None:
                    # Check if this is the shortest path
                    if shortest_path is None or new_path[0] < shortest_path[0]:
                        shortest_path = new_path
            # If destination already in path do nothing
            elif node.destination in path:
                pass
        # Return the shortest path
        return shortest_path

    # Find all possible paths
    def find_all_path(self, graph1, start, end, time, cost, path=[0, 0]):
        path[0] += int(time)        # First element of array will contain time
        path[1] += float(cost)      # Second element of array will contain cost
        path = path + [start]       # Third element onwards will contain path
        # Reached destination
        if start == end:
            return [path]
        # Went out of Graph
        if start not in graph1:
            pass
        all_paths = []              # Array to contain all paths

        # Check all edges of graph
        for node in graph1[start]:
            # If the destination not already in path, find path
            if node.destination not in path:
                time = node.time
                cost = node.cost
                new_path = self.find_all_path(Backtracking, graph1, node.destination, end, time, cost, path)
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
    paths = back_tracker.find_all_path(Backtracking, graph.adjList, "Simei", "Orchard", 0, 0)
    print(paths)
