def numOfAdjComputers(
    powerOutputs: list[int],
    boostedOutputs: list[int],
    powerMax: int
) -> int:
    #? Formula: Σ(powerOutputs) + Σ(boostedOutputs) * number_of_computers
    #! Brute force
    n = len(powerOutputs)
    curr_max_power = 0
    for i in range(n):
        for j in range(i+1, n+1):
            number_of_computers = j - i
            outputPower = sum(powerOutputs[i:j])
            boostedPower = sum(boostedOutputs[i:j])

            power = outputPower + boostedPower * number_of_computers
            if powerMax >= power > curr_max_power:
                curr_max_power = power
                result = number_of_computers
    return result

powerOutputs = [30, 40, 20]
boostedOutputs = [5, 5, 5]
powerMax = 110

expectedOutput = 2

print(numOfAdjComputers(powerOutputs, boostedOutputs, powerMax))