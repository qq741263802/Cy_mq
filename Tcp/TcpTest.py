import wx

def Tcp():
    app = wx.App()
    window = wx.Frame(None, title="TCP协议测试", size=(900, 600))
    panel = wx.Panel(window)
    btn = wx.Button(panel, -1, "click Me")
    window.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    Tcp()