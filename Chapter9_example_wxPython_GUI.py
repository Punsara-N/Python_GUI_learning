import wx
BACKGROUNDCOLOR = (240, 240, 240, 255)

class MainFrame(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createWidgets()
        self.Show()
        
    def exitGUI(self, event): # callback
        self.Destroy()
        
    def createWidgets(self):
        self.CreateStatusBar() # wxPython built-in method
        self.createMenu()
        self.createNotebook()
        
    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook) # Custom class explained below
        notebook.AddPage(widgets, "Widgets")
        notebook.SetBackgroundColour(BACKGROUNDCOLOR)
        # layout
        boxSizer = wx.BoxSizer()
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)
        
    def createMenu(self):
        self.menuBar = wx.MenuBar()
        
        self.fileMenu = wx.Menu()
        self.fileMenu.Append(0, '&Blah', 'Help note for blah...')
        
        self.menuBar.Append(self.fileMenu, '&File')
        self.SetMenuBar(self.menuBar)
        
        
class Widgets(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel = wx.Panel(self)
        self.createWidgetsFrame()
        self.createManageFilesFrame()
        self.addWidgets()
        self.addFileWidgets()
        self.layoutWidgets()
        
    def createWidgetsFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, "Widgets Frame", size=(285, -1) )
        self.statBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        
    def createManageFilesFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, "Manage Files", size=(285, -1) )
        self.statBoxSizerMgrV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        
    def layoutWidgets(self):
        boxSizerV = wx.BoxSizer( wx.VERTICAL )
        boxSizerV.Add( self.statBoxSizerV, 1, wx.ALL )
        boxSizerV.Add( self.statBoxSizerMgrV, 1, wx.ALL )
        self.panel.SetSizer( boxSizerV )
        boxSizerV.SetSizeHints( self.panel )
        
    def addWidgets(self):
        #self.addCheckBoxes()
        #self.addRadioButtons()
        self.addStaticBoxWithLabels()
        
    def addFileWidgets(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel, label='Browse to File...'))
        boxSizerH.Add(wx.TextCtrl(self.panel, size=(174, -1), value= "Z:\\" ))
        boxSizerH1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH1.Add(wx.Button(self.panel, label='Copy File To: '))
        boxSizerH1.Add(wx.TextCtrl(self.panel, size=(174, -1), value= "Z:\\Backup" ))
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(boxSizerH)
        boxSizerV.Add(boxSizerH1)
        self.statBoxSizerMgrV.Add( boxSizerV, 1, wx.ALL )
        
    def addStaticBoxWithLabels(self):
        
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        
        staticBox = wx.StaticBox( self.panel, -1, "Labels within a Frame" )
        staticBoxSizerV = wx.StaticBoxSizer( staticBox, wx.VERTICAL )
        
        boxSizerV = wx.BoxSizer( wx.VERTICAL )
        staticText1 = wx.StaticText( self.panel, -1, "Choose a number:" )
        boxSizerV.Add( staticText1, 0, wx.ALL)
        staticText2 = wx.StaticText( self.panel, -1,"Label 2")
        boxSizerV.Add( staticText2, 0, wx.ALL )
        
        staticBoxSizerV.Add( boxSizerV, 0, wx.ALL )
        boxSizerH.Add(staticBoxSizerV)
        
        textControl = wx.TextCtrl(self.panel)
        boxSizerH.Add(textControl)
        # Add local boxSizer to main frame
        self.statBoxSizerV.Add( boxSizerH, 1, wx.ALL )
        
#======================
# Start GUI
#======================
if __name__ == '__main__':
    app = wx.App()
    MainFrame(None, title="Python GUI using wxPython", size=(350,450))
    app.MainLoop()