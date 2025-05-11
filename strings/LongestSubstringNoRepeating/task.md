## Task Description
Given a string s, find the length of the longest substring without repeating characters.

---

### Solution
Sliding window but keep only index of chars.  
Slide **l** to the index of the curr reapeted char + 1.


### Constraints and Complexity
- **Time Complexity**: O(N)
- **Space Complexity**: O(N)