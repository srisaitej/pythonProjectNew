# A = [1, 3, 1, 4, 2, 3, 5, 4]
# print(A.index(5))


def earliest_time_to_cross(X, A):
    # positions = set()
    # for time, position in enumerate(A):
    #     positions.add(position)
    #     if len(positions) == X:
    #         return time
    # return -1  # If the frog cannot jump to the other side
    if X in A:
        return A.index(X)
    else:
        return -1


# Example usage:
X = 5  # The target position
A = [1, 3, 1, 4, 2, 3, 5, 4]  # Positions where leaves fall into the river
print("Earliest time to cross:", earliest_time_to_cross(X, A))
