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

    def get_shortest_path(self, graph1, start, end):
        paths = self.find_shortest_path(graph1, start, end)

        number_of_path = len(paths)
        time = [0 for i in range(number_of_path)]
        for x in range(0, number_of_path):
            for y in range(1, len(paths[x]), 2):
                if x == 1 and time[x] < time[x-1]:
                    time[x] += int(paths[x][y])

        time_taken = time[0]
        fastest_path = 0
        for x in range(1, number_of_path):
            if time[x] < time_taken:
                time_taken = time[x]
                fastest_path = x

        fastest = []
        for y in range(0, len(paths[fastest_path]), 2):
            fastest.append(paths[fastest_path][y])
        return fastest

    def find_shortest_path(self, graph1, start, end, path=[], time=0):
        path = path + [start] + [time]
        if start == end:
            return [path]
        if start not in graph1:
            pass
        paths = []
        for node in graph1[start]:
            if node.destination not in path:
                time = node.weight
                new_path = self.find_shortest_path(graph1, node.destination, end, path, time)
                if new_path is not None:
                    for new_path in new_path:
                        paths.append(new_path)
            if node.destination in path:
                pass
        return paths
