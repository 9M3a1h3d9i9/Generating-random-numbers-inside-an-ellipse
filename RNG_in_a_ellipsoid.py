### In the name of god 
### Mohammad Mahdi Shafighy

## Solution 7 : 
# Generate n = 100, 1000, 10000 number of random 
# numbers which all lie inside an ellipse 
# with a uniform distribution.


n = int(input("Enter your n: {100, 1000, 10000} : "))

# Uniform Distribution Random Number Generation N~(0,1)
from random import seed
from random import random

# we have use seed 1, 2
seed(1)
lx=[]
for x in range(n):
    x = random()
    lx.append(x)
# print(lx)

ly=[]
seed(2)
for y in range(n):
    y = random()
    ly.append(y)
# print(ly)


# We have an ellipse with parameters a=0.5 and b=0.25
# We Know that the area's is S_e = Pi*a*b
# and we Know that the rectangle area's is 
#      S_r = Length(2a) * width(2b)  

a = 0.5
b = 0.25
# Pi Number 
Pi = 3.14159265

# Ellipsoid area
S_e = Pi*a*b
# Rectangle area
S_r = 2*a * 2*b

# We Know : 
# Ellipse Formula is (x^2/a^2) + (y^2/b^2) <= 1.
# s. t. 

from math import pow

# All Random Number Generation 
points=[]
# Ellipsoid RNG
e_p=[]
# rectangle RNG
r_p=[]
#
e_lx=[]
e_ly=[]
for i in range(n):
    points.append((pow(lx[i],2)/pow(a,2))+(pow(ly[i],2)/pow(b,2)))
    if points[i] <= 1 :
        e_lx.append(lx[i])
        e_ly.append(ly[i])

for j in points :
    if j > 1:
        r_p.append(j)
    else :
        e_p.append(j)

# print(" Ellipsoid Points : ", len(r_p), r_p)
# print("Rectangle - Ellipsoid Points : ", len(e_p), e_p)

import matplotlib.pyplot as plt 

# plotting points as a scatter plot 
plt.scatter(e_lx, e_ly, label= "stars", color= "blue", 
			marker= "*", s=25) 

plt.xlabel('x ') 
plt.ylabel('y ') 
plt.title('RNG belong to Ellipsoid .') 
plt.legend() 
plt.show() 