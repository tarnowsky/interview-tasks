## Task Description
Given a sorted dictionary (array of words) in an alien language, determine the order of characters in the language.

### Solution
1. **Build a Directed Graph**: Compare adjacent words to identify the first differing characters, creating directed edges between them.  
    Example:  
    Words: `bbc`, `bba`, `dg`, `da`  
    Graph:  
    - `c -> a`  
    - `b -> d`  
    - `g -> a`

2. **Topological Sorting**: Use Kahn's Algorithm:  
    - Compute in-degrees for all nodes:  
      - `c: 0`, `b: 0`, `g: 0`, `d: 1`, `a: 2`  
    - Steps:  
      1. Select a node with in-degree 0.  
      2. Append it to the result.  
      3. Remove it from the graph and update in-degrees.  
      4. Repeat until no nodes remain.

### Constraints and Complexity
- The graph must be a Directed Acyclic Graph (DAG).  
- Time and space complexity: **O(V + E)**  
  where `V` is the number of vertices and `E` is the number of edges.
