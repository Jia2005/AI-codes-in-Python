#Greedy Best First Search & A* 
from enum import Enum 
from collections import defaultdict 
from typing import Dict, List, Optional, Tuple 
import heapq 
 
class SearchType(Enum): 
    GBFS = "gbfs" 
    ASTAR = "astar" 
 
class Graph: 
    def __init__(self, num_nodes: int): 
        self.num_nodes = num_nodes 
        self.graph = defaultdict(list) 
        self.heuristics = {} 
     
    def add_edge(self, u: int, v: int, weight: float): 
        self.graph[u].append((v, weight)) 
     
    def set_heuristic(self, node: int, value: float): 
        self.heuristics[node] = value 
     
    def get_heuristic(self, node: int) -> float: 
        return self.heuristics.get(node, float('inf')) 
 
class SearchAlgorithms: 
    def __init__(self): 
        self.path: Dict[int, Optional[Tuple[int, float]]] = {} 
     
    def gbfs(self, graph: Graph, start: int, target: int) -> Tuple[List[int], float]: 
        current = start 
        path = [start] 
        total_weight = 0 
        visited = {start} 
         
        while current != target: 
            neighbors = [(n, w) for n, w in graph.graph[current] if n not in visited] 
            if not neighbors: 
                return [], 0 
                 
            next_node = min(neighbors, key=lambda x: graph.get_heuristic(x[0])) 
            next_node, weight = next_node 
             
            visited.add(next_node) 
            path.append(next_node) 
            total_weight += weight 
            current = next_node 
             
        return path, total_weight 
 
    def astar(self, graph: Graph, start: int, target: int) -> Tuple[List[int], float]: 
        g_score = {start: 0} 
        open_set = [(graph.get_heuristic(start), start)] 
        closed_set = set() 
        came_from = {start: None} 
        weights = {} 
         
        while open_set: 
            _, current = heapq.heappop(open_set) 
             
            if current in closed_set: 
                continue 
                 
            if current == target: 
                path = [] 
                total_weight = 0 
                while current is not None: 
                    path.append(current) 
                    if current in weights: 
                        total_weight += weights[current] 
                    current = came_from[current] 
                return path[::-1], total_weight 
             
            closed_set.add(current) 
             
            for neighbor, weight in graph.graph[current]: 
                if neighbor in closed_set: 
                    continue 
                     
                tentative_g = g_score[current] + weight 
                 
                if neighbor not in g_score or tentative_g < g_score[neighbor]: 
                    came_from[neighbor] = current 
                    weights[neighbor] = weight 
                    g_score[neighbor] = tentative_g 
                    f_score = tentative_g + graph.get_heuristic(neighbor) 
                    heapq.heappush(open_set, (f_score, neighbor)) 
         
        return [], 0 
     
    def search(self, search_type: SearchType, graph: Graph, start: int, target: int) -> 
Tuple[List[int], float]: 
        match search_type: 
            case SearchType.GBFS: 
                return self.gbfs(graph, start, target) 
            case SearchType.ASTAR: 
                return self.astar(graph, start, target) 
            case _: 
                raise ValueError("Invalid search type") 
 
def get_valid_input(prompt: str, min_val: int, max_val: int) -> int: 
    while True: 
        try: 
            value = int(input(prompt)) 
            if min_val <= value <= max_val: 
                return value 
            print(f"Please enter a value between {min_val} and {max_val}") 
        except ValueError: 
            print("Please enter a valid integer") 
 
def get_valid_float(prompt: str) -> float: 
    while True: 
        try: 
            return float(input(prompt)) 
        except ValueError: 
            print("Please enter a valid number") 
 
def main(): 
    num_nodes = get_valid_input("Enter the number of nodes (1-100): ", 1, 100) 
    g = Graph(num_nodes) 
     
    start_node = get_valid_input(f"Enter the start node (0-{num_nodes-1}): ", 0, num_nodes
1) 
    target_node = get_valid_input(f"Enter the target node (0-{num_nodes-1}): ", 0, 
num_nodes-1) 
     
    print("\nEnter heuristic values for each node:") 
    for i in range(num_nodes): 
        h_value = get_valid_float(f"Heuristic value for node {i}: ") 
        g.set_heuristic(i, h_value) 
     
    num_edges = get_valid_input("\nEnter the number of edges: ", 0, num_nodes * 
(num_nodes - 1)) 
    print("\nEnter edges and weights (format: source destination weight):") 
     
    for i in range(num_edges): 
        while True: 
            try: 
                source, dest, weight = input(f"Edge {i+1}: ").split() 
                source = int(source) 
                dest = int(dest) 
                weight = float(weight) 
                 
                if not (0 <= source < num_nodes and 0 <= dest < num_nodes): 
                    print(f"Nodes must be between 0 and {num_nodes-1}") 
                    continue 
                 
                if weight < 0: 
                    print("Weight must be non-negative") 
                    continue 
                 
                g.add_edge(source, dest, weight) 
                break 
            except ValueError: 
                print("Invalid input. Please use format: source destination weight") 
     
    print("\nSelect search algorithm:") 
    print("1. Greedy Best First Search") 
    print("2. A* Search") 
     
    algo_choice = get_valid_input("Enter your choice (1-2): ", 1, 2) 
    searcher = SearchAlgorithms() 
    search_type = SearchType(["gbfs", "astar"][algo_choice - 1]) 
     
    try: 
        path, total_weight = searcher.search(search_type, g, start_node, target_node) 
         
        print(f"\n{search_type.value.upper()} result:") 
        if path: 
            print(f"Path found: {' -> '.join(map(str, path))}") 
            print(f"Total path weight: {total_weight}") 
        else: 
            print("No path found") 
             
    except ValueError as e: 
        print(f"Error: {str(e)}") 
 
if __name__ == "__main__": 
    main()
