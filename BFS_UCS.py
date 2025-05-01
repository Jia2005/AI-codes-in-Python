#BFS, UCS
from enum import Enum 
from collections import defaultdict, deque 
from typing import Dict, List, Set, Optional, Tuple 
import heapq 
 
class SearchType(Enum): 
    BFS = "bfs" 
    UCS = "ucs" 
 
class Graph: 
    def __init__(self, num_nodes: int): 
        self.num_nodes = num_nodes 
        self.graph = defaultdict(list) 
     
    def add_edge(self, u: int, v: int, weight: float): 
        self.graph[u].append((v, weight)) 
     
    def validate_node(self, node: int) -> bool: 
        return 0 <= node < self.num_nodes 
 
class SearchAlgorithms: 
    def __init__(self): 
        self.path: Dict[int, Tuple[int, float]] = {}   
     
    def reconstruct_path(self, start: int, target: int) -> Tuple[List[int], float]: 
        """Reconstruct path from start to target using stored parent pointers""" 
        if target not in self.path: 
            return None, 0.0 
         
        path = [] 
        current = target 
        total_weight = 0.0 
         
        while current is not None: 
            path.append(current) 
            parent_info = self.path.get(current) 
            if parent_info is None: 
                break 
            parent, weight = parent_info 
            total_weight += weight 
            current = parent 
         
        path.reverse() 
        return path if path[0] == start else None, total_weight 
 
    def bfs(self, graph: Graph, start: int, target: int) -> Tuple[Optional[List[int]], float]: 
        """Breadth-First Search implementation""" 
        self.path = {start: (None, 0.0)} 
        queue = deque([start]) 
        visited = {start} 
         
        while queue: 
            current = queue.popleft() 
             
            if current == target: 
                return self.reconstruct_path(start, target) 
             
            for neighbor, weight in graph.graph[current]: 
                if neighbor not in visited: 
                    visited.add(neighbor) 
                    queue.append(neighbor) 
                    self.path[neighbor] = (current, weight) 
         
        return None, 0.0 
 
    def ucs(self, graph: Graph, start: int, target: int) -> Tuple[Optional[List[int]], float]: 
        """Uniform Cost Search implementation""" 
        self.path = {start: (None, 0.0)} 
        priority_queue = [(0, start)]   
        visited = set() 
         
        while priority_queue: 
            total_cost, current = heapq.heappop(priority_queue) 
             
            if current in visited: 
                continue 
                 
            visited.add(current) 
             
            if current == target: 
                return self.reconstruct_path(start, target) 
             
            for neighbor, weight in graph.graph[current]: 
                if neighbor not in visited: 
                    new_cost = total_cost + weight 
                    if neighbor not in self.path or new_cost < self.path[neighbor][1]: 
                        self.path[neighbor] = (current, weight) 
                        heapq.heappush(priority_queue, (new_cost, neighbor)) 
         
        return None, 0.0 
     
    def search(self, search_type: SearchType, graph: Graph, start: int, target: int) -> 
Tuple[Optional[List[int]], float]: 
        """Switch-case style method to select and execute the appropriate search algorithm""" 
        match search_type: 
            case SearchType.BFS: 
                return self.bfs(graph, start, target) 
            case SearchType.UCS: 
                return self.ucs(graph, start, target) 
            case _: 
                raise ValueError("Invalid search type") 
 
def get_valid_input(prompt: str, min_val: int, max_val: int) -> int: 
    """Get and validate integer input within specified range""" 
    while True: 
        try: 
            value = int(input(prompt)) 
            if min_val <= value <= max_val: 
                return value 
            print(f"Please enter a value between {min_val} and {max_val}") 
        except ValueError: 
            print("Please enter a valid integer") 
 
def main(): 
    num_nodes = get_valid_input("Enter the number of nodes (1-100): ", 1, 100) 
     
    g = Graph(num_nodes) 
     
    start_node = get_valid_input(f"Enter the start node (0-{num_nodes-1}): ", 0, num_nodes
1) 
    target_node = get_valid_input(f"Enter the target node (0-{num_nodes-1}): ", 0, 
num_nodes-1) 
     
    num_edges = get_valid_input("Enter the number of edges: ", 0, num_nodes * (num_nodes - 1)) 
     
    print("\nEnter edges and weights (format: source destination weight):") 
    for i in range(num_edges): 
        while True: 
            try: 
                source, dest, weight = input(f"Edge {i+1}: ").split() 
                source = int(source) 
                dest = int(dest) 
                weight = float(weight) 
                 
                if not g.validate_node(source) or not g.validate_node(dest): 
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
    print("1. BFS") 
    print("2. UCS") 
     
    algo_choice = get_valid_input("Enter your choice (1-2): ", 1, 2) 
     
    searcher = SearchAlgorithms() 
    search_type = SearchType(["bfs", "ucs"][algo_choice - 1]) 
     
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
