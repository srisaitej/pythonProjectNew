def TapeEquilibrium(arr):
    total_sum=sum(arr)
    left_sum=0
    min_diff=float('inf')   #The inf constant is equivalent to float('inf').

    for num in arr[:-1]:
        left_sum+=num
        right_sum=total_sum-left_sum
        diff=abs(right_sum-left_sum)
        min_diff=min(min_diff,diff)

    return min_diff

my_list=[3,1,2,4,3]
print(f'Minimum difference : {TapeEquilibrium(my_list)}')

