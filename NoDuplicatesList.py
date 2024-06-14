old=['S','r','i','n','i','v','a','s']
old=[char.lower() for char in old]  #['s', 'r', 'i', 'n', 'i', 'v', 'a', 's']


'''
new=[]
for char in old:
    if char not in new:
        new.append(char)
print(f'Old list : {old}\nNew list : {new}')
#Old list : ['s', 'r', 'i', 'n', 'i', 'v', 'a', 's']
#New list : ['s', 'r', 'i', 'n', 'v', 'a']
'''

'''
new=list(set(old)) #The order is not maintained as Sets do not maintain order
print(f'Old list : {old}\nNew list : {new}') 
#Old list : ['s', 'r', 'i', 'n', 'i', 'v', 'a', 's']
#New list : ['i', 'a', 's', 'v', 'n', 'r']
'''

new=list(dict.fromkeys(old).keys())
#dict.fromkeys(old)   #{'s': None, 'r': None, 'i': None, 'n': None, 'v': None, 'a': None}
#dict.fromkeys(old).keys()   #dict_keys(['s', 'r', 'i', 'n', 'v', 'a'])
#list(dict.fromkeys(old).keys())   #['s', 'r', 'i', 'n', 'v', 'a']
print(f'Old list : {old}\nNew list : {new}')
#Old list : ['s', 'r', 'i', 'n', 'i', 'v', 'a', 's']
#New list : ['s', 'r', 'i', 'n', 'v', 'a']
