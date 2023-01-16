https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com

class Rectangle:

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
    def setWidth(self, width):
        self._width = width
    def setHeight(self, height):
        self._height = height
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def area(self):
        return self._width*self._height
    def  perimeter(self):
        return 2*(self._width+self._height)
    def __str__(self):
        return "Width: " + str(self._width)+"\nHeight: "+str(self._height)
def main():
    w = 100
    h = 200
    r = Rectangle(w, h)
    print(r)
    a = r.area()
    print("{0:>,.2f}".format(a))
main()
        
