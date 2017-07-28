#coding=utf-8
'''
这是学习wxPython官方文档的第三篇代码，将Editor_1.py文件进行优化，添加菜单栏、状态栏

原文：https://wiki.wxpython.org/How%20to%20install%20wxPython
翻译：http://blog.csdn.net/g975291783/article/details/38351983
==================================================================================
auther:风尘
QQ:758896823
QQ群：585499566
希望在Python的领域拥有“一番作为”的小伙伴们，可以加群和我本人，讨论项目实战中遇到的困惑
==================================================================================
'''
import wx

class SmallEditor(wx.Frame):

    def __init__(self, parent, title):
        super(SmallEditor, self).__init__(parent, title=title, size=(600,400))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # 设置状态，调用CreateStatuBar()函数，在窗口的底部状态栏
        self.CreateStatusBar()

        #设置菜单，实例化
        filemenu = wx.Menu()

        '''
        wx.ID_ABOU和wx.ID_EXIT是wxWidgets的标准ID，有助于让wxWidgets在不同的平台上使每一个控件的ID都看起来更加自然
        Append是添加菜单按钮
        '''
        #设置“关于”菜单按钮 Append()参数含义：ID,项目名称，状态栏上显示的信息
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", u"这是个文本编辑器哈，希望你能坚持到把这个项目完成")
        #设置“退出”菜单按钮filemenu.AppendSeparator()   #分离filemenu项,【省略后不影响运行，不知道起的是什么作用？】
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", u"你准备要退出了哈") #ID,项目名称，状态栏信息

        #创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, title="File") #把"filemenu"里面的菜单项添加在菜单栏【File】里
        self.SetMenuBar(menuBar)  #到frame窗口中添加菜单栏

        #设置事件events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    #设置OnAboout处理办法
    def OnAbout(self, e):
        #创建一个带“OK”按钮的对话框(wx.MessageDialog)，wx.OK是wxWidgets提供的标准ID
        dlg = wx.MessageDialog(self, u"你真棒，已经会调用对话框了", u"关于编辑器", wx.OK) #参数内容:(self,内容,标题,ID)
        #展示出来对话框
        dlg.ShowModal()
        #完成事件后，关闭该对话框
        dlg.Destroy()

    #设置OnExit处理办法
    def OnExit(self, e):
        self.Close(True) #关闭frame窗口

if __name__ == "__main__":
    app = wx.App()
    frame = SmallEditor(None, title=u"这是第三个成功的代码：文本编辑器")
    app.MainLoop()

















