## Task Description
Write a function that, given an array of entities and an integer N, keep looping around the array removing the Nth remaining entity until there is only one entity remaining. Return the remaining entity. Example Input: 2 elements, example loop below ...A E....B ..D.C Loop 1: Step 2 elements, flag B ...A E....[B] ..D.C Loop 2: Step 2 elements, flag D ...A E....x .[D]C Loop 3: Step 2 elements, Flag A ...[A] E....x ..x.C Loop 4: Step 2 elements, Flag E (NOT C, since B no longer exists) ....x... [E]..x ..x.C.. Output: C

---

### Solution
Math function is a solution for the Joseph problem.
However if one want to see the logic of it the solution would be to use deque, rotating it and poping the left most element.

### Constraints and Complexity
- **Time Complexity**: O(n) or O(n*step)
- **Space Complexity**: O(1) or O(n)