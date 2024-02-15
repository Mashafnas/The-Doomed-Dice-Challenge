def undoom_dice(Die_A, Die_B):
    # Calculate the original probabilities of obtaining each sum
    original_probabilities = [0] * 12
    for i in range(1, 7):
        for j in range(1, 7):
            original_probabilities[i + j - 2] += 1

    # Adjust Die_A to ensure no face has more than 4 spots
    New_Die_A = [min(4, spots) for spots in Die_A]

    # Calculate the total number of combinations after modifying Die_A
    total_combinations = sum(New_Die_A) * len(Die_B)

    # Calculate the desired frequency for each sum
    desired_frequencies = [int(prob * total_combinations) for prob in original_probabilities]

    # Adjust Die_B to maintain the original probabilities
    New_Die_B = [desired_frequencies[i] // len(Die_B) for i in range(11)]

    return New_Die_A, New_Die_B

# Test with the provided example
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)

print("New Die_A:", New_Die_A)
print("New Die_B:", New_Die_B)
