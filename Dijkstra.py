from IndexMinPQ import IndexMinPQ

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
            for node in self.list[v]:
                node.marked = True
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

    def find_path(self, dest):
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