def numOfAdjComputers(
    powerOutputs: list[int],
    boostedOutputs: list[int],
    powerMax: int
) -> int:
    #? Formula: Σ(powerOutputs) + Σ(boostedOutputs) * number_of_computers
    #! Sliding window
    n = len(powerOutputs)
    left = 0
    powerSum = 0
    boostSum = 0
    maxWindowSize = 0

    for right in range(n):
        powerSum += powerOutputs[right]
        boostSum += boostedOutputs[right]
        windowSize = right - left + 1
        totalPower = powerSum + boostSum * windowSize

        while totalPower > powerMax and left <= right:
            powerSum -= powerOutputs[left]
            boostSum -= boostedOutputs[right]
            left += 1
            windowSize = right - left + 1
            totalPower = powerSum + boostSum * windowSize
        
        maxWindowSize = max(maxWindowSize, windowSize)

    return maxWindowSize
            
        
powerOutputs =      [10,    20,     30,     40,     50,     60]
boostedOutputs =    [10,    9,      8,      7,      6,      5]
powerMax = 110




print(numOfAdjComputers(powerOutputs, boostedOutputs, powerMax))