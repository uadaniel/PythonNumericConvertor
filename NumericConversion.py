# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:07:01 2019

@author: Alexandru-Daniel
"""

def findTheNearestPowerOfTwo(number, lst):
    lst.reverse()
    for item in lst:
        if item <= number:
            break
    return item

def convertToHex(number):
    if number == 10:
        str(number)
        number='A'
    if number == 11:
        str(number)
        number='B'
    if number == 12:
        str(number)
        number='C'
    if number == 13:
        str(number)
        number='D'
    if number == 14:
        str(number)
        number='E'
    if number == 15:
        str(number)
        number='F'
    return number

while True:
    try:
        integerNumber=int(input("Please input your number: "))
        if integerNumber > 2**10 - 1 or integerNumber < 0:
            print("Your number cannot be represented on 10 bits. Please input a valid number.")
            continue
    except:
        print("Please provide an integer number")
        continue
    else:
        break
    
binary=""
hexadecimal=""
decimal=0

listOfPowerOf2 = list( 2**x for x in range(0,11) )
binaryList=[]
for i in range(0,11):
    binaryList.append(0)
    
startElement = findTheNearestPowerOfTwo( integerNumber, listOfPowerOf2 )
index=listOfPowerOf2.index(startElement)
binaryList[index] = 1
sum = startElement

while sum!=integerNumber:
    index=index+1
    if sum + listOfPowerOf2[index] <= integerNumber:
        sum = sum + listOfPowerOf2[index]
        binaryList[index]=1
        
for i in range(listOfPowerOf2.index(startElement), len(binaryList)):
    binary=binary+str(binaryList[i])
    
binaryReversed=binary[::-1]
for i in range(0,len(binaryReversed)):
    decimal=decimal+int(binaryReversed[i])*(2**int(i))

binaryList.reverse()
part_1=""
part_2=""
part_3=""
for i in range(0,len(binaryReversed)):
    if i < 4:
        part_1=part_1 + binaryReversed[i]
    elif i > 3 and i < 8:
        part_2=part_2 + binaryReversed[i]
    elif i >= 8:
        part_3=part_3 + binaryReversed[i]
part1Hex=0
part2Hex=0
part3Hex=0        
for i in range(0, len(part_1)):
    part1Hex=part1Hex+int(part_1[i])*(2**int(i))
for i in range(0, len(part_2)):
    part2Hex=part2Hex+int(part_2[i])*(2**int(i))
for i in range(0, len(part_3)):
    part3Hex=part3Hex+int(part_3[i])*(2**int(i))

part1Hex = convertToHex(part1Hex)
part2Hex = convertToHex(part2Hex)
part3Hex = convertToHex(part3Hex)

print("Decimal value = 0d"+str(decimal))
print("Binary value = 0b"+binary)
print("Hexadecimal value = 0h"+str(part3Hex)+str(part2Hex)+str(part1Hex))