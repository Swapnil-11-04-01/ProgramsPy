#*******************************************************************
#-------------------------------------------------------------------
# Importing all required modules.
#-------------------------------------------------------------------
#*******************************************************************
from tkinter import *
from PIL import Image, ImageTk
import pygame
from functools import partial
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import requests





# Initialising sound variable with True value by default.
sound = True





#********************************************************************************************************************
#--------------------------------------------------------------------------------------------------------------------
# Main Interactive Page.
#--------------------------------------------------------------------------------------------------------------------
#********************************************************************************************************************
def main(event):

    #****************************************************************************************************************
    # Defing events inside Menu Bar.
    #****************************************************************************************************************
    def newFile():
        global file
        file = None
        codeArea.delete(1.0, END)

    def openFile():
        global file
        file = askopenfilename(defaultextension=".py", filetypes=[("All Files", "*.*"), ("Python files", "*.py")])
        if file == "":
            file = None
        else:
            # root.title(os.path.basename(file) + " - ProgramsPy")
            codeArea.delete(1.0, END)
            f = open(file, "r")
            codeArea.insert(1.0, f.read())
            f.close()
    #----------------------------------------------------
    # Event to Save File to be handled here in future.
    #----------------------------------------------------

    def exitFile():
        root.destroy()


    def cut():
        codeArea.event_generate(("<<Cut>>"))

    def copy():
         codeArea.event_generate(("<<Copy>>"))

    def paste():
        codeArea.event_generate(("<<Paste>>"))


    def theme1():
            codeArea.config(background = "white", foreground = "black")

    def theme2():
            codeArea.config(background = "black", foreground = "light grey")

    def theme3():
            codeArea.config(background = "#000051", foreground = "#FFC600")

    def theme4():
            codeArea.config(background = "#FFC600", foreground = "#000051")

    def about():
        showinfo("Programs.Py", "Made by Swapnil Sharma\n      Have a Nice Day !!")





    #**********************************************************************
    # Events of all the Problem Buttons are handled here.
    #**********************************************************************
    def open1(event):
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 1.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\1.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\2.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\3.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\4.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\5.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\6.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 7":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 7.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\7.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 8":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 8.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\8.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 9":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 9.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\9.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 10":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 1\Problem - 10.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 1\\10.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))

    def open2(event):
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 1.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 7":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 7.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 8":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 2\Problem - 8.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()

    def open3(event):
        print(event.widget.cget("text"))
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 1.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 7":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 7.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 8":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 8.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 9":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 9.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 10":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 3\Problem - 10.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()

    def open4(event):
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 1.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 7":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 7.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 8":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 8.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 9":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 9.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 10":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 4\Problem - 10.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()

    def open5(event):
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 5\Problem - 1.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 5\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 5\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 5\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 5\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 5\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()

    def open6(event):
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 1.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 7":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 7.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 8":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 8.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 9":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 9.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
        elif event.widget.cget("text") == "Problem - 10":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 6\Problem - 10.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()

    def open7(event):
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 1.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\1.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\2.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\3.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\4.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\5.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\6.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 7":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 7.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\7.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 8":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 8.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\8.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 9":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 9.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\9.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 10":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 7\Problem - 10.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 7\\10.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))

    def open8(event):
        if event.widget.cget("text") == "Problem - 1":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 1.txt", "r")
            question.config(text=file.read(), foreground="white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\1.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 2":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 2.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\2.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 3":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 3.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\3.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 4":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 4.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\4.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 5":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 5.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\5.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 6":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 6.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\6.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 7":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 7.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\7.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 8":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 8.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\8.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 9":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 9.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\9.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 10":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 10.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\10.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))
        elif event.widget.cget("text") == "Problem - 11":
            codeArea.delete(1.0, END)
            file = open("Assignments\Assignment - 8\Problem - 11.txt", "r")
            question.config(text = file.read(), foreground = "white")
            file.close()
            codeFile = open("Assignments\Assignment - 8\\11.py", "rb")
            viewBtn.config(command = partial(viewCode, codeFile))





    #*******************************************************************************************************
    # Events of all the Assignment Buttons pressed are handled here.
    #*******************************************************************************************************
    def program(event):
        # Problem Buttons
        if event.widget.cget("text") == "Assignment - 1":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 11):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open1)

            topic.config(text = "1. BASIC PYTHON - I")



        elif event.widget.cget("text") == "Assignment - 2":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 9):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open2)

            topic.config(text = "2. BASIC PYTHON - II")



        elif event.widget.cget("text") == "Assignment - 3":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 11):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open3)

            topic.config(text = "3. FOR LOOP")



        elif event.widget.cget("text") == "Assignment - 4":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 11):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open4)

            topic.config(text = "4. WHILE LOOP")



        elif event.widget.cget("text") == "Assignment - 5":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 7):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open5)

            topic.config(text = "5. NESTED LOOP")



        elif event.widget.cget("text") == "Assignment - 6":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 11):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open6)

            topic.config(text = "6. FUNCTIONS")



        elif event.widget.cget("text") == "Assignment - 7":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 11):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open7)

            topic.config(text = "7. STRINGS")



        elif event.widget.cget("text") == "Assignment - 8":
            codeArea.delete(1.0, END)
            question.config(text="")

            for widgets in problem_frame.winfo_children():
                widgets.destroy()

            Label(problem_frame, width=1, background="#444444", relief=GROOVE).pack(side=RIGHT, fill=Y)

            for i in range(1, 12):
                programBtn = Button(problem_frame, text=f"Problem - {i}", font="lucida 10 bold",
                                    height=2, width=16, background="#777777", foreground="light grey")
                programBtn.pack(fill=X, side=TOP, pady=3)
                programBtn.bind("<Button-1>", open8)

            topic.config(text = "8. LISTS")





    #****************************************************
    # Event of loading code in Code Area is handled here.
    #****************************************************
    def viewCode(codeFile):
        codeArea.delete(1.0, END)
        codeArea.insert(1.0, codeFile.read())
        codeFile.close()





    #*****************************************
    # Setting up environment
    #*****************************************
    root = Tk()
    root.title("PROGRAMS.PY - Swapnil Sharma")
    root.state("zoomed")
    root.config(background="#101010")
    root.resizable(False, False)





    #******************************************************
    # Menu Bar
    #******************************************************
    mainmenu = Menu(root)
    m1 = Menu(mainmenu, tearoff = 0)
    m1.add_command(label="New", command = newFile)
    m1.add_command(label="Open", command = openFile)
    # m1.add_command(label="Save", command = saveFile)
    m1.add_command(label="Exit", command = exitFile)
    root.config(menu = mainmenu)
    mainmenu.add_cascade(label = "File", menu = m1)

    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label="Cut", command = cut)
    m2.add_command(label="Copy", command = copy)
    m2.add_command(label="Paste", command = paste)
    mainmenu.add_cascade(label="Edit", menu=m2)

    m3 = Menu(mainmenu, tearoff = 0)
    m3.add_command(label="Light", command = theme1)
    m3.add_command(label="Dark", command = theme2)
    m3.add_command(label="Blue", command = theme3)
    m3.add_command(label="Yellow", command = theme4)
    root.config(menu = mainmenu)
    mainmenu.add_cascade(label = "Themes", menu = m3)

    m4 = Menu(mainmenu, tearoff = 0)
    m4.add_command(label = "About me", command = about)
    mainmenu.add_cascade(label = "Know more", menu = m4)





    #***************************************************************************
    # Status Bar
    #***************************************************************************
    statusvar = StringVar()
    statusvar.set("Ready")
    sbar = Label(root, textvariable = statusvar, relief = RAISED, anchor = "w")
    sbar.pack(side = BOTTOM, fill = X)





    #***********************************************************************************************************
    # Assignments Frame
    #***********************************************************************************************************
    assignments_frame = Frame(root, background = "#090909", width = 300, relief = SUNKEN)
    assignments_frame.pack(side = LEFT, fill = Y)
    # Scroll Bar 1
    Label(assignments_frame, width =1, background = "#444444", relief = GROOVE).pack(side = RIGHT, fill = Y)
    # Assignment Buttons
    for i in range(1, 9):
        assignmentBtn = Button(assignments_frame, text = f"Assignment - {i}", font = "lucida 19 bold",
                               relief = RAISED, height = 2, width = 16, background = "#131313",
                               foreground = "light grey")

        assignmentBtn.pack(fill = X, side = TOP, pady = 3)
        assignmentBtn.bind("<Button-1>", program)





    #****************************************************************
    # Problems Frame
    #****************************************************************
    problem_frame = Frame(root, background="#101010", relief=SUNKEN)
    problem_frame.pack(side=LEFT, fill=Y)





    #*************************************************************************************
    # Topic Frame
    #*************************************************************************************
    topic_frame = Frame(root, height=280, relief = SUNKEN)
    topic_frame.pack(side=TOP, fill=X)

    topic = Label(topic_frame, background = "black", height= 2, font = "lucida 12 bold",
                  foreground = "green", pady = 0)
    topic.pack(side = TOP, fill = X)

    question = Label(topic_frame, height = 10, background = "#101010", font = "lucida 15",
                     anchor = "n", pady = 5, padx = 10)
    question.pack(side = BOTTOM, fill = X)





    #****************************************************************************************************************
    # Code Frame
    #****************************************************************************************************************
    code_frame = Frame(root, background="#101010", height = 505, relief = SUNKEN)
    code_frame.pack(side = TOP, fill=X)

    btnFrame = Frame(code_frame, background="#111111", relief=SUNKEN, height=2)
    btnFrame.pack(side=TOP, fill=X)
    viewBtn = Button(btnFrame, text="VIEW CODE", background="#003874", font="lucida 15 bold",
                     foreground="light grey")
    viewBtn.pack(side=RIGHT, padx=5)

    Label(code_frame, text = "CODE WINDOW", background = "#444444", anchor = "w", foreground = "light grey",
          relief = GROOVE, font = "lucida 10 bold", height = 1, padx = 10).pack(side = TOP, fill = X)

    scroll_y = Scrollbar(code_frame)
    scroll_y.pack(side = RIGHT, fill = Y)
    scroll_x = Scrollbar(code_frame, orient = HORIZONTAL)
    scroll_x.pack(side=BOTTOM, fill=X)

    codeArea = Text(code_frame, background = "white", relief = SUNKEN, height = 28, yscrollcommand = scroll_y.set,
         xscrollcommand = scroll_x.set, font = "comicsan 10")
    codeArea.pack(fill = BOTH)
    scroll_y.config(command = Text.yview)
    scroll_x.config(command=Text.xview)





    #**************
    # Concluding
    #**************
    root.mainloop()







