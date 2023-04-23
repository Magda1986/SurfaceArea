from math import *

list = [
    [10, 12],
    [10, 6],
    [13, 4],
    [13, 2],
    [3, 2],
    [3, 4],
    [6, 6],
    [6, 10],
    [8, 10],
    [8, 12],
]

x2=list[-1][0]          #define the last point X from list
y2=list[-1][1]          #define the last point Y from list
A=0.0                   #area field jump after the loop
surface_area=0          #surface area


for i in list:
    x=i[0]
    y=i[1]
    A=((x2+x)*(y-y2))
    x2=x
    y2=y
    surface_area += A
    
print(f"Asrea for a figure defined by 10 points {fabs(surface_area/2)}")    #fabs - depending on the direction in which the points in the XY coordinate system are read, the surface comes out positive (+) or negative (-). 
                                                                            #The absolute value is given in the final result
                                                                
# gaussian formula for any quadrilateral
# 2P=((X₂+X₁)*(Y2-Y₁))+((X3+X2)*(Y3-Y2))+((X4+X3)*(Y4-Y3))+((X₁+X4)*(Y₁-Y4)) 