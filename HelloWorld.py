#coding=utf-8
'''
这是学习wxPython官方文档的第一篇代码，遵从Python的惯例，我们来第一个代码：HelloWorld.py

原文：https://wiki.wxpython.org/How%20to%20install%20wxPython
翻译：http://blog.csdn.net/g975291783/article/details/38351983
==================================================================================
auther:风尘
QQ:758896823
QQ群：585499566
希望在Python的领域拥有“一番作为”的小伙伴们，可以加群和我本人，讨论项目实战中遇到的困惑
==================================================================================
'''
#1, 导入wx模块包，这是必须的哦，没有导入包是无法调用的哈
import wx

#2，每一个wxPython应用程序都是wx.App这个类的一个实例，
app = wx.App()

#3，wx.Frame是一个顶层窗口；参数有(Parent, Id, Title)==>>(父窗口名，父窗口名的ID，子窗口的标签名)
frame = wx.Frame(None, id=wx.ID_ANY, title=u"这是第一个成功的代码：文本编辑器，Hello World !",
                 size=(600,400))#Parent没有，用[None]；id使用ID_ANY，这样wxWidgts灰分配一个ID号
'''
__init__(self, Window parent, int id=-1, String title=EmptyString, 
    Point pos=DefaultPosition, Size size=DefaultSize, 
    long style=DEFAULT_FRAME_STYLE, String name=FrameNameStr) -> Frame
    
参数1：parent
    当前窗口的父窗口，如果当前窗口是top-level window的话，则parent=None,如果不是顶层窗口，则它的值为所属frame的名字
参数2：id
    窗体编号。如果设置为-1，则系统自动给他分配一个编号。默认为-1.
参数3：title
    窗体的标题栏，即Caption。默认为空。
参数4：pos
    窗体的位置坐标。默认值为(-1,-1),则窗体的位置由系统决定。
参数5：size
    窗体的大小。默认值为(-1,-1),则窗体的大小由系统决定。
参数6：style
    窗体样式。默认值为 DEFAULT_FRAME_STYLE
    默认样式 DEFAULT_FRAME_STYLE 是下面这些值的复合：
        wx.MINIMIZE_BOX　|　wx.MAXIMIZE_BOX　|　wx.RESIZE_BORDER　|　
        wx.SYSTEM_MENU　|　wx.CAPTION　|　wx.CLOSE_BOX　|　wx.CLIP_CHILDREN
        它包括最小化按钮、最大化按钮、系统菜单、标题栏、关闭按钮、可变大小等等。您也可以根据自己的需求改变样式，具体请参照帮助。
参数7：name
  窗体名称。
  可以看到，7个参数中6个都有默认值，只有第一个参数 parent 需要设置一下，所以一个最简单的窗体就是：frame=wx.Frame(None)  


'''


#4，Show(True)函数，把窗口显示到屏幕上，就可以看见了哈;你将参数[True]改为[False],这样程序仍然在运行，但是不会在屏幕上显示
frame.Show(True)

#5，调用MainLoop()函数，来处理应用程序里的事件
app.MainLoop()













