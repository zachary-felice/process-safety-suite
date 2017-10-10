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

        runMenu = wx.Menu()
        statsItem = runMenu.Append(-1, "&Stats\tCtrl-S",
                    "Run safety statistics frame")
        toxItem = runMenu.Append(-1, "&Toxicology",
                    "Run toxicology frame")
        dispItem = runMenu.Append(-1, "&Dispersion Model",
                    "Run dispersion modeling frame")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(runMenu, "&Run")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onHello, helloItem)
        self.Bind(wx.EVT_MENU, self.onExit, exitItem)
        self.Bind(wx.EVT_MENU, self.onStats, statsItem)
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)


    def onHello(self, event):
        wx.MessageBox("Hello from ProcessSafetySuite")

    def onExit(self, event):
        self.Close(True)

    def onStats(self, event):
        statsfrm = StatsFrame(None, title='Statistics Frame')
        statsfrm.Show()

    def onAbout(self, event):
        wx.MessageBox("This is a template for PSS main frame.",
                        "Help Pop-Up",
                        wx.OK|wx.ICON_INFORMATION)



class StatsFrame(wx.Frame):

    def __init__(self, *args, **kw):

        super(StatsFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)

        st = wx.StaticText(pnl, label="Statistics Panel", pos=(25,15))
        font=st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        font.PointSize += -10
        oshair = wx.StaticText(pnl, label="OSHA Incident Rate", pos=(25,50))
        oshair.SetFont(font)

        tcNumLostWorkdays = wx.TextCtrl(pnl, pos=(25,70))
        tcTotalHoursWorked = wx.TextCtrl(pnl, pos=(25,95))


        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Do some statistics")

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
        wx.MessageBox("Do some statistics here.")

    def onExit(self, event):
        self.Close(True)

    def onAbout(self, event):
        wx.MessageBox("This is a template for statistics frame.",
                        "Stats Help Pop-Up",
                        wx.OK|wx.ICON_INFORMATION)



if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='ProcessSafetySuite')
    frm.Show()
    app.MainLoop()
