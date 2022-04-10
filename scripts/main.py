from PIL import Image
from tkinter import *
from tkinter import filedialog as tkFileDialog
import correlate
import point

def start():
	point.checkFinger(inPut.get() ,outPut.get())

def openRef(event):
	options = {}
	options['defaultextension'] = ''
	options['filetypes'] = [('text files', '.txt')]
	options['initialdir'] = 'C:\\'
	options['parent'] = root
	options['title'] = 'Open Input File'
	
	input = tkFileDialog.askopenfilename()
	if input:
		inPut.set(input)

def openVer(event):
	options = {}
	options['defaultextension'] = ''
	options['filetypes'] = [('text files', '.txt')]
	options['initialdir'] = 'C:\\'
	options['parent'] = root
	options['title'] = 'Open Output File'
	
	output = tkFileDialog.askopenfilename()  
	if output:
		outPut.set(output)

global root
root = Tk()
root.title("Распознователь отпечатков")
root.resizable(False, False)

global inPut
global outPut
global autoGraph
inPut = StringVar()
inPut.set('')
outPut = StringVar()
outPut.set('')
autoGraph = StringVar()
autoGraph.set('')

inEntry = Entry(root, textvariable=inPut)
outEntry = Entry(root, textvariable=outPut)

getInFile = Button(root, text='Открыть файл...')
getOutFile = Button(root, text='Открыть файл...')

getInFile.bind('<1>',openRef)
getOutFile.bind('<1>',openVer)

sign = Button(root, text='Старт', command=start)

inEntry.grid(row=0,column=0)
outEntry.grid(row=1,column=0)

getInFile.grid(row=0,column=1)
getOutFile.grid(row=1,column=1)

sign.grid(row=3,column=1)


root.mainloop()