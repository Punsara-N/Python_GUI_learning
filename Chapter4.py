#IMPORTING
try:
    # for Python2
    import Tkinter as tk
    import ttk # Themed tkinter
    import ScrolledText
    import tkMessageBox
    #import tooltip as tt
    from tooltip import createToolTip
except ImportError:
    # for Python3
    import tkinter as tk
    from tkinter import ttk
    import tkinter.scrolledtext as ScrolledText
    from tkinter import tkMessageBox
    import tooltip as tt
    
class OOP():
    
    def __init__(self):

        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.win.resizable(0, 0) #Disable resizing the GUI
        self.win.iconbitmap(r'images\Captain-America.ico')
        self.main()
        
    # BUTTON METHOD
    def clickMe2(self):
        self.action2.configure(text='Hello ' + self.name.get() + ' ' + self.number.get())
        self.action2.configure(state='disabled') # Disable the Button Widget
        
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
        #exit() # This exits python!
        
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
        self.monty.grid(column=0, row=0, padx=20, pady=20)
        
        # FIRST AND SECOND ROWS (LABELS AND ENTRY BOXES)
        ttk.Label(self.monty, text="Enter a name:").grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.monty, width=12, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1, sticky='WE')
        self.action2 = ttk.Button(self.monty, text="Click me!", command=self.clickMe2)
        self.action2.grid(column=2, row=1)
        
        # COMBOBOX
        self.aLabel2 = ttk.Label(self.monty, text="Choose a number:").grid(column=1, row=0)
        self.number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.monty, width=12, textvariable=self.number, state='readonly') # ...state='readonly')  does not allow the user to enter his/her own value into combo box
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
        self.spin.grid(column=0, row=2)
        createToolTip(self.spin, 'This is a Spin control.')
        
        # ANOTHER SPINBOX
        self.spin2 = tk.Spinbox(self.monty, width=5, bd=8, state='readonly', command=self._spinBox, relief=tk.RIDGE) # Types of boarders: tk.SUNKEN tk.RAISED tk.FLAT tk.GROOVE tk.RIDGE
        self.spin2['values'] = (1,2,3)
        self.spin2.grid(column=1, row=2)
        createToolTip(self.spin2, 'This is another Spin control.')
        
        # SCROLLED TEXT
        scrolledTextWidth = 30
        scrolledTextHeight = 3
        scrText = ScrolledText.ScrolledText(self.monty, width=scrolledTextWidth, height=scrolledTextHeight, wrap=tk.WORD) # wrap=tk.WORD ... wraps words so a new line doesn't start mid-word
        scrText.grid(column=0, row=3, columnspan=3, sticky='WE')
        createToolTip(scrText, 'This is a ScrolledText widget.')
        
        # LABEL FRAME
        labelFrame = ttk.LabelFrame(self.tab2, text=" Labels in a frame ")
        labelFrame.grid(column=0, row=1, padx=20, pady=20, sticky='NW')
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
        
        # A NEW TAB
        self.tab3 = ttk.Frame(self.tabControl) # A new tab
        self.tabControl.add(self.tab3, text="Tab 3") # Adds the tab
        self.tab33 = tk.Frame(self.tab3, bg='blue')
        self.tab33.pack()
        for orangeColor in range(2):
            canvas = tk.Canvas(self.tab33, width=150, height=80, highlightthickness=0, bg='orange')
            canvas.grid(row=orangeColor, column=orangeColor)
        
        strData = self.spin.get()
        print("Spinbox value: " + strData)
        
        self.nameEntered.focus() # Place cursor into name Entry
        


oop = OOP()
oop.win.mainloop()