## Task Description
Having a number N return True if the number is a power of two.

ex. 
input 16
output True

input 15
output True

input 1
output True

---

### Solution
Use bit masks. Powers of 2 will always look like one 1 and 0s in bit format. Mask it with n-1.

### Constraints and Complexity
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)