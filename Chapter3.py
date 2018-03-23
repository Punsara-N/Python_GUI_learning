try:
    # for Python2
    import Tkinter as tk
    import ttk # Themed tkinter
    import ScrolledText
    import tkMessageBox
except ImportError:
    # for Python3
    import tkinter as tk
    from tkinter import ttk
    import tkinter.scrolledtext as ScrolledText
    from tkinter import tkMessageBox

win = tk.Tk()
win.title("Python GUI")
win.resizable(0, 0) #Disable resizing the GUI
win.iconbitmap(r'images\Captain-America.ico')

# CLASS FOR CREATING TOOL TIPS
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT, background="#ffffe0", relief=tk.SOLID, borderwidth=1,
        font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
#===========================================================
def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

# CREATING TABS
tabControl = ttk.Notebook(win) # Create tab control (list)
tabControl.pack(expand=1, fill="both") # Makes tab visible

tab1 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab1, text="Tab 1") # Adds the tab

tab2 = ttk.Frame(tabControl) # A new tab
tabControl.add(tab2, text="Tab 2") # Adds the tab

# CREATING A CONTAINER FRAME IN THE WINDOW TO HOLD ALL WIDGETS
monty = ttk.LabelFrame(tab1, text=" Monty Python ")
monty.grid(column=0, row=0, padx=20, pady=20)

# BUTTON
def clickMe2():
    action2.configure(text='Hello ' + name.get() + ' ' + number.get())
    action2.configure(state='disabled') # Disable the Button Widget

ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='WE')
action2 = ttk.Button(monty, text="Click me!", command=clickMe2)
action2.grid(column=2, row=1)

# COMBOBOX
aLabel2 = ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly') # ...state='readonly')  does not allow the user to enter his/her own value into combo box
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# NEW LABEL FRAME FOR TAB 2
monty2 = ttk.LabelFrame(tab2, text=" The Snake ")
monty2.grid(column=0, row=0, padx=20, pady=20)

# CHECKBOXES
check1 = tk.IntVar()
checkBox1 = tk.Checkbutton(monty2, text="Disabled", variable=check1, state='disabled')
checkBox1.select()
checkBox1.grid(column=0, row=0, sticky=tk.W) # sticky=tk.W ... alligns west of grid 
check2 = tk.IntVar()
checkBox2 = tk.Checkbutton(monty2, text="Unchecked", variable=check2)
checkBox2.deselect()
checkBox2.grid(column=1, row=0, sticky=tk.W)
check3 = tk.IntVar()
checkBox3 = tk.Checkbutton(monty2, text="Enabled", variable=check3)
checkBox3.select()
checkBox3.grid(column=2, row=0, sticky=tk.W)

# RADIO BUTTONS
def radioButtonCall(): # Radio button callback
    radioValue = radio.get()
    if radioValue == 1:
        monty2.configure(text=colour[0])
    elif radioValue == 2:
        monty2.configure(text=colour[1])
    elif radioValue == 3:
        monty2.configure(text=colour[2])
        
colour = ('Blue', 'Gold', 'Red')
radio = tk.IntVar()
radio.set(99)
for col in range(3):
    radioButton = ttk.Radiobutton(monty2, text=colour[col], variable=radio, value=col+1, command=radioButtonCall)
    radioButton.grid(column=0+col, row=1, sticky=tk.W)
    
# SPINBOX
def _spinBox(): # A function for the spinbox
    value = spin.get()
    print(value)
    scrText.insert(tk.INSERT, value + '\n') # Prints it into the scroll text
    scrText.yview_pickplace('end') # Auto scroll down
spin = tk.Spinbox(monty, values=(1,2,4,6,7,8,100), width=5, bd=8, state='readonly', command=_spinBox) # bd = borderwidth (makes it embedded)
spin.grid(column=0, row=2)
createToolTip(spin, 'This is a Spin control.')

# ANOTHER SPINBOX
spin2 = tk.Spinbox(monty, values=(1,2,3), width=5, bd=8, state='readonly', command=_spinBox, relief=tk.RIDGE) # Types of boarders: tk.SUNKEN tk.RAISED tk.FLAT tk.GROOVE tk.RIDGE
spin2.grid(column=1, row=2)
createToolTip(spin2, 'This is another Spin control.')

# SCROLLED TEXT
scrolledTextWidth = 30
scrolledTextHeight = 3
scrText = ScrolledText.ScrolledText(monty, width=scrolledTextWidth, height=scrolledTextHeight, wrap=tk.WORD) # wrap=tk.WORD ... wraps words so a new line doesn't start mid-word
scrText.grid(column=0, row=3, columnspan=3, sticky='WE')
createToolTip(scrText, 'This is a ScrolledText widget.')

# LABEL FRAME
labelFrame = ttk.LabelFrame(tab2, text=" Labels in a frame ")
labelFrame.grid(column=0, row=1, padx=20, pady=20, sticky='NW')
ttk.Label(labelFrame, text="Label 1").grid(column=0, row=0)
ttk.Label(labelFrame, text="Label 2").grid(column=0, row=1)
ttk.Label(labelFrame, text="Label 3").grid(column=0, row=2)

for subLabel in labelFrame.winfo_children():
    subLabel.grid_configure(padx=8, pady=4)
    
# LEFT ALLIGNS ALL WIDGETS IN FRAME MONTY
#for child in monty.winfo_children():
#    child.grid_configure(sticky='W', padx=5, pady=5)
    
# FUNCTIONS FOR MENU BAR
def _quit():
    win.quit()
    win.destroy()
    #exit() # This exits python!

def _aboutMsgBox():
    tkMessageBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2018.')
    
def _warning():
    tkMessageBox.showwarning('WARNING!', 'This is a test warning!')

def _error():
   tkMessageBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
   
def _customMessage(msg):
    tkMessageBox.showinfo("Hello!", "Hello " + msg)
   
def _question():
    answer = tkMessageBox.askyesno('Test question', 'Are you a male?')
    if answer == True:
        msg="Sir!"
    else:
        msg="Madam!"
    _customMessage(msg)
    
# MENU BAR
menuBar = tk.Menu(win)
win.config(menu=menuBar)

fileMenu = tk.Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = tk.Menu(menuBar,tearoff=0) # Creating menu
helpMenu.add_command(label="About", command=_aboutMsgBox) # Adding items to menu
helpMenu.add_command(label="Test warning", command=_warning)
helpMenu.add_command(label="Test error", command=_error)
helpMenu.add_command(label="Test question", command=_question)
menuBar.add_cascade(label="Help", menu=helpMenu) # Inserting menu into menu bar

# A NEW TAB
tab3 = ttk.Frame(tabControl) # A new tab
tabControl.add(tab3, text="Tab 3") # Adds the tab
tab33 = tk.Frame(tab3, bg='blue')
tab33.pack()
for orangeColor in range(2):
    canvas = tk.Canvas(tab33, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orangeColor, column=orangeColor)


nameEntered.focus() # Place cursor into name Entry
win.mainloop()