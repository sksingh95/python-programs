from tkinter import *
import subprocess

def create_dev_file():
    devName = entryDeviceFile.get()
    majorNo = entryMajorNo.get()
    minorNo = entryMinorNo.get()
    cmd = subprocess.Popen(['sudo','mknod','/dev/'+devName, 'c', majorNo, minorNo], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = cmd.communicate()
    if err == "":
        statusVar.set(output)
    else :
        statusVar.set(err)

def remove_dev_file():
    devName = entryDeviceFile.get()
    cmd = subprocess.Popen(['sudo','rm','/dev/'+devName], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = cmd.communicate()
    if err == "":
        statusVar.set(output)
    else :
        statusVar.set(err)
    
window = Tk()
''' 
	Take Device File name
'''
lblDeviceFile = Label(window, text="Device File Name : ")
lblDeviceFile.grid(row=0, column=0)
entryDeviceFile = Entry(window)
entryDeviceFile.grid(row=0, column=1)

''' 
	Take major no
'''
lblMajorNo = Label(window, text="Major No. : ")
lblMajorNo.grid(row=1, column=0)
entryMajorNo = Entry(window)
entryMajorNo.grid(row=1, column=1)

''' 
	Take minor no
'''
lblMinorNo = Label(window, text="Minor No. : ")
lblMinorNo.grid(row=2, column=0)
entryMinorNo = Entry(window)
entryMinorNo.grid(row=2, column=1)

'''
    Status Label
'''
statusVar = StringVar()
lblStatus = Label(window, textvariable=statusVar, fg="red");
lblStatus.grid(row=3, column=0, columnspan=2)
''' 
	Add buttons
'''
btnDevFileCrte = Button(window, text = "Create Device File", command=create_dev_file)
btnDevFileCrte.grid(row=4, column=0)
btnDevFileCrte = Button(window, text = "Remove Device File", command=remove_dev_file)
btnDevFileCrte.grid(row=4, column=1)

window.mainloop()
