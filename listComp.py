####List Comprehension

'''
A list comprehension generally consists of these parts :

Output expression,
Input sequence,
A variable representing a member of the input sequence and
An optional predicate part.
'''

ls=[x**2 for x in range(1,11) if x%2 == 1 ]
print(ls)   #[1, 9, 25, 49, 81]

ls1=[x**2 if x%2==1 else x*2 for x in range(1,11)]
#ls1=[x**2 for x in range(1,11) if x%2==1 else x*2] #wrong statement
print(ls1)   #[1, 4, 9, 8, 25, 12, 49, 16, 81, 20]

# below list contains square of all odd numbers from
# range 1 to 10
odd_squares=[x**2 for x in range(1,11) if x%2==1]
print(f'{odd_squares=}')     #odd_squares=[1, 9, 25, 49, 81]

#the above without list comprehension
odd_square=[]
for i in range(1,11):
    if i%2==1:
        odd_square.append(i**2)
print(f'{odd_square=}')  #odd_square=[1, 9, 25, 49, 81]


# below list contains power of 2 from 1 to 8
power_of_two = [2**x for x in range(1,9)]
print(f'{power_of_two=}')   #power_of_two=[2, 4, 8, 16, 32, 64, 128, 256]

list1 = [x**2 if x%2==1 else x*2 for x in range(1,11)]
print(f'{list1=}') #list1=[1, 4, 9, 8, 25, 12, 49, 16, 81, 20]

#The above can be written as
list1=[]
for i in range(1,11):
    if i%2==1:
        list1.append(i**2)
    else:
        list1.append(i*2)
print(f'{list1=}')   #list1=[1, 4, 9, 8, 25, 12, 49, 16, 81, 20]


noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primenums= [x for x in range(2, 50) if x not in noprimes]
print(f'{primenums=}')   #primenums=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


primes=[]
for i in range(2,50):
    flag=0
    for j in range(2,i-1):
        if i%j==0:
            flag=1
            break
    if flag==0:
        primes.append(i)
print(f'{primes=}')   #primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# list for lowering the characters
str=[x.lower() for x in ['A','B','C','D']]
print(f'{str=}')   #str=['a', 'b', 'c', 'd']

# list which extracts number
string1 = "my phone number is : 11122 !!"
nums=[x for x in string1 if x.isdigit()]
nums1=[int(x) for x in string1 if x.isdigit()]
print(f'Extracted digits-chars : {nums}')  #Extracted digits : ['1', '1', '1', '2', '2']
print(f'Extracted digits-ints : {nums}')  #Extracted digits : [1, 1, 1, 2, 2]

# A list of list for multiplication table
n=5
table_five=[[n,a,n*a] for a in range(1,11)]
print(table_five)
#[[5, 1, 5], [5, 2, 10], [5, 3, 15], [5, 4, 20], [5, 5, 25], [5, 6, 30], [5, 7, 35], [5, 8, 40], [5, 9, 45], [5, 10, 50]]
print("\nMultiplication Table")  
for i in table_five:
    print(i)





words=['Srinivas','Kamala','Sri Sai Tejas','Anish Krishang']

#List Comprehension
words_len=[len(name) for name in words]
print(words_len)  #[8, 6, 13, 14]

#Dictionary Compreshension
words_dict={name:len(name) for name in words}
print(words_dict) #{'Srinivas': 8, 'Kamala': 6, 'Sri Sai Tejas': 13, 'Anish Krishang': 14}


names = ['Mike','Sam','Jason','Sam','Smith','Sam','Jason']

count_dict={name:names.count(name) for name in names}
print(count_dict)  #{'Mike': 1, 'Sam': 3, 'Jason': 2, 'Smith': 1}

mystr='GeeksQuizg'

#string=input(f"Enter a name: ")
#for _ in range(10):
#    print(string)



