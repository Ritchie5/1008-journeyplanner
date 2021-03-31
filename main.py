import csv
import time
from IndexMinPQ import IndexMinPQ


class Edge:
    source = None
    destination = None
    weight = None

    def __init__(self, v, w, wt):
        self.source = v
        self.destination = w
        self.weight = wt

    def src(self):
        return self.source

    def dest(self):
        return self.destination

    def to_string(self):
        return "[" + str(self.source) + "-" + str(self.destination) + "," + str(self.weight) + "] "


class Graph:
    adjList = {}

    def __init__(self, file):
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                type = row[0]
                v1 = row[1]
                v2 = row[2]
                v3 = row[3]

                e = Edge(v1, v2, v3)
                e1 = Edge(v2, v1, v3)

                if v1 in self.adjList:
                    if v2 in self.adjList[v1]:
                        pass
                    else:
                        self.adjList[v1].append(e)
                else:
                    self.adjList[v1] = []
                    self.adjList[v1].append(e)

                if type == "MRT":
                    if v2 in self.adjList:
                        if v1 in self.adjList[v2]:
                            pass
                        else:
                            self.adjList[v2].append(e1)
                    else:
                        self.adjList[v2] = []
                        self.adjList[v2].append(e1)

    def print_list(self):
        for line in self.adjList:
            for edge in self.adjList[line]:
                print(line + " " + edge.to_string())


def find_path(graph1, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph1:
        pass
    for node in graph1[start]:
        if node.destination not in path:
            new_path = find_path(graph1, node.destination, end, path)
            if new_path is not None:
                return new_path
        if node.destination in path:
            pass


def find_all_path(graph1, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph1:
        pass
    paths = []
    for node in graph1[start]:
        if node.destination not in path:
            new_path = find_all_path(graph1, node.destination, end, path)
            if new_path is not None:
                for new_path in new_path:
                    paths.append(new_path)
        if node.destination in path:
            pass
    return paths


def compare_shortest_path(graph1, start, end):
    paths = find_shortest_path(graph1, start, end)
    time = [0, 0, 0, 0, 0]

    print(paths[0])

    number_of_path = len(paths)
    for x in range(0, number_of_path):
        for y in range(1, len(paths[x]), 2):
            time[x] += int(paths[0][y])

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


def find_shortest_path(graph1, start, end, path=[], time=0):
    path = path + [start] + [time]
    if start == end:
        return [path]
    if start not in graph1:
        pass
    paths = []
    for node in graph1[start]:
        if node.destination not in path:
            time = node.weight
            new_path = find_shortest_path(graph1, node.destination, end, path, time)
            if new_path is not None:
                for new_path in new_path:
                    paths.append(new_path)
        if node.destination in path:
            pass
    return paths


class Dijkstra:
    source = None
    list = {}
    pq = None

    def __init__(self, G, source):
        self.source = source

        for v in G.adjList:
            self.list[v] = []
            self.list[v].append(Dijkstra_node(None, False, 9999))

        self.pq = IndexMinPQ()
        self.pq.insert(source, 0.0)

        for node in self.list[source]:
            node.dist = 0.0

        while not self.pq.isEmpty():
            v = self.pq.del_min()
            self.pq.print_pq()
            for node in self.list[v]:
                node.marked = True
            print("Relaxing Vertex " + str(v))
            for e in G.adjList[v]:
                self.relax(e)

    def relax(self, e):
        v = e.src()
        w = e.dest()

        for node in self.list[v]:
            source_node = node

        for node in self.list[w]:
            dest_node = node

        if dest_node.dist > source_node.dist + int(e.weight):
            dest_node.dist = source_node.dist + int(e.weight)
            dest_node.edge = e

            if self.pq.contains(w):
                self.pq.change(w, dest_node.dist)
            elif dest_node.marked is False:
                self.pq.insert(w, dest_node.dist)

    def print_path(self, dest):
        path = [dest]
        for node in self.list[dest]:
            time = node.dist

        while dest != self.source:
            for node in self.list[dest]:
                temp = node.edge
                temp = temp.src()
                path.append(temp)
                dest = temp

        path.reverse()
        print(path)
        print("Time take:",time)


class Dijkstra_node:
    edge = None
    marked = False
    dist = 0

    def __init__(self, edge, marked, dist):
        self.edge = edge
        self.marked = marked
        self.dist = dist

    def edge(self):
        return self.edge.src()


def main():
    graph = Graph("C:/1008/graph.csv")
    # temp1 = find_path(graph.adjList, "Pasir ris", "Woodlands")
    # print(temp1)
    #temp2 = compare_shortest_path(graph.adjList, "Pasir ris", "Woodlands")
    #print(temp2)
    # temp3 = find_all_path(graph.adjList, "Pasir ris", "Woodlands")
    # print(temp3)
    temp4 = Dijkstra(graph, "Simei")
    temp4.print_path("64229:72")


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)
