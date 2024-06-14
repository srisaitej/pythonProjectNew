




#1. Write me a function called add that takes in two parameters, x and y, and returns
# the addition of those two parameters

def add(a,b):
    return a+b

a=int(input('Enter a number :'))
b=int(input('Enter a number :'))
print(f'Sum of {a} and {b} is {add(a,b)}')


#2. Create a function called calculator that takes in 3 parameters func, a and b.
#if func is "add", i want it to return the addition of a and b.
#if func is "multiply" i want it to return the multiplication of a and b.
#if func is anything else, i want it to return a minus b


def calculator(func, a, b):
    if func.lower()=='add':
        return a+b
    elif func.lower() == 'multiply':
        return a*b
    else:
        return a-b

print(calculator('add',10,20))
print(f'{calculator("multiply",10,20)=}') #calculator("multiply",10,20)=200
print(calculator('other',20,10))


#3. The customer is complaining that the output of the function isn't telling them what it's doing.
#Can you add print statements under each if/elif/else that says what the function is doing, and
#what numbers it's doing it to?


def calculator(func, a, b):
    if func.lower()=='add':
        print(f'{a} + {b} = {a+b}')

    elif func.lower() == 'multiply':
        print(f'{a} * {b} = {a*b}')

    else:
        print(f'{a} - {b} = {a-b}')


calculator('add',10,20)
calculator("multiply",10,20)
calculator('other',20,10)


#4. Starting with animals = ['dog', 'cat', 'mouse'], i want you to append three new animals onto the list.
#Create a new list called cars, containing 3 car brands.
#Make a list called everything, which contains the contents of animals and carsprint the 4th element in everything.
animals = ['cat','dog','mouse']
animals.extend(['horse','cow','sheep'])
print(animals)  #['cat', 'dog', 'mouse', 'horse', 'cow', 'sheep']

cars=['Tesla','JLR','BMW']
print(cars)  #['Tesla', 'JLR', 'BMW']

everything=animals+cars
print(everything) #['cat', 'dog', 'mouse', 'horse', 'cow', 'sheep', 'Tesla', 'JLR', 'BMW']

print(animals[3]) #horse
print(everything[3])  #horse

#5. dans_fat_list = ['hello','hey','hi','howdy','pokemon','bass','the matrix','cool']
#define a new empty list called udays_skinny_list
#then go through dans_fat_list using a for loop, and append any item in it that contains an 'o' to udays_skinny_list.
# Then print udays_skinny_list.

dans_fat_list = ['hello','hey','hi','howdy','pokemon','bass','the matrix','cool']
#udays_skinny_list=[]
#udays_skinny_list=[x for x in dans_fat_list if x.__contains__('o')]  #['hello', 'howdy', 'pokemon', 'cool']
#udays_skinny_list=[x for x in dans_fat_list if 'o' in x]  #['hello', 'howdy', 'pokemon', 'cool']


udays_skinny_list=[x for x in dans_fat_list if 'o' in x and 'h' in x]  #['hello', 'howdy']
print(udays_skinny_list)

###Pallindrome
def pallindrome(word):
    #if word == word[::-1]:
    if word == ''.join((reversed(word))):
        return True
    else:
        return False

word = input('Enter a word :')
if(pallindrome(word)):
    print(f'The given word {word} is Pallindrome')
else:
    print(f'The given word {word} is not Pallindrome')




###Removing Duplicates from the list

a_list=[1,2,1,2,4,5,7,6,4,3,2,8,6]
#b_list=list(dict.fromkeys(a_list))
b_list=list(set(a_list))

print(f'{a_list=}')
print(f'{b_list}')


####Anagram
def anagram(s1,s2):
    a=sorted(s1.lower().replace(' ',''))
    b=sorted(s2.lower().replace(' ',''))

    print(list_to_string(a))
    print(list_to_string(b))

    return a == b


def list_to_string(l1):
    newstr = ''.join(l1)
    return newstr

#    newstr = ''
#    for x in l1:
#        newstr += x
#    return newstr



#str1 = ' Astron omer '
#str2 = 'Moon Starer'
str1 = 'Java'
str2 = 'Python'

if(len(str1)==len(str2)):
    if anagram(str1,str2):
        print(f'{str1} and {str2} are Anagram')
    else:
        print(f'{str1} and {str2} are not Anagram')
else:
    print(f'{str1} and {str2} are not Anagram')

'''
# def non_repeating_char(mystr1):
#     counter={}
#     mystr1=mystr1.lower()
#     for char in mystr1:
#         if char in counter:
#             counter[char]+=1
#         else:
#             counter[char]=1
#
#     for char,char_count in counter.items():
#         print(char, char_count)
#         if char_count==1:
#             return char
#
#
# mystr='SkyGlass'
# #mystr='GeeksQuizg'
# print(f'First non-repeating character in \'{mystr}\' is {non_repeating_char(mystr)}')



# import random
# randomlist = []
# for i in range(0,5):
#     n = random.randint(1,50)
#     randomlist.append(n)
# randomlist.sort()
# print(randomlist)
# #print(sorted(randomlist))


def move1(str1):
    charB=str1.count('B')
    charA=str1.count('A')
    charN=str1.count('N')
    print(f'As :{charA}, Bs :{charB}, Ns :{charN}')
    #print(charA/3)
    numA=int(charA/3)
    numB=int(charB/1)
    numN=int(charN/2)
    print(numA, numB,numN)

    return(min(numA,numB,numN))


str2='QABAAAWOBL'
print(f'The given string is {str2} and number of BANANAs in it are {move1(str2)}')
str2='NAABXXAN'
print(f'The given string is {str2} and number of BANANAs in it are {move1(str2)}')
str2='NAANAAXNABABYNNBZ'
print(f'The given string is {str2} and number of BANANAs in it are {move1(str2)}')






str1 = "PYnative"
print(f'The reverse of the String {str1} is {str1[::-1]}')
str2=list(reversed(str1))  #['e', 'v', 'i', 't', 'a', 'n', 'Y', 'P']
print(str2)   #['e', 'v', 'i', 't', 'a', 'n', 'Y', 'P']

#print(''.join(str2))  #evitanYP
#print(''.join(reversed(str1))+'\n')  #evitanYP

str2 = ''.join(str2)
print(str2) #evitanYP

str3=[]
str3[:]=str2
#str3=str2.split(' ')
print(str3) #['e', 'v', 'i', 't', 'a', 'n', 'Y', 'P']

'''

str1='srinivas'
print(dict.fromkeys(str1))

str2={str1}
print(type(str2))
print(str2)




