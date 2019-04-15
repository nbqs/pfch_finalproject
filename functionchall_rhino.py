import rhinoscriptsyntax as rs


class graphLine:

    def __init__(self, pt1, pt2):

        self.pt1 = pt1
        self.pt2 = pt2

    def makeLine(self):
        rs.AddLine(self.pt1,self.pt2)

fakedata1 = [0,0,0]
fakedata2 = [2,2,2]
fakedata3 = [2,0,0]
fakedata4 = [3,3,3]

line1 = graphLine((fakedata1), (fakedata2))
line1.makeLine()


line2 = graphLine((fakedata3), (fakedata4))
line2.makeLine()
