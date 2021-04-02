import csv
import time
from Backtracking import Backtracking
from Dijkstra import Dijkstra
from graph import Graph


def main():
    # Initialize Graph
    graph = Graph("C:/1008/graph.csv")

    # Using BackTracking Algo
    # BackTracking: Finding single path algo
    back_tracker = Backtracking()
    path = back_tracker.find_path(graph.adjList, "Pasir ris", "Woodlands")
    print(path)

    # BackTracking: Finding all path Algo
    path1 = back_tracker.find_all_path(graph.adjList, "Pasir ris", "Woodlands")
    print(path1)

    # BackTracking: Finding shortest path Algo
    path2 = back_tracker.get_shortest_path(graph.adjList, "Pasir ris", "64229:72")
    print(path2)

    # Dijkstra
    temp_Dij = Dijkstra(graph, "Simei")
    temp_Dij.find_path("64229:72")


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)
