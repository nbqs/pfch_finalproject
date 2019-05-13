# import points from csv

import rhinoscriptsyntax as rs
import  re

# select a file to open
filename = rs.OpenFileName("Open CSV file", "*.csv", None, None, None)

# open file for reading
file = open(filename, 'r')

# read lines into a variable called lines
lines = file.readlines()

#close the file
file.close()

# delete the first line cause its a header
del lines[0]

#print(lines)

ptNumber = 0

for line in lines:
    #remove the \n and whitespace
    line = line.strip()
    #split the line by the comma
    ptinfo = line.split(",")
    #print(ptinfo)

#variable names of different CSV columns

    strawberry = int(ptinfo[0])
    orange = int(ptinfo[1])
    lemon = int(ptinfo[2])
    apple = int(ptinfo[3])
    grape = int(ptinfo[4])
    uncounted = int(ptinfo[5])


#create definitions to build shapes


    rs.EnableRedraw(False)

    def create_colored_pt (x, y, z, r, g, b):
        current_color = [r, g, b]
        pt = rs.AddPoint(x, y, z)
        # ptsforcurve = pt[]
        #     ptsforcurve.append(pt)
        # curve = rs.AddCurve(ptsforcurve)



    step = 10

    create_colored_pt(strawberry*50, 0, 0, 191, 43, 39)
    create_colored_pt(apple*50, 50, 0, 253, 143, 29)
    create_colored_pt(orange*50, 100, 0, 253, 243, 92)
    create_colored_pt(grape*50, 150, 0, 98, 255, 68)
    create_colored_pt(lemon*50, 200, 0, 94, 48, 86)

    rs.EnableRedraw()
