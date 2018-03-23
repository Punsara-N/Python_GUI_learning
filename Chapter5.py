try:
    # for Python2
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import Tkinter as tk
except ImportError:
    # for Python3
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import tkinter as tk

fig = Figure(figsize=(12,8), facecolor='white')

axis = fig.add_subplot(211)

xValues = [1,2,3,4]
yValues = [5,7,6,8]
axis.plot(xValues, yValues)
axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')
axis.grid(linestyle='-')

axis = fig.add_subplot(212)

xValues = [1,2,3,4]

yValues1 = [5,7,6,8]
yValues2 = [8,9,50,5]
yValues3 = [5,6,7,8]

yAll = [yValues1, yValues2, yValues3]
        
minY = min([y for yValues in yAll for y in yValues])
print("Min y = " + str(minY))

yUpperLimit = 20
maxY = max([y for yValues in yAll for y in yValues if y < yUpperLimit])
print("Max y = " + str(maxY))


t0, = axis.plot(xValues, yValues1, color='red')
t1, = axis.plot(xValues, yValues2, color='green')
t2, = axis.plot(xValues, yValues3, color='blue')
axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')
axis.grid()
axis.set_ylim(minY, maxY)
axis.set_xlim(min(xValues), max(xValues))

fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'), 'upper right')

def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()