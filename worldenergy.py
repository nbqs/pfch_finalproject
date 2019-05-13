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

ptNumber = [0]

for line in lines:
    #remove the \n and whitespace
    line = line.strip()
    #split the line by the comma
    ptinfo = line.split(",")
    #print(ptinfo)

#variable names of different CSV columns

    keyid = int(ptinfo[0])
    total_supply = int(ptinfo[1])
    net_imports = int(ptinfo[2])
    production = int(ptinfo[3])
    percapita = int(ptinfo[4])
    xaxis = int(ptinfo[5])
    yaxis = int(ptinfo[6])
    country = str(ptinfo[7])
    yaxis_scaled = yaxis * -1000

#create definitions to build shapes


    rs.EnableRedraw(False)

    # def create_percapita_circle (x, y, z, r, g, b):
    #     current_color = [r, g, b]
    #     pt = rs.AddPoint(x, y, z)
    #     sphere = rs.AddCircle(pt,percapita)


    # def create_energy_shape (a, b, c, d, e, f, g, h, i):
    #     pt1 = rs.AddPoint(a, b, c)
    #     pt2 = rs.AddPoint(d, e, f)
    #     pt3 = rs.AddPoint(g, h, i)
    #     pt4 = rs.AddPoint(j, k, l)
    #     pts = [pt1, pt2, pt3]
    #     shape = rs.AddPolyline(pts)
    #     line = rs.AddLine(pt1,pt3)

#this is for the circle with the line that has slope to show total vs production
    # def create_energy_grid (a, b, c, d, e, f):
    #     pt1 = rs.AddPoint(a, b, c)
    #     pt2 = rs.AddPoint(d, e, f)
    #     line = rs.AddLine(pt1,pt2)
    #     circle = rs.AddCircle(pt1, percapita*10)

#this is to show circle with line for net_imports either positive or negative

    def create_energy_design (a, b, c, d, e, f):
        pt1 = rs.AddPoint(a, b, c)
        pt2 = rs.AddPoint(d, e, f)
        pt3 = rs.AddPoint(10000, yaxis_scaled, 0)
        line = rs.AddLine(pt1,pt2)
        #dash = rs.AddLine(pt1,pt3)
        #dashline = rs.AddHatch(dash,100,0)
        circle = rs.AddSphere(pt1, percapita*6)
        text = rs.AddText(country, pt3, 500, 'Avenir')

        if total_supply < 50:
            rs.ObjectColor(circle, (61, 194, 0))
        elif total_supply > 50 and total_supply <100:
            rs.ObjectColor(circle, (0, 193, 24))
        elif total_supply > 100 and total_supply <300:
            rs.ObjectColor(circle, (0, 193, 109))
        elif total_supply > 300 and total_supply <500:
            rs.ObjectColor(circle, (0, 192, 193))
        elif total_supply > 500 and total_supply <800:
            rs.ObjectColor(circle, (0, 107, 192))
        elif total_supply > 800 and total_supply <1300:
            rs.ObjectColor(circle, (0, 22, 192))
        elif total_supply > 1300 and total_supply <2000:
            rs.ObjectColor(circle, (62, 0, 192))
        elif total_supply > 2000 and total_supply <4000:
            rs.ObjectColor(circle, (146, 0, 191))
        elif total_supply > 4000 and total_supply <10000:
            rs.ObjectColor(circle, (191, 0, 152))
        elif total_supply > 10000 and total_supply <50000:
            rs.ObjectColor(circle, (191, 0, 68))
        elif total_supply > 50000:
            rs.ObjectColor(circle, (191, 15, 0))
        else:
            rs.ObjectColor(circle, (188, 171, 169))


    #AddText(text, point_or_plane, height=1.0, font='Arial', font_style=0, justification=None)

    # create_percapita_circle(200, yaxis*200, 0, 191, 43, 39)
    create_energy_design (0, yaxis_scaled, 0, net_imports, yaxis_scaled, 0)

    rs.EnableRedraw()
