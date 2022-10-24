from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from os.path import isfile, join
from tkinter import messagebox
import easygui, os

# Tkinter Setup
appName = 'Quick Template'
version = 'v1'
author = 'MTMAK9'

root = Tk()
root.title(appName)
root.geometry('700x580')
root.iconbitmap('icon.ico')
root.resizable(False,False)
root.configure(bg='#9fc5e8')
#root.grid_columnconfigure(0, weight=1)

#-set the base path
path = './templates/'

n = StringVar()
combo_list = ttk.Combobox(root, height=10, width=80, textvariable=n)
text_message = ' '

# File Types, when opening and saving files.
ch = ('.txt')
file_ls = [f for f in os.listdir(path) if isfile(join(path, f))]
file_ls = [elem.replace(ch, '') for elem in file_ls]
combo_list['values'] = file_ls
combo_list['state'] = 'readonly'
combo_list.current(0)

#--Display Function
def display():
    selected = combo_list.get()
    text_file = open((path + selected + '.txt'), 'r')
    stuff = text_file.read()
    text_box.delete('1.0', END)
    text_box.insert(END, stuff)
                
#--Save Function
def save():
    selected = combo_list.get()
    new_text = text_box.get(1.0, END)
    if len(new_text) == 1.0:
        MsgBox = messagebox.askquestion('Save empty Template','Text box is empty, are you sure to Save it?', icon='warning')
        if MsgBox == 'yes':
            new_text_file = open((path + selected + '.txt'), 'w')
            new_text_file.write(new_text)
            new_text_file.close()
            Show = Label(root, text = "Empty Template has been saved", bg='#9fc5e8')
            Show.place(x = 265, y = 435)
            root.after(2500, Show.destroy)
        else:
            pass
    else:
        new_text_file = open((path + selected + '.txt'), 'w')
        new_text_file.write(new_text)
        new_text_file.close()
        Show = Label(root, text = "Template has been saved", bg='#9fc5e8')
        Show.place(x = 280, y = 435)
        root.after(2500, Show.destroy)
       
#--Add Function
def add():
    template_name = easygui.enterbox("What is your Template name?")
    with open((path + template_name + '.txt'), 'w') as f:
        f.write('')
    Show = Label(root, text ="New template has been Created", bg='#9fc5e8')
    Show.place(x = 265, y = 435)
    root.after(2500, Show.destroy)
    ch = ('.txt')
    file_ls = [f for f in os.listdir(path) if isfile(join(path, f))]
    file_ls = [elem.replace(ch, '') for elem in file_ls]
    combo_list['values'] = file_ls
    combo_list.current(0)

#--Edit Function
def edit():
    #status_box.config(text='')
    selected = combo_list.get()
    old_title_name = (path + selected + '.txt')
    new_name = easygui.enterbox("What is your new Template name?")
    new_title_name = (path + new_name + '.txt')
    os.rename(old_title_name,new_title_name)
    messagebox.showinfo(title='Template renamed', message='Template name has been changed')
    Show = Label(root, text ="Template name has been changed.", bg='#9fc5e8')
    Show.place(x = 265, y = 435)
    root.after(2500, Show.destroy)
    ch = ('.txt')
    file_ls = [f for f in os.listdir(path) if isfile(join(path, f))]
    file_ls = [elem.replace(ch, '') for elem in file_ls]
    combo_list['values'] = file_ls
    combo_list.current(0)

def delete():
    ch = ('.txt')
    selected = combo_list.get()
    filename = (path + selected + ch)
    ## If file exists, delete it ##
    if os.path.isfile(filename):
        os.remove(filename)
    else:    ## Show an error ##
        print("Error: %s file not found" % filename)
    
    Show = Label(root, text ="Template has been deleted", bg='#9fc5e8')
    Show.place(x = 280, y = 435)
    root.after(2500, Show.destroy)
    combo_list.set('')
    file_ls = [f for f in os.listdir(path) if isfile(join(path, f))]
    file_ls = [elem.replace(ch, '') for elem in file_ls]
    combo_list['values'] = file_ls
    combo_list.current(0)
    
#---ComboBox Alocated---
combo_list
combo_list.pack(pady=10)
combo_list.current(0)

#------------Buttons--------------------------
#--Display Button
Show = Button(root, text='Display', font=('Calibri', 10), borderwidth=2,
              bg="#BBFF8F", command=display)
Show.pack(padx=5, pady=5)
#--Text Box
mid_frame = LabelFrame(root, padx=5, pady=5, bg='#9fc5e8')
text_box = Text(root, height="20", width="70", borderwidth=1, bg="#f3f6f4")
text_box.pack(pady=5)
#--Show Box
bottom_frame = LabelFrame(root,text='Info-Log:', padx=275, pady=7, bg='#9fc5e8', labelanchor=N)
bottom_frame.pack(pady=5, expand='yes')
status_box = Label(bottom_frame, text=' ', bg='#9fc5e8')
status_box.pack(expand='no')
#------Buttons Settings
frame = LabelFrame(root, text='Settings:', padx=80, pady=5, bg='#9fc5e8', labelanchor=N)
frame.pack(padx=5, pady=5)
#--Save Button
Save = Button(frame, text='Save', font=('Calibri', 10), borderwidth=2,
                     bg="#97DB98", command=save).grid(row=0, column=0, padx=5, pady=5)
#--Edit Button
Edit = Button(frame, text='Edit Title', font=('Calibri', 10), borderwidth=2,
              bg="#8FBBFF", command=edit).grid(row=0, column=1, padx=5, pady=5)
#--Add Button
Add = Button(frame, text='Add New', font=('Calibri', 10), borderwidth=2,
              bg="#FFE652", command=add).grid(row=0, column=2, padx=5, pady=5)
#--Delete Button
Del = Button(frame, text='Delete', font=('Calibri', 10), borderwidth=2,
              bg="#ef6359", command=delete).grid(row=0, column=3, padx=5, pady=5)

footer1 = Label(root, text= 'Creator: ' + '©' + author, bg='#9fc5e8', font=('Comic Sans MS', 10, BOLD))
footer1.pack(padx=5, pady=5, side=RIGHT)
footer2 = Label(root, text=appName + ' ' + version, bg='#9fc5e8', font=('Comic Sans MS', 10))
footer2.pack(padx=5, pady=5, side=LEFT)
root.mainloop()
