def changelist(l1):
    a[5]=20
    return

a=[1,2,3,4,5,6]
changelist(a)
print(a)  #[1, 2, 3, 4, 5, 20]

print(True+1)  #2
print(True and False) #False
print(True or False) #True
print(7+False) #7#

mydict={'name':'Srini','Job':'IT'}
print(mydict.items()) #dict_items([('name', 'Srini'), ('Job', 'IT')])
print(type(mydict.items())) #<class 'dict_items'>
print(len(mydict)) #2

mydict1={'name':'Srini','Job':'IT','name':'Srinivas'}
#dictionary should not have duplicate keys but will not throw an error
print(mydict1.items()) #dict_items([('name', 'Srinivas'), ('Job', 'IT')])
print(len(mydict1)) #2
