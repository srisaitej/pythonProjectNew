d1 = {"name":"uday",
      1:2,
      "val": True}
#Add an item to the dictionary
d1["month"]="jan"
marks = {"maths":50}
d1.update(marks)
d1.update({"x":"y"})
print(d1)
#Access the values
for i in d1:
    print(d1[i])
d2 = {"python":"oops","z":1}
#Concatinating the two dictionaries
d2.update(d1)
print(d2)
#removing an element from the dictionary
del d2['x']
print(d2)
#clearing the whole dictionary
d1.clear()
print("d1=",d1)
#changing one of the dic item maths to 75
d2['maths'] = 75
print(d2)
#length of the dictionary
print("d2 len =",len(d2))
#pop a particualr element for the given key
d2.pop(1)
print("d2 = ",d2)
#retrieve the value using GET function
print(d2.get('z'))
#print all the values form the dictionary using items
#Display the dictioanry as tuple pairs
print(d2.items())
#accessing keys from the dictionary
print(d2.keys())
#accessing values form the dictionary
print(d2.values())