#LIST COMPREHENSION => A CONCISE WAY TO CRAETE LISTSIN PYTHON
#COMPACT AND EASIER TO READ THAN TRADITIONAL LOOPS
# name = [expression for value in range()]

import math

doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#HERE IS THE EASIER WAY
tripples = [ x*3 for x in range(1,11)]
print(tripples)

squares = [pow(x,2) for x in range(1,11)]
print(squares)

fruits = ["BANANA", "APPLE","COCO","ORANGE"]
fruits =[x.lower() for x in fruits]
print(fruits) #['banana', 'apple', 'coco', 'orange']

nums = [1, -2, -3 ,-4, 5, -6]
#positive_nums = [num for num in nums if num>=0]
#print(positive_nums)
negative_nums =[num for num in nums if num<0]
print(negative_nums)




