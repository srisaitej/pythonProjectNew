#my_str='''Srini's laptop'''
my_str='Srini\'s laptop'
print(my_str)

print(2==2.0)
print(int(2)==float(2))
print(1&2)
print(1|2)
print(1>>2)
print(1<<2)


def fun(str1="Hello", str2="World!"):
    print(str1, str2)


#fun(str2="Python!")
fun()

count = 0
while count < 3:
    print(count, end = ",")
    count += 1

print()

letters = ['A', 'B', 'C']
#letters[3]='D' #IndexError
#letters.insert(2,'D') #['A', 'B', 'D', 'C']
letters.append('D') #['A', 'B', 'C', 'D']
print(letters)


def factorial(x):
    if (x == 0):
        return 1
    else:
        return x * factorial(x - 1)




num = 3
print("The factorial of", num, "is", factorial(num))

x = 10

def fun():
    global x
    if x >= 10:
        x += 100


fun()
print(x) #110

print(2%6) #2

d = {'c': 3, 'a': 1, 'a': 5, 'a': 2}

print(d) #{'c': 3, 'a': 2}
print(d['a']) #2

lst = [[i * 2 for i in range(3)] for j in range(3)]
print(lst)



tpl = ('a', True, 'Python', 1, [2, 3, 4], ('five', 6))

print(tpl[-len(tpl)], end=' ')

print(tpl[tpl[3]], end=' ')

print(tpl[2:-2], end=' ')

print()
tp=(1,2,3,4,5,6,)
print(tp[2:-2]) #(3, 4)

print()
tp=[1,2,3,4,5,6,]
print(tp[2:-2]) #[3, 4]

print()
a=[2,4,5,3,2,8,6,2]
print(max(a)) #8
print(max(a,key=a.count)) #2
print(a[::-1]) #[2, 6, 8, 2, 3, 5, 4, 2]
print(list(reversed(a))) #[2, 6, 8, 2, 3, 5, 4, 2]

a.reverse()
print(a) #[2, 6, 8, 2, 3, 5, 4, 2]

print()
a=[2,4,5,3,2,8,6,2]
a.sort()
print(a)

print()
d={}
print(type(d)) #<class 'dict'>
print()
s=set()
print(type(s)) #<class 'set'>

#####Exception Handling#####
#####Pre-defined or Builtin Exceptions#####
''' eg: division by zero-----> ZeroDivisionError   ,
        invalid arguements---> TypeError,
        invalid variable-----> NameError,
        invalid module-------> ModuleNotFoundError
                               ValueError               
'''
print()
#####List methods#####
my_list=[10,'A',20,30,'X']
new_ele='S'
#my_list.insert(3,new_ele)
my_list[3:3]=new_ele
print(my_list) #[10, 'A', 20, 'S', 30, 'X']

capital_cities = {'UK':'London','USA':'Washington DC','India':'New Delhi','France':'Paris','Germany':'Berlin'}
inverted_cities = {capital:country for country,capital in capital_cities.items()}
print()
print(capital_cities)
#{'UK': 'London', 'USA': 'Washington DC', 'India': 'New Delhi', 'France': 'Paris', 'Germany': 'Berlin'}
print(inverted_cities)
#{'London': 'UK', 'Washington DC': 'USA', 'New Delhi': 'India', 'Paris': 'France', 'Berlin': 'Germany'}

print()

'''
*
**
***
****
*****
'''

for i in range(5):
    ln=''
    for j in range(i+1):
        ln += '*'
    print(ln)

print()
str='SKYSKYSKjhkjhjhkhfff'
mystrdict={char:0 for char in 'SKY'}
#print(mystrdict)
for char in str.upper():
    if char in mystrdict:
        mystrdict[char]+=1
print(mystrdict)


print()
str='SKYSKYSKjhkjhjhkhfff'
my_dict={}
for char in str:
    if char in my_dict:
        my_dict[char]+=1
    else:
        my_dict[char]=1
print(f'{my_dict}')


mystr=input('Enter a String').upper()
mystr='SKYskys'.upper()
countS=mystr.count('S')
countK=mystr.count('K')
countY=mystr.count('Y')
print(f'S={countS}')
print(f'K={countK}')
print(f'Y={countY}')
#
# print()
# s = 'cebad'
# mys=sorted(s)
# print(f'{mys=}') #mys=['a', 'b', 'c', 'd', 'e']
# print(f'{s=}') #s='cebad'
# mys1=''.join(mys)
# print(f'{mys1=}') #mys1='abcde'


# mystr='skySKY'
# mylist=[mystr.lower().count(x)for x in 'sky']
# print(mylist)
# print(f'S={mylist[0]}, K={mylist[1]}, Y={mylist[2]}')



# numlist=[]
# for i in range(10):
#     if i%2==0:
#         numlist.append(i)

numlist = [i for i in range(10) if i%2==0]

print(numlist)






