import wx
from multiprocessing import Queue
from threading import Thread

class GUI1(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createMenuBar()
        self.panel1 = panel1(self)
        self.Show()
        
    def createMenuBar(self):
        self.CreateStatusBar()

        fileMenu = wx.Menu()
        fileMenu.Append(-1, 'Random file menu', 'Supporting text for random file menu item')
        fileMenu.Append(-1, 'Quit', 'Supporting text for quit menu item')
        
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)
        
class panel1(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
        self.frame = parent
        self.createButtons()
        self.scrollText()
        self.layout_()
        self.createListeningQueueThread()
        
    def createButtons(self):
        
        text1 = wx.StaticText(self, -1, label="Button 1:")
        text2 = wx.StaticText(self, -1, label="Button 2:")
        
        button1 = wx.Button(self, -1, label="Open window 1!")
        button2 = wx.Button(self, -1, label="Open window 2!")
        button1.Bind(wx.EVT_BUTTON, self.buttonEvent1)
        button2.Bind(wx.EVT_BUTTON, self.buttonEvent2)
        
        boxSizerV1 = wx.BoxSizer(wx.VERTICAL)
        boxSizerV1.Add(text1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 3)
        boxSizerV1.Add(button1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 3)
        
        boxSizerV2 = wx.BoxSizer(wx.VERTICAL)
        boxSizerV2.Add(text2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 3)
        boxSizerV2.Add(button2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 3)
        
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(boxSizerV1, 1)
        boxSizerH.Add(boxSizerV2, 1)
        
        self.buttonBoxSizer = boxSizerH
        
    def buttonEvent1(self, event):
        
        self.listenQueue.put("Hello! \n")
        GUI2 = secondaryGUI(self, title='Another window')
        GUI2.MakeModal(True)
        
    def buttonEvent2(self, event):
        
        self.listenQueue.put("World! \n")
        
    def scrollText(self):
        
        self.scrlTxt = wx.TextCtrl(self, -1, value="", size=wx.Size(300,100), style = wx.TE_MULTILINE|wx.TE_READONLY)
        
        scrlTxtBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        scrlTxtBoxSizer.Add(self.scrlTxt, 1, wx.EXPAND | wx.TOP | wx.ALL, 5)
        
        self.scrollTextBoxSizer = scrlTxtBoxSizer
            
    def createListeningQueueThread(self):
        
        self.listenQueue = Queue()
        self.thread1 = Thread(target=self.listening)
        self.thread1.setDaemon(True)
        self.thread1.start()
        
    def listening(self):
        
        while True:
            text = self.listenQueue.get()
            self.scrlTxt.write(text)
            

    def layout_(self):
        
        verticalBox = wx.BoxSizer(wx.VERTICAL)
        
        verticalBox.Add(self.buttonBoxSizer, 1, wx.EXPAND | wx.ALL)
        verticalBox.Add(self.scrollTextBoxSizer, 1, wx.EXPAND | wx.ALL)
        
        self.SetSizer(verticalBox)
        
class secondaryGUI(wx.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        
        wx.Frame.__init__(self, parent, *args, **kwargs)
        self.oldWindow = parent
        
        self.panel1 = wx.Panel(self)
        button1 = wx.Button(self.panel1, -1, label="Press!")
        button1.Bind(wx.EVT_BUTTON, self.buttonPress)
        
        self.Bind(wx.EVT_CLOSE, self.on_exit)
        self.Show()
        
    def buttonPress(self, event):
        
        self.oldWindow.listenQueue.put("Boom! \n")
        
    def on_exit(self, event):
        
        self.MakeModal(False)
        event.Skip()

if __name__ == '__main__':
    
    app = wx.App()
    GUI1Instance = GUI1(None, title='Main GUI window')
    app.MainLoop()
    
# Cpntinue with chapter 10!