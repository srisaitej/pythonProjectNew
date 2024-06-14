# use readlines() to split the file into a list of lines
'''
with open(file="Demo.txt", mode="r", encoding="utf-8") as file1:

    lines_list = file1.readlines()
    #print(f'{lines_list}')   #['1abc2\n', 'pqr3stu8vwx\n', 'a1b2c3d4e5f\n', 'treb7uchet']

list_strings = []
for line in lines_list:
    #print(line)
    str1 = ''
    for char in line:
        if char.isdigit():
            str1=str1+char
    list_strings.append(str1)

print(f'{lines_list=}  numbers in the line={list_strings}')
#lines_list=['1abc2\n', 'pqr3stu8vwx\n', 'a1b2c3d4e5f\n', 'treb7uchet']  numbers in the line=['12', '38', '12345', '7']
#print(list_strings)   #['12', '38', '12345', '7']

list_nums=[]
for str2 in list_strings:
    list_nums.append(int(str2[0]+str2[-1]))
#print(list_nums)     #[12, 38, 15, 77]

print(sum(list_nums))   #142

'''

'''
    list_strings = []
    for line in file1:
        #print(line)
        str1 = ''
        for char in line:
            if char.isdigit():
                str1=str1+char
        list_strings.append(str1)
        print(f'{line=}  numbers in the line={list_strings}')
    #print(list_strings)   #['12', '38', '12345', '7']

    list_nums=[]
    for str2 in list_strings:
        list_nums.append(int(str2[0]+str2[-1]))
    #print(list_nums)     #[12, 38, 15, 77]

    print(sum(list_nums))   #142

'''



"""
This is a solution to https://adventofcode.com/2023/day/1
"""
import re


def answer(data):
    def is_digit(char: str) -> bool:
        return bool(re.match('\d', char))

    def calibration_value(string: str) -> int:
        digits = [char for char in string if is_digit(char)]
        calibration_value = int(digits[0] + digits[-1])
        return calibration_value

    return sum([calibration_value(datum) for datum in data])


with open('Demo.txt') as test_data_file:
    print(answer(test_data_file.readlines()))






'''
str='srinivasp'
#str='s'
print(str[::])  #srinivas
print(str[1:5]) #rini
print(str[0])  #s   prints the first character of the string
print(str[-1]) #p   prints the last character of the string
'''
