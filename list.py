#list
fruits=["apple","banana","orange","chiku"]
print(fruits)
print(fruits[2])

#list of number
number = [1,2,3,4,5,6,7,8,9]
print(number)
print(number[-2])
number[5] =8   #updated values from old
print(number)
print(number + fruits) #combination of two list
print(number*3) #number list multiply 3 times
print(fruits*3) # same as number

#empty list
abc = []
print(abc)

#in operation in list
print("apple" in fruits) # return true value if value present in fruits list
print("papaya" in fruits)

# append function in list
# fruits=["apple","banana","orange","chiku"]
fruits.append("watermelon") # watermelon added in fruits list
print(fruits)

#lenth function in python
#fruits = ['apple', 'banana', 'orange', 'chiku', 'watermelon']
print(len(fruits))

#insert function in list
#number = [1,2,3,4,5,6,7,8,9]
number.insert(-1,99)
print(number)

#index function in list
#number = [1,2,3,4,5,6,7,8,9]
print(number.index(9))