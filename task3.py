import heapq


def minimum_connection_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        connection_cost = first + second
        total_cost += connection_cost

        heapq.heappush(cables, connection_cost)

        print(
            f"Connect {first} and {second} "
            f"-> cost: {connection_cost}"
        )

    return total_cost


cables = [4, 3, 2, 6]

result = minimum_connection_cost(cables)

print("Minimum total cost:", result)