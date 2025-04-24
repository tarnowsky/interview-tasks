from collections import deque, defaultdict

packages = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
dependencies = [
    ('A', 'B'), 
    ('C', 'B'), 
    ('D', 'A'), 
    ('E', 'C'), 
    ('F', 'D'), 
    ('G', 'E'), 
    ('H', 'F'), 
    ('H', 'G')
]

#? O(N + D)
def packageOrder(packages: list[str], dependencies: list[tuple[str, str]]) -> list[str]:
    #? O(len(packages))
    in_degree_dict = {node: 0 for node in packages}
    graph = defaultdict(list)
    result = []

    #? O(len(dependencies))
    for from_node, to_node in dependencies:
        graph[from_node].append(to_node)
        in_degree_dict[to_node] += 1
    
    #? O(len(packages))
    q = deque([node for node, in_degree in in_degree_dict.items() if in_degree == 0])

    #? O(len(packages))
    while q:
        new_node = q.popleft()
        result.append(new_node)
        for node in graph[new_node]:
            in_degree_dict[node] -= 1
            if in_degree_dict[node] == 0:
                q.append(node)

    if len(result) != len(packages): 
        raise ValueError("Cyclic graph. Not possible to sort.")
    
    return result

print(packageOrder(packages, dependencies))