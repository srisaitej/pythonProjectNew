
def binary_gap(num):

    binary_rep=bin(num)[2:]
    print(f'Binary equivalent of {num} : {binary_rep}')  #10000010001
    #print(type(binary_rep))  #<class 'str'>
    max_gap=0
    curr_gap=0
    started=False

    for digit  in binary_rep:
        if digit == '1':
            if not started:
                started = True
            else:
                max_gap=max(max_gap,curr_gap)
                curr_gap=0
        elif digit == '0' and started:
            curr_gap+=1

    return max_gap


# Example usage:
number = 1041
#print("Binary Gap of", number, ":", binary_gap(number))
print(f'Binary gap of the number {number} : {binary_gap(number)}')
