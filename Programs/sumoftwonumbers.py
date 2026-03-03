

# // [2,7,11,15]
# // target = 5


def sumOfTwoNumbers(nums, target):
    hashDic = {}
    print("hashDic ", hashDic)
    for i, value in enumerate(nums):
        canBePartner = target - value
        print("hash index ",i )
        print("hash value ",value )
        print("canBePartner: ",canBePartner)
        
        whatIsAtPosition = hashDic.get(value)
        
        print(" hashDic ",hashDic)
        print("whatIsAtPosition ", whatIsAtPosition)
        if(whatIsAtPosition != None):
            return [whatIsAtPosition, i]
        else:
            hashDic[canBePartner] = i
        print("*********")
    return hashDic

result = sumOfTwoNumbers([-3,4,3,90],0)
print("Result is: ",result)