#***************************************************************************************************************
#...............................................................................................................
# Starting Page
#...............................................................................................................
#***************************************************************************************************************
def startWindow():

    #**************************************
    # Importing and handeling sound
    #**************************************
    pygame.mixer.init()
    pygame.mixer.music.load("bgmusic.wav")





    #********************************************************
    # Events
    #********************************************************
    def enter(event):
        b.config(background="#090909")

    def leave(event):
        b.config(background="black")

    def f_in(event):
        b.config(background="#090909")

    def f_out(event):
        b.config(background="black")

    def play(event):
        if img_sound.cget("background") == "#121212":
            pygame.mixer.music.play(-1)
            img_sound.config(image=photo4)
            img_sound.config(background = "#141414")
        else:
            pygame.mixer.music.stop()
            img_sound.config(image=photo3)
            img_sound.config(background="#101010")

    def img_enter(event):
        if img_sound.cget("background") == "#101010":
            img_sound.config(background="#121212")
        elif img_sound.cget("background") == "#141414":
            img_sound.config(background="#131313")

    def img_leave(event):
        if img_sound.cget("background") == "#121212":
            img_sound.config(background="#101010")
        elif img_sound.cget("background") == "#131313":
            img_sound.config(background="#141414")





    #*******************************************
    # Basic structure of page
    #*******************************************
    root = Tk()
    root.title("PROGRAMS.PY - Swapnil Sharma")
    root.state("zoomed")
    root.resizable(False, False)
    root.config(background="#101010")





    #*****************************************************
    # Importing images
    #*****************************************************
    image = Image.open("3.png")
    image = image.resize((300, 150), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    image3 = Image.open("soundOff.png")
    image3 = image3.resize((150, 100), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image3)

    image4 = Image.open("soundOn.png")
    image4 = image4.resize((150, 100), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(image4)





    #**********************************************************************************************
    # Handeling all widgets
    #**********************************************************************************************
    f = Frame(root)
    f.pack(fill=X)
    Label(f, text="Welcome to PROGRAMS.PY", font="Script 80 bold", background="black",
          foreground="grey").pack(fill=X, ipady=10)


    f = Frame(root)
    f.pack(fill=X)
    Label(f, text="'' Experience is the name everyone gives to their mistakes ''",
          font="lucida 20", background="grey", foreground="#1E1E1E", relief=SUNKEN).pack(fill=X)


    f = Frame(root, background="#101010")
    f.pack(side=LEFT, fill=Y)
    img_sound = Label(f, image=photo3, background="#101010")
    img_sound.pack(side=BOTTOM, ipady=10, ipadx=70)
    img_sound.bind("<ButtonRelease-1>", play)
    img_sound.bind("<Enter>", img_enter)
    img_sound.bind("<Leave>", img_leave)


    f = Frame(root, background="#101010")
    f.pack(side=RIGHT, fill=Y, ipadx=10)
    b = Button(f, text="ENTER", relief=RAISED, font="lucidia 25 bold", background="black", foreground="grey")
    b.pack(ipadx=70, ipady=10, side=BOTTOM)
    b.bind("<ButtonRelease-1>", main)
    b.bind("<Enter>", enter)
    b.bind("<Leave>", leave)
    b.bind("<FocusIn>", f_in)
    b.bind("<FocusOut>", f_out)


    f = Frame(root, background="#101010")
    f.pack(fill=X, pady=225)
    img = Label(f, image=photo, background="#101010")
    img.pack(side=BOTTOM, ipadx=10)







    #****************************
    # Entering infinite mainloop
    #****************************
    root.mainloop()







# START
startWindow()







#***********************************************************************************************************************
#.......................................................................................................................
# Problematic Code Snippet for Save File event
# def saveFile():
#     global file
#     if file == None:
#         file = asksaveasfilename(initialfile='Untitled.py', defaultextension=".py", filetypes=[("All Files", "*.*"),
#                         ("Python files", "*.py")])
#         if file == "":
#             file = None
#
#         else:
#             # Save as a new file
#             f = open(file, "w")
#             f.write(codeArea.get(1.0, END))
#             f.close()
#
#             root.title(os.path.basename(file) + " - ProgramsPy")
#             print("File Saved")
#     else:
#         # Save the file
#         f = open(file, "w")
#         f.write(codeArea.get(1.0, END))
#         f.close()
#.......................................................................................................................
#***********************************************************************************************************************