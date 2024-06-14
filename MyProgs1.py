

####Anagram
def anagram(s1,s2):
    a=sorted(s1.lower().strip().replace(' ',''))
    b=sorted(s2.lower().strip().replace(' ',''))
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


str1 = ' Astron omer '
str2 = 'Moon Starer'
#str1 = 'Java'
#str2 = 'Python'
if anagram(str1,str2):
    print(f'{str1} and {str2} are Anagram')
else:
    print(f'{str1} and {str2} are not Anagram')




#####Print the first non repeating character
def non_repeating_char(mystr1):
    counter={}
    mystr1=mystr1.lower()
    for char in mystr1:
        if char in counter:
            counter[char]+=1
        else:
            counter[char]=1

    print(f'{counter=}') #counter={'s': 3, 'k': 1, 'y': 1, 'g': 1, 'l': 1, 'a': 1}

    for char, char_count in counter.items():
        if char_count==1:
            return char


#mystr='SkyGlass'
mystr='GeeksQuizg'
print(f'First non-repeating character in \'{mystr}\' is {non_repeating_char(mystr)}')
#First non-repeating character in 'SkyGlass' is k

########
str1='GeeksQuizg'

#print(dict.fromkeys(str1))   #{'s': None, 'r': None, 'i': None, 'n': None, 'v': None, 'a': None}
str3=dict.fromkeys(str1.lower())
print(f'{type(str1)=}   ,   {type(str3)=}')  #type(str1)=<class 'str'>   ,   type(str3)=<class 'dict'>
print(f'{str3=}')  #str3={'g': None, 'e': None, 'k': None, 's': None, 'q': None, 'u': None, 'i': None, 'z': None}

print(f'{str3.keys()=}')  #str3.keys()=dict_keys(['g', 'e', 'k', 's', 'q', 'u', 'i', 'z'])

for char_keys in str3.keys():
    str3[char_keys]=str1.lower().count(char_keys)

for char_keys, char_values in str3.items():
    if char_values==1:
        print(f'{char_keys=}  {char_values}')
        break

    #if str3[char_keys]==1:
    #    print(f'{char_keys=}  {str3[char_keys]}')
    #    break




print(f'{str3=}')




str2=list({*str1})
print(type(str2))
print(str2)



#####
x=[1,2,1,3,4,1,2,4,1]
most=max(x,key=x.count)
print(most)

