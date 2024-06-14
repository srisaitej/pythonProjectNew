d1={'Name': 'Srini','Job': 'Programming','Age': None,'OS': 'Windows'}

#s_d1=sorted(d1) #['Age', 'Job', 'Name', 'OS'] , returns a list of sorted keys
#print(type(s_d1)) #<class 'list'>

'''
s_d1=sorted(d1.items()) #returns a sorted list of tuples( sorted by key and not value)
# with each tuple representing a key-value pair of the dictionary.
#[('Age', None), ('Job', 'Programming'), ('Name', 'Srini'), ('OS', 'Windows')]
'''

'''
##### Using dictionary constructor dict() #####
s_d2=dict(s_d1) #covert list of tuples to dictionary using dictionary constructor dict()
#{'Age': None, 'Job': 'Programming', 'Name': 'Srini', 'OS': 'Windows'}
print(f'Actual Dictionary : {d1}, Sorted Dictionary : {s_d2}')
#Actual Dictionary : {'Name': 'Srini', 'Job': 'Programming', 'Age': None, 'OS': 'Windows'}, 
# Sorted Dictionary : {'Age': None, 'Job': 'Programming', 'Name': 'Srini', 'OS': 'Windows'}
'''

'''
##### Using for loop #####
s_d2={}
for key,value in s_d1:
    s_d2[key]=value

print(f'Actual Dictionary : {d1}, Sorted Dictionary : {s_d2}')
#Actual Dictionary : {'Name': 'Srini', 'Job': 'Programming', 'Age': None, 'OS': 'Windows'},
# Sorted Dictionary : {'Age': None, 'Job': 'Programming', 'Name': 'Srini', 'OS': 'Windows'}
'''

'''
##### Using dictionary comprehension #####
s_d2 = {key: value for key, value in s_d1}

print(f'Actual Dictionary : {d1}, Sorted Dictionary : {s_d2}')
#Actual Dictionary : {'Name': 'Srini', 'Job': 'Programming', 'Age': None, 'OS': 'Windows'}, 
# Sorted Dictionary : {'Age': None, 'Job': 'Programming', 'Name': 'Srini', 'OS': 'Windows'}
'''

d2={'Name': 'Srini','Job': 'Programming','Age': 'forty five' ,'OS': 'Windows'}


##### Sort a dictionary based on Value  with normal function for a key arguement in sorted()  #####
def value_getter(item):
    return item[1]


s_d1=sorted(d2.items(), key=value_getter)  #sorted based on keys in the dictionary and returns a
                                           # list of tuples with key, value pairs
s_d2=dict(s_d1)
print(f'Actual Dictionary : {d2}, Sorted Dictionary : {s_d2}')
#Actual Dictionary : {'Name': 'Srini', 'Job': 'Programming', 'Age': 'forty five', 'OS': 'Windows'},
# Sorted Dictionary : {'Job': 'Programming', 'Name': 'Srini', 'OS': 'Windows', 'Age': 'forty five'}



'''
##### Sort a dictionary based on Value  with lambda function for a key arguement in sorted()  #####
s_d1=sorted(d2.items(), key=lambda item: item[1])
s_d2=dict(s_d1)
print(f'Actual Dictionary : {d2}, Sorted Dictionary : {s_d2}')
#Actual Dictionary : {'Name': 'Srini', 'Job': 'Programming', 'Age': 'forty five', 'OS': 'Windows'}, 
# Sorted Dictionary : {'Job': 'Programming', 'Name': 'Srini', 'OS': 'Windows', 'Age': 'forty five'}
'''


print(reversed([3, 2, 1])) #<list_reverseiterator object at 0x000001DA7C16BBE0>
print(list(reversed([3,2,1]))) #[1, 2, 3]
#print(help(reversed))  #Return a reverse iterator over the values of the given sequence.