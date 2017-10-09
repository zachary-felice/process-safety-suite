import wx

class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):

        super(MainFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)

        st = wx.StaticText(pnl, label="ProcessSafetySuite", pos=(25,25))
        font=st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Welcome to PSS")


    def makeMenuBar(self):

        fileMenu = wx.Menu()

        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                    "Help string shown in staus for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onHello, helloItem)
        self.Bind(wx.EVT_MENU, self.onExit, exitItem)
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)


    def onHello(self, event):
        wx.MessageBox("Hello from ProcessSafetySuite")

    def onExit(self, event):
        self.Close(True)

    def onAbout(self, event):
        wx.MessageBox("This is a template for PSS main frame.",
                        "About number 2",
                        wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='ProcessSafetySuite')
    frm.Show()
    app.MainLoop()
