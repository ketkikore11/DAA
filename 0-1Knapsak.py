def knapsack_01(items, capacity):
    n = len(items)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, profit, weight = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w], table[i - 1][w - weight] + profit)

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][2]

    selected_items.reverse()
    return table[n][capacity], selected_items, table

# Input from the user
num_items = int(input("Enter the number of items: "))
items = []
for i in range(num_items):
    name = input("Item name: ")
    profit = int(input("Profit: "))
    weight = int(input("Weight: "))
    items.append((name, profit, weight))

capacity = int(input("Enter the knapsack capacity: "))

# Solve the knapsack problem
max_profit, selected_items, table = knapsack_01(items, capacity)

# Print the results
print("\nMaximum Profit:", max_profit)
print("Selected Items:")
for item in selected_items:
    print(f"Item: {item[0]}, Profit: {item[1]}, Weight: {item[2]}")

# Print the dynamic programming table
print("\nDynamic Programming Table:")
for row in table:
    print(row)
#Time complexity= O(n*W), n=no.of items and W=capacity of knapsack
