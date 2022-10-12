# Program to add two matrices using nested loop
#first matrice
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
#second matrice
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
print("Result is")
for r in result:
   print(r)

#Adding two MAtrix using Numpy
import numpy as np

#First Matrix
X = np.array([12,7,3,4,5,6,7,8,9],ndmin=2).reshape(3,3)
#second matrice 
Y =np.array([5,8,1,6,7,3,4,5,9],ndmin=2).reshape(3,3)

#Sum 
result = X+Y

print(result)
