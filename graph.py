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


