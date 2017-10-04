#    _     _      _     _      _     _      _     _      _     _      _     _
#   (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)
#    / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \
#  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__
# (_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)
#    || O ||      || O ||      || O ||      || O ||      || O ||      || O ||
#  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._
# (.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)
#  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'

###########################################################################
#   Author:  Matt Fletcher                                                #
#      PID:  None                                                         #
#    Class:  MAE273 Statics 	                                          #
#  Helpers:  None                                                         #
#                                                                         #
#  Program:  Centroid of Polygon Calculator                               #
# Due Date:                                                               #
#                                                                         #
# Language:  Python 2.7.6                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:   Given XY Coordinates for a shape, calculates the centroid    #
#                                                                         #
#   "Bugs":  Points come out skewed and flipped                           #
#   "Undocumented features": None.                                        #
###########################################################################

#The change in this from the previous program is using an equation for the centroid of an N-sided polygon
#Link is here https://en.wikipedia.org/wiki/Centroid#Centroid_of_a_polygon

#####################################################
#                     Imports						#
#####################################################
import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab
import math


#####################################################
#                       Setup			     		#
#####################################################

#Set empty list for coordinates
x,y =[],[]

#Importing csv data 
with open("russiadata.csv", "r") as russiadataFile:
	russiadataReader = csv.reader(russiadataFile)
	
	#Create list of points
	russiadatalist = []

	#Import data
	for row in russiadataReader:
		#While the rows have data, AKA length not equal to zero. 
		if len(row) != 0: 
			#Append data to arrays created above
			x.append(float(row[0]))
			y.append(float(row[1]))

#Close file as importing is done
russiadataFile.close


############################################


#Get approximate centroid for use in calculations 


#Convert list to array for computations
x=np.array(x)
y=np.array(y)


#Calculate number of data points
x_len=len(x)
y_len=len(y)

#Set sum of points equal to x_sum and y_sum
x_sum=np.sum(x)
y_sum=np.sum(y)

#Calculate centroid of points
x_centroid_approx=x_sum/x_len
y_centroid_approx=y_sum/y_len





#This method divides the shape into a bunch of triangles
#These triangles 1 vertex being the approximate centroid from above,
#and 2 points being in the scatter plot set 
#Calculates the centroid of each triangle


#Defining functions for triangle stuff

def distance(x1,y1,x2,y2):
	length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return length;


#Create empty lists for centroids of triangles, areas, and area products (see end of loop)
x_triangle_centroid_list = []
y_triangle_centroid_list = []
area_list				 = []
x_area_product_list 	 = []
y_area_product_list 	 = []


#Loop for each set of coordinates 
for index in range(len(x)-1):

	#Calculate centroid of triangle and append to list
	#This is the average of the x coordinates
	x_triangle_centroid_list.append((x_centroid_approx + x[index]+ x[index+1])*0.333)
	#Do the same thing for y (average of the y coordinates)
	y_triangle_centroid_list.append((y_centroid_approx + y[index]+ y[index+1])*0.333)

	#Area calculations using Heron's formula

	#Lengths of sides
	side1 = distance(x_centroid_approx,y_centroid_approx,x[index],y[index])
	side2 = distance(x_centroid_approx,y_centroid_approx,x[index+1],y[index+1])
	side3 = distance(x[index],y[index],x[index+1],y[index+1])
	
	#Calculation of semiperimeter
	sp = 0.5 * (side1 + side2 + side3)

	#Calculation of area 
	area = math.sqrt(sp * (sp-side1) * (sp - side2) * (sp - side3))

	area_list.append(area)

	#This value is the product of the area and the x coordinate of the centroid of that shape
	x_area_product_list.append(area * x_triangle_centroid_list[index])
	y_area_product_list.append(area * y_triangle_centroid_list[index])



#Then do some math to average the centroids.
# https://skyciv.com/tutorials/calculate-the-centroid-of-a-beam-section/

#Calculation of x centroid 
x_master = sum(x_area_product_list) / sum(area_list)
y_master = sum(y_area_product_list) / sum(area_list)

print "x --> ", x_master
print "y --> ", y_master




############################
#         Plotting         #
############################


#Plot all points in data

plt.xkcd()

plt.plot(x,y, ".-")

#Plot centroid and label it
plt.plot(x_master,y_master,'*')

plt.plot(x_centroid_approx,y_centroid_approx,'h')

#plt.ymax=max(x)
#Add axis labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Russia")

#Show the plot
plt.show()
