## Task Description
Given an input of two arrays that represent computers' power output (powerOutputs) and boosted output (boostedOutputs) and a maximum allowed power (powerMax), return the maximum amount of adjacent computers that are less than or equal to powerMax given the formula totalPowerOutput = powerOutputs[i] + powerOutputs[i + 1...] + (boostedOutputs[i] + boostedOutputs[i + 1...] * numOfAdjacentComputers).

---

### Solution
Sliding window. Right till the sum exceed the limit. Then left till it will be in the limit.  
It is important to know the nature of the task. It asks not about the value but rather the max window size, so the exact value is not important. 


### Constraints and Complexity
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)