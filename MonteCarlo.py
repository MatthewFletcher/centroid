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
#            using a Monte Carlo simulation.                              #
#   "Bugs":  Points come out skewed and flipped                           #
#   "Undocumented features": None.                                        #
###########################################################################

#This program uses a Monte Carlo simulation to get an even number of points within the polygon

#####################################################
#                     Imports						#
#####################################################
import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import time


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


#Create list for x and y coordinates points that end up being inside the polygon 
inside_points_x_list = []
inside_points_y_list = []

#Set number of iterations for Monte Carlo simulation 
iteration_idx = 0

#The higher this number is, the greater the resolution of the image, but the longer the compute time will take
#Using an i7-6700HQ @ 3.5Ghz, I get around 600 iterations per second. 
total_iteration_number = 200000 

#Start time
start_time = time.clock()

#Monte Carlo simulation 
while iteration_idx < total_iteration_number:

	#Reset cross count equal to zero for each iteration 
	cross_count = 0

	#Select a random test point inside the bounding rectangle of the shape 
	x_t = random.uniform(min(x), max(x))
	y_t = random.uniform(min(y), max(y))
	



	#Check if test point is in between each successive set of points 
	for idx in range(0,len(x)-1):
		
		#Check if x coordinate of point is betweeen the 2 successive points. 
		
		#if this is true, add 1 to the cross count, and try another point 
		if y_t < y[idx]:
			#If x is between the two points from left to right
			if x_t>x[idx] and x_t<x[idx+1]:
				cross_count = cross_count + 1
			

			#If x is between the two points from right to left 
			if x_t<x[idx] and x_t>x[idx+1]:
				cross_count = cross_count + 1
				#print "success"



	#Check parity of number
	
	#Odd implies inside 
	if cross_count%2 == 1:
		inside_points_x_list.append(x_t)
		inside_points_y_list.append(y_t)

	#Go to next iteration
	iteration_idx = iteration_idx + 1


#Calculate centroid by averaging all points inside. 
#Calculate number of data points
x_len=len(inside_points_x_list)
y_len=len(inside_points_y_list)

#Set sum of points equal to x_sum and y_sum
x_sum=np.sum(inside_points_x_list)
y_sum=np.sum(inside_points_y_list)

#Calculate centroid of points
x_centroid = x_sum/x_len
y_centroid = y_sum/y_len



#Stop Time and print running time
running_time = time.clock() - start_time

#Print running time
print "Total Run Time = %.2f seconds."%running_time
#Print iterations per second
print "Program Frequency = %.2f iterations per second."%float(total_iteration_number / running_time)

print "Centroid X: %.2f"%x_centroid
print "Centroid Y: %.2f"%y_centroid



################################
#          Plot Points         #
################################

plt.plot()

plt.plot(inside_points_x_list,inside_points_y_list, ".")

#Plot centroid and label it
plt.plot(x_centroid,y_centroid,'*',markersize = 20)


#plt.ymax=max(x)
#Add axis labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Russia")

#Show the plot
plt.show()
