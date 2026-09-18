# test.py
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

#利用向量叉乘计算多边形面积
def GetArea(points):
    area=0
    for i in range(0,len(points)-1):
        p1=points[i]
        p2=points[i+1]
        trArea=(p1.x*p2.y-p2.x*p1.y)/2
        area+=trArea
    return abs(area)

def SetPoints(x,y):
    points=[]
    for index in range(len(x)):
        points.append(Point(x[index],y[index]))
    return points

def main():
    x=[3,9,12,5,3]
    y=[4,5,8,11,4]

    points = SetPoints(x,y)
    area=GetArea(points)
    print('多边形面积为：')
    print(area)

if __name__=="__main__":
    main()
