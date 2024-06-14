
def missingElement(arr):
    n=len(arr)+1
    exp_sum=n*(n+1)//2
    act_sum=sum(arr)
    return  exp_sum-act_sum

my_list=[1,4,3,5]
print(f'missing element in the {my_list} is {missingElement(my_list)}')