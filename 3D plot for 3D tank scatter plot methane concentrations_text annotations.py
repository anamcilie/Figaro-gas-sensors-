# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:01:08 2022

@author: anamc
"""

'''
==============
3D scatterplot
https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html

https://pythonnumericalmethods.berkeley.edu/notebooks/chapter12.02-3D-Plotting.html

https://pythonprogramming.net/matplotlib-3d-scatterplot-tutorial/

https://pythonprogramming.net/3d-scatter-plot-customizing/?completed=/matplotlib-3d-scatterplot-tutorial/


https://likegeeks.com/3d-plotting-in-python/  (for details, subplots, polygon)

https://towardsdatascience.com/how-to-add-text-labels-to-scatterplot-in-matplotlib-seaborn-ec5df6afed7a

==============

Demonstration of a basic scatterplot in 3D.
'''

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure

from mpl_toolkits import mplot3d

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
import os
import csv


#def randrange(n, vmin, vmax):
    #'''
    #Helper function to make an array of random numbers having shape (n, )
    #with each number distributed Uniform(vmin, vmax).
   # '''
   # return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
ax = fig.add_subplot(111, projection='3d')

#geometry of the #d tank
ax.set_xlim(0,420)
ax.set_ylim(0,230)
ax.set_zlim(-50,0)


#plot a poligon (or the #30 sand layer in the 3D tank)

ax.text3D(0,	120,	-48,"#70 layer")

x1 = [0, 420, 400, 0]

y1 = [0, 0, 200, 200]

z1 = [-40, -40, -40, -40]

vertices = [list(zip(x1,y1,z1))]
poly = Poly3DCollection(vertices, alpha=0.1)
ax.add_collection3d(poly)
ax.text3D(0,	120,	-42,"#30 layer")


#plot a poligon (or #1st RF layer in the 3D tank)
x2 = [0, 420, 400, 0]

y2 = [0, 0, 200, 200]

z2 = [-35, -35, -35, -35]

vertices = [list(zip(x2,y2,z2))]
poly = Poly3DCollection(vertices, alpha=0.1)
ax.add_collection3d(poly)
ax.text3D(0,	120,	-36,"1st_RF layer")

#plot a poligon (or 2nd RF layer in the 3D tank)
x3 = [0, 420, 400, 0]

y3 = [0, 0, 200, 200]

z3 = [-30, -30, -30, -30]

vertices = [list(zip(x3,y3,z3))]
poly = Poly3DCollection(vertices, alpha=0.1)
ax.add_collection3d(poly)
ax.text3D(0,	120,	-31,"2nd_RF layer")


#plot a poligon (or 3rd RF layer in the 3D tank)
x4 = [0, 420, 400, 0]

y4 = [0, 0, 200, 200]

z4 = [-25, -25, -25, -25]

vertices = [list(zip(x4,y4,z4))]
poly = Poly3DCollection(vertices, alpha=0.1)
ax.add_collection3d(poly)
ax.text3D(0,	120,	-25,"3rd_RF layer")


#plot a poligon (or #12/20 sand layer in the 3D tank)
x5 = [0, 420, 400, 0]

y5 = [0, 0, 200, 200]

z5 = [-20, -20, -20, -20]

vertices = [list(zip(x5,y5,z5))]
poly = Poly3DCollection(vertices, alpha=0.1)
ax.add_collection3d(poly)
ax.text3D(0,	120,	-20,"#12/20 layer")

#plot a poligon (close the #12/20 sand layer in the 3D tank)
x5 = [0, 420, 400, 0]

y5 = [0, 0, 200, 200]

z5 = [-15, -15, -15, -15]

vertices = [list(zip(x5,y5,z5))]
poly = Poly3DCollection(vertices, alpha=0.1)
ax.add_collection3d(poly)



#color='m'


#plot a poligon (or silt soil layer in the 3D tank)
x6 = [220, 265, 265, 220]

y6 = [0, 0, 250, 250]

z6 = [-13, -13, -13, -13]

vertices = [list(zip(x6,y6,z6))]
poly = Poly3DCollection(vertices,color='k', alpha=0.2)
ax.add_collection3d(poly)
ax.text3D(230,	230,	-12,"Silt soil")

#plot a poligon (or #30/40 sand layer left side of the tank in the 3D tank)
x6 = [170, 220, 220, 170]

y6 = [0, 0, 250, 250]

z6 = [-13, -13, -13, -13]

vertices = [list(zip(x6,y6,z6))]
poly = Poly3DCollection(vertices, alpha=0.2)
ax.add_collection3d(poly)
ax.text3D(170,	230,	-13,"#30/40")

#plot a poligon (or #30/40 sand layer right side of the tank in the 3D tank)
x6 = [265, 335, 335, 265]

y6 = [0, 0, 250, 250]

z6 = [-13, -13, -13, -13]

vertices = [list(zip(x6,y6,z6))]
poly = Poly3DCollection(vertices, alpha=0.2)
ax.add_collection3d(poly)
ax.text3D(280,	230,	-13,"#30/40")


#plot a poligon (or the water reservoirs left side of the tank in the 3D tank)
x7 = [0, 0, 0, 0]

y7 = [0, 250, 250, 0]

z7 = [-50, -50, 0, 0]

vertices = [list(zip(x7,y7,z7))]
poly = Poly3DCollection(vertices, alpha=0.05)
ax.add_collection3d(poly)


#plot a poligon (or the water reservoirs right side of the tank in the 3D tank)
x7 = [420, 420, 420, 420]

y7 = [0, 250, 250, 0]

z7 = [-50, -50, 0, 0]

vertices = [list(zip(x7,y7,z7))]
poly = Poly3DCollection(vertices, alpha=0.05)
ax.add_collection3d(poly)



# plot the dots at the soil moisture locations 

x =[100,100,	200,	200,	200,	300	,300,	300,	100	,100,	200	,200,	200,	300	,300,	300	,100,	100	,200,	200,	200	,300,	300,	300	,70	,150,	150,	150,	250,	250,	250,	350	,350,	350]
y =[70,	150,	40,	110,	170,	40,	110,	170,	70,	150,	40,	110,	170,	40,	110	,170,	70,	150,	40,	110	,170,	40,	110,	170	,130,	40,	110,	170,	40,	110,	170,	40,	110,	170]
z =[-40,	-40,	-40,	-40,-40,	-40,	-40,	-40,-35,	-35,	-35,	-35,-35,	-35,	-35	,-35,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,	-25,-25,	-25]
s =['P27,	P03,	P24,	P26	,P21,	P22,	P06	,P31,	P01,	P02,	P11,	P12	,P13,	P28,	P07	,P14,	P15	,P29,	P05,	P30	,P33,	P18,	P17	,P16,	S10	,S09,	S08	,S07,	S06	,S05,	S04	,S03,	S02	,S01']


ax.scatter(x, y, z, c='k', marker='o')

# #30 sand layer soil moisture sensors
ax.text3D(100,	70,	-40	,"P27", c='k')
ax.text3D(100,	150,-40,"P03", c='k')
ax.text3D(200,	40,	-40,"P24", c='k')
ax.text3D(200,	110	,-40,"P26", c='k')
ax.text3D(200,	170	,-40,"P21", c='k')
ax.text3D(300,	40,	-40,"P22", c='k')
ax.text3D(300,	110	,-40,"P06", c='k')
ax.text3D(300,	170,-40,"P31", c='k')

# 1st RF layer soil moisture sensors
ax.text3D(100,	70,	-35,"P01", c='b')
ax.text3D(100,	150,-35,"P02", c='m')
ax.text3D(200,	40,-35,"P11", c='b')
ax.text3D(200,	110,-35,"P12", c='y')
ax.text3D(200,	170,-35,"P13", c='y')
ax.text3D(300,	40,	-35,"P28", c='m')
ax.text3D(300,	110,-35,"P07", c='m')
ax.text3D(300,	170,-35,"P14", c='y')

# 3rd RF layer soil moisture sensors
ax.text3D(100,	70,	-26	,"P15", c='m')
ax.text3D(100,	150,-25,"P29", c='b')
ax.text3D(200,	40,	-25,"P05", c='m')
ax.text3D(200,	110	,-25,"P30", c='c')
ax.text3D(200,	170	,-25,"P33", c='m')
ax.text3D(300,	40,	-25	,"P18", c='r')
ax.text3D(300,	110	,-25,"P17", c='c')
ax.text3D(300,	170,-25,"P16", c='y')
ax.text3D(70,	130	,-25,"S10", c='m')
ax.text3D(150,	40,	-25,"S09", c='m')
ax.text3D(150,	110,-25,"S08", c='c')
ax.text3D(150,	170,-25,"S07", c='m')
ax.text3D(250,	40,	-25	,"S06", c='c')
ax.text3D(250,	110,-25,"S05", c='c')
ax.text3D(250,	170,-25,"S04", c='m')
ax.text3D(350,	40,-25	,"S03", c='r')
ax.text3D(350,	110	,-25,"S02", c='m')
ax.text3D(350,	170,-25,"S01", c='m')


# legend
ax.text3D(500,	170,0,"Legend sand type", c='k')
ax.text3D(500,	170,-2,"#12/20 very coarse sand", c='b')
ax.text3D(500,	170,-4,"#20/30 coarse sand", c='c')
ax.text3D(500,	170,-6,"#30 medium sand", c='k')
ax.text3D(500,	170,-8,"#40/50 medium sand", c='m')
ax.text3D(500,	170,-10,"#70 fine sand", c='y')
ax.text3D(500,	170,-12,"#110 very fine sand", c='r')
ax.text3D(500,	170,-14,"+ = gas injection ports", c='r')
ax.text3D(500,	170,-16," o = soil moisture sensors", c='k')


# Add the gas injection pipes and define them
xp = [300, 300, 300, 200, 200, 200, 100, 100]
yp = [190, 130, 60, 190, 130, 60, 170, 90]
zp = [-37.5,-37.5,-37.5,-37.5,-37.5,-37.5,-37.5,-37.5]
ax.scatter3D(xp,yp,zp, c='r', marker="+", s=85)

ax.text3D(305,	190,	-37.5,"A", c='r')
ax.text3D(305,	130,	-37.5,"B", c='r')
ax.text3D(305,	60,	-37.5,"C", c='r')
ax.text3D(205,	190,	-37.5,"D", c='r')
ax.text3D(205,	130,	-37.5,"E", c='r')
ax.text3D(205,	60,	-37.5,"F", c='r')
ax.text3D(105,	170,	-37.5,"G", c='r')
ax.text3D(105,	90,	-37.5,"H", c='r')

# title 
#ax.set_title("3D tank")
ax.text3D(150,	170,5, "3D tank design", c='k')

ax.text3D(0,	0,0,"Top", c='k')
ax.text3D(0,	0,-50,"Bottom", c='k')

ax.text3D(0,	0,-2,"Upstream", c='k')
ax.text3D(420,	0,-2,"Downstream", c='k')

ax.set_xticks([0, 50,100,150,200,250, 300, 350, 400])
ax.set_yticks([0, 50,100,150,200])
ax.set_zticks([0, -5,-10,-15,-20, -25, -30, -35, -40, -45, -50])

#ax.legend(loc="best")

ax.set_xlabel('X_axis')
ax.set_ylabel('Y_axis')
ax.set_zlabel('Z_axis')


ax.grid(False)
#ax.grid(True)


plt.show()
 
 

#test_data = np.zeros(shape=(230,430,36))
#test_data[14,9,10] = 133.2
#test_data[20,19,10] = 158.4
#test_data[11,20,25] = 279.9
#test_data[13,28,25] = 90.3
#test_data[21,29,35] = 92.6
#print(test_data)



















