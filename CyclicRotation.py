'''
a=[1,2,3,4,5]
print(f'{a[-1:]=}')   #a[-1:]=[5] ----prints the last element
print(f'{a[:-1]=}')   #a[:-1]=[1, 2, 3, 4] -----prints all the elements from the start but not including the last
'''

def rotate_nums_array(num_arr,k):
    #print(f'{num_arr=}')
    #print(f'{not num_arr=}')
    #empty list returns False and not emptylist returns True

    if not num_arr:
        return []
    k=k%len(num_arr)  #returns the remainder
    return num_arr[-k:]+num_arr[:-k]

a=[1,2,3,4,5]
k=2
print(f'Given array : {a} , after rotating {k} times, then the array is {rotate_nums_array(a,k)}')