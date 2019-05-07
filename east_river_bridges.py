# import points from csv

import rhinoscriptsyntax as rs
import re

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

    month = int(ptinfo[0])
    day_of_week = int(ptinfo[1])
    hightemp = float(ptinfo[3])
    lowtemp = float(ptinfo[4])
    precip = float(ptinfo[5])
    bk_bridge = int(ptinfo[6])
    man_bridge = int(ptinfo[7])
    willy_bridge = int(ptinfo[8])
    queen_bridge = int(ptinfo[9])
    total_bridge = int(ptinfo[10])

# to establish pts at ends of curve line

    startpoint = rs.AddPoint(0,0,0)
    endpoint = rs.AddPoint(746000,0,0)

# to scale day_of_week into point locations

    bridge_scaled = (man_bridge*100)
    bridge_mid = rs.AddPoint((day_of_week*80000), bridge_scaled, 0)

# here is where to change variable for different bridge outputs
    # bridge_scaled = ((bk_bridge/2)*100)
    #
    # if day_of_week =="Sunday":
    #     rs.AddPoint(40000, bridge_scaled, 0)
    # elif day_of_week =="Monday":
    #     rs.AddPoint(80000, bridge_scaled, 0)
    # elif day_of_week =="Tuesday":
    #     rs.AddPoint(120000, bridge_scaled, 0)
    # elif day_of_week =="Wednesday":
    #     rs.AddPoint(160000, bridge_scaled, 0)
    # elif day_of_week =="Thursday":
    #     rs.AddPoint(200000, bridge_scaled, 0)
    # elif day_of_week =="Friday":
    #     rs.AddPoint(240000, bridge_scaled, 0)
    # elif day_of_week =="Saturday":
    #     rs.AddPoint(280000, bridge_scaled, 0)
    # else:
    #     rs.AddPoint(400000, bridge_scaled, 0)

#to create curves between points, height of curve dependent on number ped

    bridge_curve_pts = (startpoint, bridge_mid, endpoint)
    bridge_curve = rs.AddInterpCurve(bridge_curve_pts)


    if hightemp < 10:
        rs.ObjectColor(bridge_curve, (0,0,255))
    elif hightemp > 10 and hightemp <20:
        rs.ObjectColor(bridge_curve, (0,128,255))
    elif hightemp > 20 and hightemp <30:
        rs.ObjectColor(bridge_curve, (0,0,255))
    elif hightemp > 40 and hightemp <50:
        rs.ObjectColor(bridge_curve, (0,255,128))
    elif hightemp > 50 and hightemp <60:
        rs.ObjectColor(bridge_curve, (0,255,0))
    elif hightemp > 60 and hightemp <70:
        rs.ObjectColor(bridge_curve, (128,255,0))
    elif hightemp > 70 and hightemp <80:
        rs.ObjectColor(bridge_curve, (255,255,0))
    elif hightemp > 80 and hightemp <90:
        rs.ObjectColor(bridge_curve, (255,128,0))
    elif hightemp > 90 and hightemp <100:
        rs.ObjectColor(bridge_curve, (255,0,0))
    else:
        rs.ObjectColor(bridge_curve, (0,0,0))
    # # r = int(ptinfo[3])
    # g = int(ptinfo[4])
    # b = int(ptinfo[5])

    # man_mid = rs.AddPoint(500, ((bkped/2)*-1), 0)
    # man_arc = rs.AddArc(bkpoint, man_mid, manpoint)

    # circle = rs.AddCircle(centerpt, Size)
    #
    # temp = int(ptinfo[0])
    # if boro == "M":
    #     rs.ObjectColor(circle, (0,0,255))
    # elif boro == "X":
    #     rs.ObjectColor(circle, (0,255,0))
    # elif boro == "B":
    #     rs.ObjectColor(circle, (255,0,0))
    # elif boro == "Q":
    #     rs.ObjectColor(circle, (125,125,125))
    # else:
    #     rs.ObjectColor(circle, (0,0,0))
    # # r = int(ptinfo[3])
    # # g = int(ptinfo[4])
    # # b = int(ptinfo[5])
    #
    #
    #
    # # color = (r,g,b)
    # # rs.ObjectColor(pt, color)
    # name = "pt_" + str(ptNumber)
    # rs.ObjectName(centerpt, name)
    # ptNumber += 1
