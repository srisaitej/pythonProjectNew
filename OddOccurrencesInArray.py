def find_odd_occurrence(A):
    result = 0
    for num in A:
        result ^= num  # Using XOR operation to find the odd-occurring element
    return result

# Example usage:
arr = [9, 9, 9, 7, 9, 7, 6]
print("Odd occurring element:", find_odd_occurrence(arr))


#print(f'{10^6=}')