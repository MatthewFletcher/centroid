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



#Initialize area and x,y centroid to 0 for iteration. 
area = 0
c_x = 0
c_y = 0
#For loop using equation from wikipedia

#Area of polygon 
for i in range(len(x)-1):
	area_i = 0.5 * (x[i] * y[i+1]) - (x[i+1]*y[i])
	area = area + area_i


for i in range(len(x)-1):
	c_xi = (x[i]+x[i+1]) * (x[i]*y[i+1] - x[i+1]*y[i])
	c_x = c_x+c_xi

c_x = c_x/(6*area)

for i in range(len(y)-1):
	c_yi = (y[i]+y[i+1]) * (y[i]*x[i+1] - y[i+1]*x[i])
	c_y = c_y+c_yi
c_y = c_y/(6*area)


print ('Centroid is at %f, %f',c_x,c_y)

#####################################################
#                     Plotting    					#
#####################################################


#Plot all points in data
plt.xkcd()
plt.plot(x,y, "-.")

#Plot centroid and label it
plt.plot(c_x,c_y,'^')


plt.ymax=max(x)
#Add axis labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("russia")

#Show the plot
plt.show()






#Use this to convert image to xy points
#http://imagej.1557.x6.nabble.com/Obtaining-X-Y-coordinates-from-an-image-td3692369.html
