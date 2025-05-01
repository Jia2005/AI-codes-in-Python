#DFS, DLS & DFID 
from enum import Enum 
from collections import defaultdict 
from typing import Dict, List, Set, Optional, Tuple 
 
class SearchType(Enum): 
    DFS = "dfs" 
    DLS = "dls" 
    DFID = "dfid" 
 
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
        self.visited: Set[int] = set() 
        self.path: List[int] = [] 
        self.path_weight: float = 0.0 
     
    def dfs(self, graph: Graph, start: int, target: int) -> Tuple[Optional[List[int]], float]: 
        self.visited = set() 
        self.path = [] 
        self.path_weight = 0.0 
        return self._dfs_util(graph, start, target) 
     
    def _dfs_util(self, graph: Graph, current: int, target: int) -> Tuple[Optional[List[int]], 
float]: 
        self.visited.add(current) 
        self.path.append(current) 
         
        if current == target: 
            return self.path.copy(), self.path_weight 
         
        for neighbor, weight in graph.graph[current]: 
            if neighbor not in self.visited: 
                self.path_weight += weight 
                result, _ = self._dfs_util(graph, neighbor, target) 
                if result: 
                    return result, self.path_weight 
                self.path_weight -= weight 
         
        self.path.pop() 
        return None, 0.0 
     
    def dls(self, graph: Graph, start: int, target: int, depth_limit: int) -> 
Tuple[Optional[List[int]], float]: 
        self.visited = set() 
        self.path = [] 
        self.path_weight = 0.0 
        return self._dls_util(graph, start, target, depth_limit) 
     
    def _dls_util(self, graph: Graph, current: int, target: int, depth_limit: int) -> 
Tuple[Optional[List[int]], float]: 
        if depth_limit < 0: 
            return None, 0.0 
         
        self.visited.add(current) 
        self.path.append(current) 
         
        if current == target: 
            return self.path.copy(), self.path_weight 
         
        if depth_limit > 0: 
            for neighbor, weight in graph.graph[current]: 
                if neighbor not in self.visited: 
                    self.path_weight += weight 
                    result, _ = self._dls_util(graph, neighbor, target, depth_limit - 1) 
                    if result: 
                        return result, self.path_weight 
                    self.path_weight -= weight 
         
        self.path.pop() 
        self.visited.remove(current) 
        return None, 0.0 
     
    def dfid(self, graph: Graph, start: int, target: int, max_depth: int) -> 
Tuple[Optional[List[int]], float]: 
        for depth in range(max_depth + 1): 
            result, weight = self.dls(graph, start, target, depth) 
            if result: 
                return result, weight 
        return None, 0.0 
     
    def search(self, search_type: SearchType, graph: Graph, start: int, target: int,  
               depth_limit: int = None, max_depth: int = None) -> Tuple[Optional[List[int]], 
float]: 
        match search_type: 
            case SearchType.DFS: 
                return self.dfs(graph, start, target) 
            case SearchType.DLS: 
                if depth_limit is None: 
                    raise ValueError("Depth limit must be specified for DLS") 
                return self.dls(graph, start, target, depth_limit) 
            case SearchType.DFID: 
                if max_depth is None: 
                    raise ValueError("Max depth must be specified for DFID") 
                return self.dfid(graph, start, target, max_depth) 
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
    print("1. DFS") 
    print("2. DLS") 
    print("3. DFID") 
     
    algo_choice = get_valid_input("Enter your choice (1-3): ", 1, 3) 
     
    searcher = SearchAlgorithms() 
    search_type = SearchType(["dfs", "dls", "dfid"][algo_choice - 1]) 
     
    depth_limit = None 
    max_depth = None 
     
    if search_type == SearchType.DLS: 
        depth_limit = get_valid_input("Enter depth limit: ", 0, num_nodes) 
    elif search_type == SearchType.DFID: 
        max_depth = get_valid_input("Enter maximum depth: ", 0, num_nodes) 
     
    try: 
        path, total_weight = searcher.search(search_type, g, start_node, target_node,  
                                           depth_limit=depth_limit, max_depth=max_depth) 
         
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
