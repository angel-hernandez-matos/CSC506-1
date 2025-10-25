# File: mainCT7.py
# Written by: Angel Hernandez
# Description: Module 7 - Critical Thinking
# Requirement(s): Dijkstra's Algorithm

import os
import sys
import heapq
import subprocess

class DependencyChecker:
    @staticmethod
    def ensure_package(package_name):
        try:
            __import__(package_name)
        except ImportError:
            print(f"Installing missing package: {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"Package '{package_name}' was installed successfully.")

class TestCaseRunner:
    @staticmethod
    def run_test():
        end = "Customer"
        start = "Restaurant"
        pathfinder = ShortestPathFinder()
        pathfinder.add_edge("Restaurant", "A", 5)
        pathfinder.add_edge("A", "B", 2)
        pathfinder.add_edge("A", "C", 4)
        pathfinder.add_edge("B", "Customer", 7)
        pathfinder.add_edge("C", "Customer", 3)
        pathfinder.add_edge("Restaurant", "C", 10)
        distances, previous_nodes = pathfinder.use_dijkstra(pathfinder, start)
        shortest_path = pathfinder.create_path(previous_nodes, start, end)
        print(f"The shortest path is : {' -> '.join(shortest_path)}")
        print(f"Estimated delivery time is: {distances[end]} minutes.")
        pathfinder.draw_graph(shortest_path)

class ShortestPathFinder:
    def __init__(self):
          self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges.setdefault(from_node, []).append((to_node, weight))
        self.edges.setdefault(to_node, []).append((from_node, weight))

    def use_dijkstra(self, graph, start):
        queue = [(0, start)]
        distances = {node: float('inf') for node in graph.edges}
        distances[start] = 0
        previous_nodes = {node: None for node in graph.edges}

        while queue:
            distance, node = heapq.heappop(queue)
            for neighbor, weight in graph.edges.get(node, []):
                distance = distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = node
                    heapq.heappush(queue, (distance, neighbor))

        return distances, previous_nodes

    def create_path(self, previous_nodes, start, end):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = previous_nodes[current]
            if current is None:
                return []
        path.append(start)
        return path[::-1]

    def draw_graph(self, shortest_path):
        import networkx as nx
        import matplotlib.pyplot as plt
        G = nx.Graph()
        for node in self.edges:
            for neighbor, weight in self.edges[node]:
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G, seed=42)
        edge_labels = nx.get_edge_attributes(G, 'weight')

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
        plt.title("Optimized Food Delivery App")
        plt.show()

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    try:
        clear_screen()
        print('*** Module 7 - Critical Thinking ***\n')
        DependencyChecker.ensure_package('networkx')
        DependencyChecker.ensure_package('matplotlib')
        TestCaseRunner.run_test()
    except Exception as e:
        print(e)

if __name__ == '__main__':  main()