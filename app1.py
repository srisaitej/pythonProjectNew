
'''
class Student:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
'''

var1 = "my name is uday"
var2 = [ ]
for x in var1.split() :
    print(x)
    var2.append(x[::-1])
print(var2)   #['ym', 'eman', 'si', 'yadu']

activities = ['Tennis','Swimming','Football','Keyboard']
print('The activities are',activities)  #The activities are ['Tennis', 'Swimming', 'Football', 'Keyboard']
activities[3] = 'Horse Riding'
print('The activities are',activities)   #The activities are ['Tennis', 'Swimming', 'Football', 'Horse Riding']

Animals = ['dog','cat','mouse']
cars = ['Audi','Skoda','Lexus']
print(Animals)  #['dog', 'cat', 'mouse']
print(cars)  #['Audi', 'Skoda', 'Lexus']
Everything=Animals+cars
print(Everything)  #['dog', 'cat', 'mouse', 'Audi', 'Skoda', 'Lexus']

#Animals.append(cars)
#print(Animals)   #['dog', 'cat', 'mouse', ['Audi', 'Skoda', 'Lexus']]

#All_animals=Animals[:2]+['parrot']+Animals[2:]
#print(f'{All_animals=}')
Animals.insert(2,'parrot')
print(f'{Animals=}')

Animals.append('monkey')
print(Animals)   #['dog', 'cat', 'mouse', 'monkey']

Animals.extend(cars)
print(Animals)   #['dog', 'cat', 'mouse', 'monkey', 'Audi', 'Skoda', 'Lexus']


str='SRIIVAS'
str1=str[:3]+'N'+str[3:]
print(f'{str=}  {str1=}')

