import time

# Function to solve the fractional knapsack problem
def fractional_knapsack(value, weight, capacity):
    # Create a list of tuples with calculated value/weight ratios
    val_per_weight = [(v / w, w, v) for v, w in zip(value, weight)]
    
    # Sort items by their value-to-weight ratio in descending order
    val_per_weight.sort(reverse=True)

    total_value = 0  # Initialize total value
    fractions = [0] * len(value)  # Initialize a list to keep track of fractions selected

    for val_per_w, w, v in val_per_weight:
        if capacity == 0:
            break

        # Take the whole item if capacity is greater than or equal to the item's weight
        if w <= capacity:
            fractions[val_per_weight.index((val_per_w, w, v))] = 1
            total_value += v
            capacity -= w
        else:
            # If capacity is less, take a fraction of the item
            fraction = capacity / w
            fractions[val_per_weight.index((val_per_w, w, v))] = fraction
            total_value += v * fraction
            capacity = 0

    return total_value, fractions

# Input from the user
n = int(input("Enter the number of items: "))
values = []
weights = []

for i in range(n):
    value = float(input(f"Enter the value of item {i + 1}: "))
    weight = float(input(f"Enter the weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

knapsack_capacity = float(input("Enter the knapsack capacity: "))

st = time.time()
max_value, fractions_selected = fractional_knapsack(values, weights, knapsack_capacity)
end = time.time()

print("Maximum value (profit) that can be obtained:", max_value)
print("Fractions of items to be selected:", fractions_selected)
print("Time taken:", end - st, "seconds")

#Time complexity=O(n*logn)
