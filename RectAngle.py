#coding=utf-8
'''
这是学习实验楼第2节的内容，画矩形

原文：https://www.shiyanlou.com/courses/427
==================================================================================
auther:风尘
QQ:758896823
QQ群：585499566
希望在Python的领域拥有“一番作为”的小伙伴们，可以加群和我本人，讨论项目实战中遇到的困惑
==================================================================================
画方
1，class Point是基类点的封装；
2，线是由点组成的，构建基础类————点；
3，点的位置：绝对位置(x,y)；相对位置(B点相对于A点的位置，B.x-A.x,B.y-A.y，使用加减法计算相对位置)
4，返回基点的元组形式
5，计算两个点的距离，使用勾股定理
5，加入__str__,__repr__函数，方便调试
'''
import math
import wx

class Point(object):
    #点坐标x,y参数写入构造器中进行初始化
    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''
    1,点坐标相减的类方法，确定出另一点的相对位置
    2,使用相对方法，以一个基点确定出其他点的位置
    '''
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)
    '''
    1,点坐标相减的类方法，确定出另一点的相对位置
    2,使用相对方法，以一个基点确定出其他点的位置
    '''
    def __add__(self,other):
        return Point(self.x+other.x ,self.y+other.y)
    '''
    1,在调用wx.PaintDC.DrawLines函数时，需要点位置的元组形式，定义属性xy
    2,Python内置的@property装饰器就是负责把一个方法变成属性调用的
    '''
    @property
    def xy(self):
        return (self.x ,self.y)
    '''
    1,使用特殊方法__str__生成面向用户成可读性好的字符串，在对实例进行print时，会调用该方法，方便调试
    2,使用format内建函数，进行搭配print，将信息格式化
    3，format中的参数按顺序填入字符串中对应的“{}”中
    4,打印操作会首先尝试__str__和str内置函数
    
    '''
    def __str__(self):
        return "x={0},y={1}".format(self.x, self.y)
    '''
    1，程序员在开发期间则使用底层的__repr__来显示，实际上__str__只是覆盖了__repr__以得到更友好的用户显示
    '''
    def __repr__(self):
        return str(self.xy)


    '''
    使用静态函数dist定义两个点的距离；
    1,staticmethod是将外部函数集中到类中， 在不需要实例的情况下可以去调用
    2,如果你去掉staticmethod,在方法中加self也可以通过实例化访问方法也是可以集成代码
    '''
    @staticmethod
    def dist(a,b):
        return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

#----------------------------------------我是分割线----------------------------------------
'''
class Polygon是基类多边形的封装，使用抽象基类
1，线由点组成，使用points列表表示这些点
2，DrawLines的参数是元组，所以用drawPoints来返回需要的参数格式
3，area用来代表形状的面积，不同的形状有不同的算法，所以用抽象函数去实现;两个多边形的比较用面积来比较---抽象函数
4，不同的形状由不同的颜色来表示，所以用了属性color
'''

from abc import ABCMeta,abstractmethod
class Polygon(object):
    '''
    1，定义抽象基类Polygon，需要将元类__metaclass__设置为ABCMeta
    2，抽象类的实现离不开元类，在抽象类Polygon中，@abstractmethod和@abstractproperty装饰的方法/特性其子类必须实现
    3，抽象类不能直接实例化
    4，当从抽象类派生非抽象类时，这些非抽象类必须具体实现所继承的所有抽象成员，从而重写那些抽象成员
    '''
    __metaclass__ = ABCMeta

    def __init__(self,points_list,**kwargs):
        '''
        1,函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值
        2,*args,**kwargs两个都存在时，*args要写在**kwargs的前面
        3，assert 断言语句，其返回值为假，就会触发异常
        4,isinstance()布尔函数判定一个对象是否是另一个给定类(或给定类的子类)的实例
        '''
        for point in points_list:
            assert isinstance(point,Point), "input must be Point type"
        self.points = points_list[:]        #将所有点赋值给points
        self.points.append(points_list[0])  #需要一个终点，也就是起始点，构成图形
        self.color = kwargs.get('color','#000000')

    def drawPoints(self):
        points_xy = []
        for point in self.points:
            points_xy.append(point.xy)
        print points_xy
        return tuple(points_xy)

    @abstractmethod
    def area(self):
        raise("not implement") #raise 异常处理

    def __lt__(self,other):  #__lt__() 方法 小于
        assert isinstance(other,Polygon)
        return self.area < other.area

#----------------------------------------------我是分隔符-----------------------------------------------
'''
1，继承抽象类，抽象类的子类，进行矩形化
'''
class RectAngle(Polygon):

    def __init__(self,startPoint,w,h,**kwargs):
        Polygon.__init__(self,[startPoint,startPoint+Point(w,0),startPoint+Point(w,h),startPoint+Point(0,h)], **kwargs)
        self._w = w
        self._h = h
       
    def area(self):
        return self._w*self._h

class Example(wx.Frame):
    '''继承wx.Frame基类的__init__方法'''
    def __init__(self, title, shapes):
        #使用内建super()方法，调用wx.Fram基类的初始化方法
        super(Example, self).__init__(None, title=title,
            size=(500,300))

        self.shapes = shapes

        '''
        绑定渲染窗口的动作到OnPaint
        这样当resize窗口，会重新调用该函数
        '''
        self.Bind(wx.EVT_PAINT,self.OnPaint)

        self.Centre()
        self.Show()

    #画线
    def OnPaint(self, e):
        dc = wx.PaintDC(self)

        for shape in self.shapes:
            dc.SetPen(wx.Pen(shape.color))
            dc.DrawLines(shape.drawPoints())

if __name__== "__main__":

    prepare_draws = []
    start_p = Point(50,60)
    R=RectAngle(start_p,100,80,color = "#ff0000")
    prepare_draws.append(R)


    for shape in prepare_draws:
        print shape.area()

    app = wx.App()
    Example(u'需要好好复习，接下来是三角形，圆形...',prepare_draws)
    app.MainLoop()



