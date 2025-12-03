def find_max_joltage(num_length, bank):
    bank_length = len(bank)
    max_joltage = []
    last_max_pos = -1
    
    for remaining_digits in range(num_length, 0, -1):
        range_max = (0, "0")
        for pos in range(last_max_pos+1, bank_length - (remaining_digits-1)):
            if bank[pos] > range_max[1]: 
                range_max = (pos, bank[pos])
        last_max_pos = range_max[0]
        max_joltage.append(range_max[1])
    
    return(int("".join(max_joltage)))


with open("data.txt", "r") as f:
    joltages = ([], [])
    
    for bank in f:
        bank = bank.strip()
        joltages[0].append(find_max_joltage(2, bank))
        joltages[1].append(find_max_joltage(12, bank))
    
    print(sum(joltages[0]), sum(joltages[1]))
