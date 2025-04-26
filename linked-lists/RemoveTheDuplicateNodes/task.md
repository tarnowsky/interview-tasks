## Task Description
Remove the duplicate node(s) from a linked list.

---

### Solution
Using hashmap and node-walking. Nice to remember:  
1. check while node->next not while node. 
2. Do not switch ot next if its not valid node. Remove duplicate and and check next instead.

### Constraints and Complexity
- **Time Complexity**: O(n)
- **Space Complexity**: worst case O(n) (when no duplicates)