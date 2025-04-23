from collections import deque

#? Math solution O(n)
def josephProblemWinner(arr: list[str], step: int) -> str:
    n = len(arr)
    index = 0
    #? O(n)
    for i in range(1, n+1):
        index = (index + step) % i
    return arr[index]

#? Simulation O(n*step)
def josephSimulation(arr: list[str], step: int) -> str:
    indices = deque(range(len(arr)))
    #? O(n)
    while len(indices) > 1:
        #? O(k)
        indices.rotate(-(step - 1))
        #? O(1)
        indices.popleft()
    return arr[indices[0]]
    

arr = [chr(i) for i in range(65, 91)]
step = 10

print(josephProblemWinner(arr, step), josephSimulation(arr, step))