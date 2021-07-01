import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

img = cv2.imread("C:/Users/dell/Desktop/ML Robot Pattern formation/ML Project Group 10 - Artistic Pattern Formation Using Multi Robot System/Test Images and Data Used/fox.jpg");
#image resize
width = 500 #Y
height = 500 #X
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
final_image=resized
print("resized image size = ", final_image.shape)
#----------------------------------
image=img
# convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape)
#show the grayscale image

# perform the canny edge detector to detect image edges
edges = cv2.Canny(gray, threshold1=30, threshold2=100)
print("edges", edges)
plt.imshow(edges, cmap='gray')
plt.show()


indices = np.where(edges != [0])
print(type(indices))

coordinates = list(zip(indices[0], indices[1]))

print(type(coordinates))
print(coordinates)
#flattening a list of tuples into 1 list
#______________________________________
# Python code to convert list of tuple into list
import itertools
# List of tuple initialization
tuple = coordinates
# Using itertools
flat_coordinates = list(itertools.chain(*tuple))
# printing output
#-----------------------------------
# converting list of int to list of string
flat_coordinates = list(map(str, flat_coordinates))
print("type of flat coordinates=",type(flat_coordinates))
print(flat_coordinates)
#_______________________________________________________________

#writing all points data to a text file
points_file = open(r"C:/Users/dell/Desktop/ML Robot Pattern formation/ML Project Group 10 - Artistic Pattern Formation Using Multi Robot System/Code Files/allPoints.txt","w")
# w=Open the file for writing. For existing file, the data is truncated and over-written.
#The handle is positioned at the beginning of the file. Creates the file if the
# file does not exists.
i=0
while (i !=(len(flat_coordinates))):
    for element in flat_coordinates:
        points_file.write(element + " ")
        i = i + 1
        if ((i%2)==0):
            points_file.write("\n")
        else:
            continue
points_file.close()
#____________________________________________________
#creating a list of points
points=[]
# Read in the points from a text file
with open("C:/Users/dell/Desktop/ML Robot Pattern formation/ML Project Group 10 - Artistic Pattern Formation Using Multi Robot System/Code Files/allPoints.txt") as file:
    for line in file:
        x, y = line.split()
        points.append((int(x), int(y)))


print("Final points", type(points))
print(points)

#__________________________________________________



#reducing number of points obtained from canny edge detection
#--- this function reduces number of cannny edge points randomly ----
points = np.array(points)
def random_subset(points, n):
  return points[np.random.choice(points.shape[0], size= n, replace= False)]

# enter how many points you want to keep (this is not number of robots)
Number_of_Points=100#<---------------------------------------


new_points = random_subset(points, Number_of_Points)
print(new_points)

#---------------------------------------------------------
#flattening a list of tuples into 1 list
#____________________________________________________________________________________________
# Python code to convert list of tuple into list
# List of tuple initialization
new_tuple = new_points
# Using itertools
new_flat_coordinates = list(itertools.chain(*new_tuple))
# printing output
#-----------------------------------
# converting list of int to list of string
new_flat_coordinates = list(map(str, new_flat_coordinates))
print("type of new flat coordinates=",type(new_flat_coordinates))
print("new flat coordinates = ", new_flat_coordinates)

#----------------------------------------------------------
#writing new points data to new text file
new_points_file = open(r"C:/Users/dell/Desktop/ML Robot Pattern formation/ML Project Group 10 - Artistic Pattern Formation Using Multi Robot System/Code Files/fox.txt","w")
# w=Open the file for writing. For existing file, the data is truncated and over-written.
#The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
i=0
while (i !=(len(new_flat_coordinates))):
    for element in new_flat_coordinates:
        new_points_file.write(element + " ")
        i = i + 1
        if ((i%2)==0):
            new_points_file.write("\n")
        else:
            continue
new_points_file.close()

#---------------------------------------------
# showing new points
#creating a list of points
new_points=[]
# Read in the points from a text file
with open("C:/Users/dell/Desktop/ML Robot Pattern formation/ML Project Group 10 - Artistic Pattern Formation Using Multi Robot System/Code Files/fox.txt") as file:
    for line in file:
        x, y = line.split()
        new_points.append((int(x), int(y)))
print("new points = ", new_points)

#converts x y coordinates points into 1 point (pseudo pixel value)
def coordinates2image(l, shape):
  r = np.zeros(shape)
  r[l[:,0], l[:,1]] = 1
  return r

new_points_plot = coordinates2image(np.array(new_points), gray.shape)

plt.imshow(new_points_plot, cmap="gray")
plt.show()


