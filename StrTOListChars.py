

#######SPLIT STRING INTO A LIST OF CHARACTERS#######

str='sriNi'
print(str.upper())  #SRINI
print(str.lower())  #srini
print(str.title())  #Srini


###1) Using unpack(*) method
str1=[*str]
print(f'{str1=}')   #str=['s', 'r', 'i', 'N', 'i']


###2)Python Split String in List using a loop
str1=[]
for letter in str:
    str1.append(letter)

print(f'{str1=}')   #str1=['s', 'r', 'i', 'N', 'i']

###3)Python Split String in List using List Comprehension
str1=[i for i in str]
print(f'{str1=}  {type(str1)=}')   #str1=['s', 'r', 'i', 'N', 'i']  type(str1)=<class 'list'>


###4)Python Split String using a list() typecasting
str1=list(str)
print(f'{str1=}')   #str1=['s', 'r', 'i', 'N', 'i']


###5)Python Split String in List using Extend() Function
str1=[]
str1.extend(str)
print(f'{str1=}')   #str1=['s', 'r', 'i', 'N', 'i']


###6)Python Split String in List using List Slicing
str1=[]
str1[:]=str
print(f'{str1=}')    #str1=['s', 'r', 'i', 'N', 'i']

[*s]='Anish'
s1=s
s2=s
print(f'{s=}')   #s=['A', 'n', 'i', 's', 'h']
print(f'{s.reverse()=}')   #s.reverse()=None   #reverse() is a method of String
print(f'{s=}')    #s=['h', 's', 'i', 'n', 'A']

#print(type(s1))   #<class 'list'>

s2.sort()
print(f'{s2=}')   #s2=['A', 'h', 'i', 'n', 's']

s1.sort(reverse=True)
print(f'{s1=}')   #s1=['s', 'n', 'i', 'h', 'A']











l1=[1,2,3,4,5]
print(f'{l1[-2]=}')   #returns 4
print(f'{ len(l1)=}')   #len(l1)=5



#print(str.split(' '))


