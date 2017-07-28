#coding=utf-8
'''
这是学习wxPython官方文档的第二篇代码，构建一个简单的文本编辑器Editor.py，添加多行输入框

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
    '派生wx.Frame的类，并重写__init__方法'
    def __init__(self, parent, title):
        #1，super()，调用父类的方法，和[wx.Frame.__init__(self,...)]方法是一样的
        super(SmallEditor, self).__init__(parent, title=title, size=(600,400))
        #2，wx.TextCtrl()方法为输入框，参数wx.TE_MULTILINE允许在文本框中输入多行文本
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    smalled = SmallEditor(None, u"这是第二个成功的代码：文本编辑器")
    app.MainLoop()



