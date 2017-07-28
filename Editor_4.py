#coding=utf-8
'''
这是学习wxPython官方文档的第四篇代码，将Editor_2.py文件进行优化，添加打开文件菜单项

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
import os

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

        #设置“打开”菜单按钮 Append()参数含义：ID,项目名称，状态栏上显示的信息
        menuopen = filemenu.Append(wx.ID_OPEN, u"打开", u"你即将打开一个文件哈")
        #设置“关于”菜单按钮 Append()参数含义：ID,项目名称，状态栏上显示的信息
        menuAbout = filemenu.Append(wx.ID_ABOUT, u"关于", u"这是个文本编辑器哈，希望你能坚持到把这个项目完成")
        #分离前两个按钮
        filemenu.AppendSeparator()
        # 设置“退出”菜单按钮
        menuExit = filemenu.Append(wx.ID_EXIT, u"退出", u"你准备要退出了哈") #ID,项目名称，状态栏信息


        #创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, title=u"文件") #把"filemenu"里面的菜单项添加在菜单栏【File】里
        self.SetMenuBar(menuBar)  #到frame窗口中添加菜单栏

        #设置事件events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.onOpen, menuopen)

        #设置sizer
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)    #wx.BoxSizer基于水平或处置布局，wx.HORIZONTAL水平布局 wx.VERTICAL垂直布局
        self.buttons = []   #创建按钮对象
        for i in range(6):  #设置6个按钮
            self.buttons.append(wx.Button(self, -1, u"按钮" + str(i)))    #wx.Button:Create and show a button
            '''
            把按钮对象buttons添加到sizer2的布局中
            sizer.Add()参数：fist：把1个控件添加到sizer里面.
            second：权重因子，控件在所在控件的空间比例(0:控件在父sizer，不会随着frame改变；1：).
            third：参数flag wx.GROW /wx.EXPAND, 控件可以调整自己的尺寸以适应 frame 尺寸的变化; 
            wx.SHAPED:控件的尺寸虽然可以变化，但是形状会保持不变
            '''
            self.sizer2.Add(self.buttons[i], 1, wx.SHAPED)

        #将子sizer添加到父sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.GROW)

        #激活sizer
        self.SetSizer(self.sizer)    #告诉window(Frame)使用哪个sizer
        self.SetAutoLayout(True)    #告诉window使用sizer阿里布局
        self.sizer.Fit(self)        #告诉 sizer 计算它所容纳的元素的初始化尺寸和位置

        self.Show(True)

    #设置OnAboout处理办法
    def OnAbout(self, e):
        #创建一个带“OK”按钮的对话框(wx.MessageDialog)，wx.OK是wxWidgets提供的标准ID
        dlg = wx.MessageDialog(self, u"你真棒，已经会调用对话框了", u"关于编辑器", wx.OK) #参数内容:(self,内容,标题,ID)
        #展示出来对话框
        dlg.ShowModal()
        #完成事件后，关闭该对话框，释放资源
        dlg.Destroy()

    #设置OnExit处理办法
    def OnExit(self, e):
        self.Close(True) #关闭frame窗口


    """  FileDialog
     __init__(self, Window parent, String message=FileSelectorPromptStr, 
            String defaultDir=EmptyString, String defaultFile=EmptyString, 
            String wildcard=FileSelectorDefaultWildcardStr, 
            long style=FD_DEFAULT_STYLE, 
            Point pos=DefaultPosition, Size size=DefaultSize) -> FileDialog
    Constructor(构造器).  Use ShowModal method to show the dialog.
    """
    def onOpen(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, u"请选择一个文件", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()   #文件名
            self.dirname = dlg.GetDirectory()   #文件夹名
            f = open(os.path.join(self.dirname, self.filename), 'r+')   #打开文件
            self.control.SetValue(f.read())     #读取文件内容
            f.close()   #关闭文件
        dlg.Destroy()   #关闭该对话框，释放资源

if __name__ == "__main__":
    app = wx.App()
    frame = SmallEditor(None, title=u"这是第四个成功的代码：文本编辑器")
    app.MainLoop()

















