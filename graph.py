import csv


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

                # Uni direction implementation for buses
                # Check if mrt/bus is already in graph
                # If in graph add edge/path to mrt/bus key
                if v1 in self.adjList:
                    # Check if edge has already been added to mrt/bus key
                    edge_in_graph = False
                    for edge in self.adjList[v1]:
                        if v2 == edge.dest():
                            edge_in_graph = True

                    # If edge is not in graph add edge
                    if not edge_in_graph:
                        self.adjList[v1].append(e)

                    # If edge in graph do not add edge
                    elif edge_in_graph:
                        pass

                # Mrt/Bus not found in the graph, add key and edge into graph
                else:
                    self.adjList[v1] = []
                    self.adjList[v1].append(e)

                # Dual direction
                # MRT are dual direction
                if type == "MRT":
                    if v2 in self.adjList:
                        # Check if edge has already been added to mrt/bus key
                        edge_in_graph = False
                        for edge in self.adjList[v2]:
                            if v1 == edge.dest():
                                edge_in_graph = True

                        # If edge is not in graph add edge
                        if not edge_in_graph:
                            self.adjList[v2].append(e1)

                        # If edge in graph do not add edge
                        elif edge_in_graph:
                            pass
                    else:
                        self.adjList[v2] = []
                        self.adjList[v2].append(e1)

    def print_list(self):
        for line in self.adjList:
            for edge in self.adjList[line]:
                print(line + " " + edge.to_string())

    def print_dest(self):
        for edge in self.adjList["Simei"]:
            print(edge.dest())


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


if __name__ == '__main__':
    graph = Graph("graph.csv")
    graph.print_list()
