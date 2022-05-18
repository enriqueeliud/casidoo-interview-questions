# Given two integer arrays of size n, return a new array of size n such that

# n consists of only unique elements and the sum of all its elements is maximum

# Example : 

# arr1 = [7, 4, 10, 0, 1]
# arr2 = [9, 7, 2, 3, 6]

# maximizedArray(arr1, arr2)
# [9, 7, 6, 4, 10]


def maximizedArray( arr1, arr2, n ):
 
 # create another array to store arr1 and arr2 elements
 arr3 = [0] * (2*n)

 k = 0

# add arr1, arr2 elements to arr3
 for i in range(n):

   arr3[k] = arr1[i]

   k += 1

 for i in range(n):

   arr3[k] = arr2[i]

   k += 1

# create a hash to store n largest unique elements
 hash = {}

 arr3 = sorted(arr3)

 arr3 = arr3[::-1]

#find and store n largest unique elements from arr3 and store in hash
 i = 0

 while (len(hash) != n):

   if(arr3[i] not in hash):

     hash[arr3[i]] = 1

   i += 1

 k = 0

# Get and store arr2 elements present in hash into arr3
 for i in range(n):

   if(arr2[i] in hash):

     arr3[k] = arr2[i]

     k += 1

     del hash[arr2[i]]

# Get and store arr1 elements present in hash into arr3
 for i in range(n):

   if(arr1[i] in hash):

     arr3[k] = arr1[i]

     k += 1

     del hash[arr1[i]]

#copy first n elements of arr3 to arr1
 for i in range(n):

   arr1[i] = arr3[i]

# print array elements
def printArray(arr, n):

  for i in arr:

    print(i, end = " ")

  print()

if __name__ == '__main__':
  
  arr1 = [7, 4, 10, 0, 1]

  arr2 = [9, 7, 2, 3, 6]

  size = len(arr1)

  maximizedArray(arr1, arr2, size)

  printArray(arr1,size)

