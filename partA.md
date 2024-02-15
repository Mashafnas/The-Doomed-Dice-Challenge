#Total Combinations
total_combinations = 6 * 6
print("Total combinations possible:", total_combinations)
distribution = [[0] * 6 for _ in range(6)]

for i in range(1, 7):
    for j in range(1, 7):
        distribution[i-1][j-1] = (i, j)

# Displaying the distribution
print("Distribution of all possible combinations:")
for row in distribution:
    print(row)
probabilities = {}
for i in range(2, 13):
    count = sum(1 for row in distribution for val in row if sum(val) == i)
    probabilities[i] = count / total_combinations

# Displaying probabilities
print("\nProbability of each sum:")
for key, value in probabilities.items():
    print(f"P(Sum = {key}) = {value}")# The-Doomed-Dice-Challenge
