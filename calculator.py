#coding=utf-8
'''
这是学习实验楼第3节的内容，制作计算器

原文：https://www.shiyanlou.com/courses/427
==================================================================================
auther:风尘
QQ:758896823
QQ群：585499566
希望在Python的领域拥有“一番作为”的小伙伴们，可以加群和我本人，讨论项目实战中遇到的困惑
==================================================================================

按钮处理方法：http://www.yiibai.com/wxpython/wxpython_buttons.html

'''
import wx
import math


class calculator(wx.Frame):

    def __init__(self, title):
        super(calculator, self).__init__(None, title=title, size=(300,250))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        '''
        wx.BoxSizer:布局分级  wx.VERTICAL垂直  wx.HORIZONTAL水平
        wx.GridSizer:网格分级
        wx.TextCtrl:输入框
        wx.Button：按钮
        
        '''
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.textprint = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT|wx.TE_READONLY)
        vbox.Add(self.textprint, 1, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        self.equation = ""

        gridBox = wx.GridSizer(5, 4, 5, 5)
        labels = ['AC', 'DEL', 'pi', 'CLOSE', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3',
                  '-', '0', '.', '=', '+']
        for label in labels:
            buttonIterm = wx.Button(self, label=label)
            self.createHandler(buttonIterm, label)
            gridBox.Add(buttonIterm, 1, wx.EXPAND)
        vbox.Add(gridBox, 1, wx.EXPAND)
        self.SetSizer(vbox)


    def createHandler(self, button, labels):
        '''
        1,通过wx.EvtHandler类中的Bind方法可以绑定事件的类型、事件处理函数和事件对象。
        2,Bind的三个参数：事件类型、绑定事件的处理函数、绑定对象。
        3,事件：用户对界面的各种操作，列如鼠标的单击和移动。
        4,事件类型：同一个事件下的不同类型。
        
        '''
        item = "DEL AC = CLOSE"
        if labels not in item:
            self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
        elif labels == 'DEL':
            self.Bind(wx.EVT_BUTTON, self.OnDel, button)
        elif labels == 'AC':
            self.Bind(wx.EVT_BUTTON, self.OnAc, button)
        elif labels == '=':
            self.Bind(wx.EVT_BUTTON, self.OnTarget, button)
        elif labels == 'CLOSE':
            self.Bind(wx.EVT_BUTTON, self.OnExit, button)

    def OnAppend(self, event):
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)

    def OnDel(self, event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)

    def OnAc(self, event):
        self.textprint.Clear()
        self.equation = ""

    def OnTarget(self, event):
        string = self.equation
        try:
            target = eval(string)
            self.equation = str(target)
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self, u"格式错误，请输入正确的等式！",
                                   u"请注意", wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def OnExit(self, event):
        self.Close()





if __name__ == "__main__":
    app = wx.App()
    calculator(title=u"计算器")
    app.MainLoop()