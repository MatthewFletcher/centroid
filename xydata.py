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



#####################################################
#                     Imports						#
#####################################################
import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab


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




#####################################################
#                  Data Analysis					#
#####################################################

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
x_centroid=x_sum/x_len
y_centroid=y_sum/y_len


#Print for testing
#print("x_centroid= %f" %x_centroid)
#print("y_centroid= %f" %y_centroid)

# #I don't know why this needs to be done but don't delete this
# #The goal of this is to flip the state over. 
# for i in range(0,len(x)):
# 	if x[i]>x_centroid:
# 		x[i]=x[i]-x_centroid

# 	elif x[i]<x_centroid:
# 		x[i]=x_centroid-x[i]

# for j in range(0,len(y)):
# 	if y[j]>y_centroid:
# 		y[j]=y[j]-y_centroid

# 	elif y[j]<y_centroid:
# 		y[j]=y_centroid-y[j]



#####################################################
#                     Plotting    					#
#####################################################


#Plot all points in data
plt.plot(x,y, "-.")

#Plot centroid and label it
plt.plot(x_centroid,y_centroid,'^')


plt.ymax=max(x)
#Add axis labels
plt.xlabel("X")
plt.ylabel("Y")

#Show the plot
plt.show()






#Use this to convert image to xy points
#http://imagej.1557.x6.nabble.com/Obtaining-X-Y-coordinates-from-an-image-td3692369.html