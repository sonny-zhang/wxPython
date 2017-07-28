#coding=utf-8
'''
这是学习实验楼第2节的内容，画三角形

原文：https://www.shiyanlou.com/courses/427
==================================================================================
auther:风尘
QQ:758896823
QQ群：585499566
希望在Python的领域拥有“一番作为”的小伙伴们，可以加群和我本人，讨论项目实战中遇到的困惑
==================================================================================
'''
import wx
import math
'''
画三角形
1，在GUi显示三角形，该三角形基点（50,50），边长为60,80,100，并计算三角形的面积
'''
class Point(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __sub__(self,other):
		return Point(self.x-other.x, self.y-other.y)

	def __add__(self, other):
		return Point(self.x+other.x, self.y+other.y)

	@property
	def xy(self):
		return self.x, self.y

	def __str__(self):
		return "x={0},y={0}".format(self.x, self.y)

	def __repr__(self):
		return str(self.xy)

	@staticmethod
	def distance(a, b):
		return u"距离是：",math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)


from abc import abstractmethod,ABCMeta
class Polygon(object):
	'多边形基类使用抽象类'
	__metaclass__ = ABCMeta

	def __init__(self, points_list, **kwargs):
		for point in points_list:
			assert isinstance(point, Point), u"必须是输入Point的类型"
		self.points = points_list[:]
		self.points.append(points_list[0])   #需要一个终点，也就是起始点，构成图形
		self.color = kwargs.get('color','#000000')

	def drawPoints(self):

		'''
		return tuple(self.points)
		print tuple(self.points)
		'''
		points_xy = []
		print 1,self.points
		
		
		for point in self.points:
			points_xy.append(point.xy)
		print points_xy

		return tuple(points_xy)


	@abstractmethod
	def area(self):
		raise (u"没有完成...")

	def __lt__(self,other):
		assert isinstance(other,Polygon)
		return self.area < other.area



class Triangle(Polygon):

	def __init__(self, startPoint, len1, len2, **kwargs):
		Polygon.__init__(self, [startPoint, startPoint+Point(len1,0), startPoint+Point(len1,len2)], **kwargs)
		self._len1 = len1
		self._len2 = len2

	def area(self):
		return u"三角形的面积为：",(self._len1 * self._len2)/2


class Example(wx.Frame):
	def __init__(self, title, shapes):
		super(Example, self).__init__(None, title=title,
									  size=(600, 400))
		self.shapes = shapes

		self.Bind(wx.EVT_PAINT, self.OnPaint)

		self.Centre()
		self.Show()

	def OnPaint(self, e):
		dc = wx.PaintDC(self)

		for shape in self.shapes:
			dc.SetPen(wx.Pen(shape.color))
			dc.DrawLines(shape.drawPoints())


if __name__ == "__main__":

	prepare_draws = []

	p = Point(50,60)
	t = Triangle(p, 70, 80, color = "#ff0000")
	prepare_draws.append(t)

	app = wx.App()
	Example(u"三角形",prepare_draws)
	app.MainLoop()
