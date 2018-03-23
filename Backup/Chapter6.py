#IMPORTING
try:
    # for Python2
    import Tkinter as tk
    import ttk # Themed tkinter
    import ScrolledText
    import tkMessageBox
    from tooltip import createToolTip
    from threading import Thread
    from time import sleep
    from Queue import Queue
    import queues
    import tkFileDialog
    from os import path
    from os import makedirs
except ImportError as err:
    print(err)
    # for Python3
    import tkinter as tk
    from tkinter import ttk
    import tkinter.scrolledtext as ScrolledText
    from tkinter import tkMessageBox
    from tooltip import createToolTip
    from threading import Thread
    from time import sleep
    from queue import Queue
    from tkinter import filedialog
    from os import path
    from os import makedirs
    
# Module level GLOBALS
GLOBAL_CONST = 42
fDir = path.dirname(__file__)
netDir = fDir + '/Backup'
if not path.exists(netDir):
    try:
        makedirs(netDir) # Makes directory if it does not exist
    except OSError:
        if not path.isdir(netDir):
            raise
    
class OOP():
    
    def __init__(self):

        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.win.resizable(0, 0) #Disable resizing the GUI
        self.win.iconbitmap(r'images\Captain-America.ico')
        self.guiQueue = Queue()
        
        self.main()
        self.defaultFileEntries()
        
    # BUTTON METHOD
    def clickMe(self):
        #self.action2.configure(text='Hello ' + self.name.get() + ' ' + self.number.get())
        #self.action2.configure(state='disabled') # Disable the Button Widget
        #self.createThread()
    
        # Passing in the current class instance to queue module
        print(self)
        queues.writeToScrollText(self)
        
    # RADIO BUTTONS METHOD
    def radioButtonCall(self): # Radio button callback
        radioValue = self.radio.get()
        if radioValue == 1:
            self.monty2.configure(text=self.colour[0])
        elif radioValue == 2:
            self.monty2.configure(text=self.colour[1])
        elif radioValue == 3:
            self.monty2.configure(text=self.colour[2])
     
    # SPINBOX METHOD       
    def _spinBox(self): # A function for the spinbox
            value = self.spin.get()
            print(value)
            self.scrText.insert(tk.INSERT, value + '\n') # Prints it into the scroll text
            self.scrText.yview_pickplace('end') # Auto scroll down
            
    # METHODS FOR MENU BAR
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() # This exits python!
        
    def _aboutMsgBox(self):
        tkMessageBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2018.')
            
    def _warning(self):
        tkMessageBox.showwarning('WARNING!', 'This is a test warning!')
        
    def _error(self):
        tkMessageBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
           
    def _customMessage(self,msg):
        tkMessageBox.showinfo("Hello!", "Hello " + msg)
           
    def _question(self):
        answer = tkMessageBox.askyesno('Test question', 'Are you a male?')
        if answer == True:
            msg="Sir!"
        else:
            msg="Madam!"
        self._customMessage(msg)
        
    # A METHOD THAT WILL BE CREATED IN A NEW THREAD
    def createThread(self):
        self.runT = Thread(target=self.methodInAThread, args=[int(self.number.get())])
        self.runT.setDaemon(True)
        self.runT.start()
        print(self.runT)
        print("createThread():", self.runT.is_alive())
        
        self.writeT = Thread(target=self.useQueues)
        self.writeT.setDaemon(True)
        self.writeT.start()
        
    def methodInAThread(self, numOfLoops=10):
        for i in range(numOfLoops):
            sleep(1)
            self.scrText.insert(tk.INSERT, str(i) + '\n')
            print(str(i))
            self.scrText.yview_pickplace('end') # Auto scroll down
        sleep(1)
        print("methodInAThread():", self.runT.isAlive())
        
    # MAKING QUEUE FOR THREADS
    def useQueues(self):
        #self.guiQueue = Queue() # Create queue instance
        #print(self.guiQueue)
        #for i in range(10):
        #    self.guiQueue.put('Message from a queue ' + str(i))
        while True:
            print(self.guiQueue.get())
            
    def defaultFileEntries(self):
        self.nameEntered.delete(0, tk.END)
        self.nameEntered.insert(0, '< default name >')
        
        self.fileEntry.delete(0, tk.END)
        self.fileEntry.insert(0, fDir)
        if len(fDir) > self.entryLen:
            self.fileEntry.config(width=len(fDir) + 3)
        self.fileEntry.config(state='readonly')
            
        self.netwEntry.delete(0, tk.END)
        self.netwEntry.insert(0, netDir)
        if len(netDir) > self.entryLen:
            self.netwEntry.config(width=len(netDir) + 3)
            
        
    def main(self):
    
        # CREATING TABS
        self.tabControl = ttk.Notebook(self.win) # Create tab control (list)
        self.tabControl.pack(expand=1, fill="both") # Makes tab visible
        
        self.tab1 = ttk.Frame(self.tabControl) # Create a tab
        self.tabControl.add(self.tab1, text="Tab 1") # Adds the tab
        
        self.tab2 = ttk.Frame(self.tabControl) # A new tab
        self.tabControl.add(self.tab2, text="Tab 2") # Adds the tab
        
        # CREATING A CONTAINER FRAME IN THE WINDOW TO HOLD ALL WIDGETS
        self.monty = ttk.LabelFrame(self.tab1, text=" Monty Python ")
        self.monty.grid(column=0, row=0, padx=5, pady=5)
        
        # FIRST AND SECOND ROWS (LABELS AND ENTRY BOXES)
        ttk.Label(self.monty, text="Enter a name:").grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.monty, width=24, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1, sticky='WE')
        self.action2 = ttk.Button(self.monty, text="Click me!", command=self.clickMe)
        self.action2.grid(column=2, row=1)
        
        # COMBOBOX
        self.aLabel2 = ttk.Label(self.monty, text="Choose a number:").grid(column=1, row=0)
        self.number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.monty, width=14, textvariable=self.number, state='readonly') # ...state='readonly')  does not allow the user to enter his/her own value into combo box
        self.numberChosen['values'] = (1, 2, 4, 42, 100)
        self.numberChosen.grid(column=1, row=1)
        self.numberChosen.current(0)
        
        # NEW LABEL FRAME FOR TAB 2
        self.monty2 = ttk.LabelFrame(self.tab2, text=" The Snake ")
        self.monty2.grid(column=0, row=0, padx=20, pady=20)
        
        # CHECKBOXES
        self.check1 = tk.IntVar()
        self.checkBox1 = tk.Checkbutton(self.monty2, text="Disabled", variable=self.check1, state='disabled')
        self.checkBox1.select()
        self.checkBox1.grid(column=0, row=0, sticky=tk.W) # sticky=tk.W ... alligns west of grid 
        self.check2 = tk.IntVar()
        self.checkBox2 = tk.Checkbutton(self.monty2, text="Unchecked", variable=self.check2)
        self.checkBox2.deselect()
        self.checkBox2.grid(column=1, row=0, sticky=tk.W)
        self.check3 = tk.IntVar()
        self.checkBox3 = tk.Checkbutton(self.monty2, text="Enabled", variable=self.check3)
        self.checkBox3.select()
        self.checkBox3.grid(column=2, row=0, sticky=tk.W)
        createToolTip(self.checkBox3, text="This is a checkbox")
        

                
        self.colour = ('Blue', 'Gold', 'Red')
        self.radio = tk.IntVar()
        self.radio.set(99)
        for col in range(3):
            self.radioButton = ttk.Radiobutton(self.monty2, text=self.colour[col], variable=self.radio, value=col+1, command=self.radioButtonCall)
            self.radioButton.grid(column=0+col, row=1, sticky=tk.W)
            
        # SPINBOX
        self.spin = tk.Spinbox(self.monty, values=(1,2,4,6,7,8,100), width=5, bd=8, state='readonly', command=self._spinBox) # bd = borderwidth (makes it embedded)
        self.spin.grid(column=0, row=2, sticky='W')
        createToolTip(self.spin, 'This is a Spin control.')
        
        # SCROLLED TEXT
        self.scrolledTextWidth = 40
        self.scrolledTextHeight = 10
        self.scrText = ScrolledText.ScrolledText(self.monty, width=self.scrolledTextWidth, height=self.scrolledTextHeight, wrap=tk.WORD) # wrap=tk.WORD ... wraps words so a new line doesn't start mid-word
        self.scrText.grid(column=0, row=3, columnspan=3, sticky='WE')
        createToolTip(self.scrText, 'This is a ScrolledText widget.')
        
        # LABEL FRAME
        labelFrame = ttk.LabelFrame(self.monty2, text=" Labels in a frame ")
        #labelFrame.grid(column=0, row=1, padx=20, pady=20, sticky='NW')
        labelFrame.grid(columnspan=3, padx=5, pady=5, sticky='W')
        ttk.Label(labelFrame, text="Label 1").grid(column=0, row=0)
        ttk.Label(labelFrame, text="Label 2").grid(column=0, row=1)
        ttk.Label(labelFrame, text="Label 3").grid(column=0, row=2)
        
        for subLabel in labelFrame.winfo_children():
            subLabel.grid_configure(padx=8, pady=4)
            
        # LEFT ALLIGNS ALL WIDGETS IN FRAME MONTY
        #for child in monty.winfo_children():
        #    child.grid_configure(sticky='W', padx=5, pady=5)
            
        # MENU BAR
        menuBar = tk.Menu(self.win)
        self.win.config(menu=menuBar)
        
        fileMenu = tk.Menu(menuBar,tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        helpMenu = tk.Menu(menuBar,tearoff=0) # Creating menu
        helpMenu.add_command(label="About", command=self._aboutMsgBox) # Adding items to menu
        helpMenu.add_command(label="Test warning", command=self._warning)
        helpMenu.add_command(label="Test error", command=self._error)
        helpMenu.add_command(label="Test question", command=self._question)
        menuBar.add_cascade(label="Help", menu=helpMenu) # Inserting menu into menu bar
        
        # ADDITIONS TO SECOND TAB
        # Create Manage Files Frame
        mngFilesFrame = ttk.LabelFrame(self.tab2, text=' Manage Files: ')
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=5, pady=5)
        # Button Callback
        def getFileName():
            print('hello from getFileName')
            fDir = path.dirname(__file__)
            fName = tkFileDialog.askopenfilename(parent=self.win, initialdir=fDir)
            self.fileEntry.config(state='write')
            self.fileEntry.delete(0, tk.END)
            self.fileEntry.insert(0, fName)
            self.fileEntry.config(width=len(fName) + 3)
        # Add Widgets to Manage Files Frame
        lb = ttk.Button(mngFilesFrame, text="Browse to File...", command=getFileName)
        lb.grid(column=0, row=0, sticky='WE')
        file = tk.StringVar()
        self.entryLen = self.scrolledTextWidth
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)
        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W)
        def copyFile():
            import shutil
            src = self.fileEntry.get()
            print(src)
            file = src.split('/')[-1]
            print(file)
            dst = self.netwEntry.get() + '/'+ file
            print(dst)
            try:
                shutil.copy(src, dst)
                tkMessageBox.showinfo('Copy File to Network', 'Success: File copied.')
#            except FileNotFoundError as err:
            except IOError as err:
                tkMessageBox.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as ex:
                tkMessageBox.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(ex))
        cb = ttk.Button(mngFilesFrame, text="Copy File To : ", command=copyFile)
        cb.grid(column=0, row=1, sticky='WE')
        # Add some space around each label
        for child in mngFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)
                
            




        
        #self.nameEntered.focus() # Place cursor into name Entry
        self.tabControl.select(1)
        
oop = OOP()
runT = Thread(target=oop.methodInAThread)
oop.win.mainloop()


### Continue from page 142