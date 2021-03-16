# London Underground Journey Planner - www.101computing.net/london-underground-journey-planner/
from tubemap import tubemap


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, shortestLength=-1, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            if shortestLength == -1 or len(path) < (shortestLength - 1):
                newpath = find_shortest_path(graph, node, end, shortestLength, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
                        shortestLength = len(newpath)
    return shortest


stationFrom = "Simei"
stationTo = "55509:72"
print("From: " + stationFrom)
print("To: " + stationTo)
print("Searching shortest route... This may take a while...")
path = find_shortest_path(tubemap, stationFrom, stationTo)
print("Suggested Route: ")
print(path)

path1 = find_all_paths(tubemap, stationFrom, stationTo)
print("All possible Routes: ")
print(path1)
