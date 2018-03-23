import Tkinter as tk
import ttk # Themed tkinter
import ScrolledText

win = tk.Tk()
win.title("Python GUI")
win.resizable(0, 0) #Disable resizing the GUI

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

# SCROLLED TEXT
scrolledTextWidth = 30
scrolledTextHeight = 3
scrText = ScrolledText.ScrolledText(monty, width=scrolledTextWidth, height=scrolledTextHeight, wrap=tk.WORD) # wrap=tk.WORD ... wraps words so a new line doesn't start mid-word
scrText.grid(column=0, row=4, columnspan=3, sticky='WE')

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
    
# MENU BAR
menuBar = tk.Menu(win)
win.config(menu=menuBar)

fileMenu = tk.Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = tk.Menu(menuBar,tearoff=0) # Creating menu
helpMenu.add_command(label="About") # Adding items to menu
helpMenu.add_command(label="More info")
menuBar.add_cascade(label="Help", menu=helpMenu) # Inserting menu into menu bar





nameEntered.focus() # Place cursor into name Entry
win.mainloop()