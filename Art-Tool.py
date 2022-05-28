#------------------------------------------------------------------------------------------------------------------------------------------------------
#Import required libraries
import paramiko
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Root menu configuration (fonts, backgrounds and colours)
root = Tk()
root.title('test')
root.geometry("400x200")
Backdrop = PhotoImage(file = "image1.png")
label1 = Label(root, image = Backdrop)
label1.place(x=0,y=0)
root.configure(bg='black')

font1 = "Arial"
fg1Red = "red"
fg2Green = "green"
fg3Black = "black"
fg4Blue = "blue"
fg5White = "white"
fg6Grey = "Light Grey"

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Command list to destroy current menu
def FirewallMenuExit():
	advfire.destroy()

def SecurityMenuExit():
	SecMen2.destroy()

def MasqueradeMenuExit():
	MasqueradeMenuToplevel.destroy()

def ScriptingMenuExit():
	ScriptingMenuToplevel.destroy()

def HelpMenuExit():
	Helpmen2.destroy()

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Command list starts here - list of all the commands in the code in order.
def QuickfixCommand():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(TheBox1.get(), username=Userbox.get(), password=Passbox.get())
	stdin, stdout, stderr = Handler.exec_command('ip service set ftp disabled=yes')
	stdin, stdout, stderr = Handler.exec_command('ip service set api disabled=yes')
	stdin, stdout, stderr = Handler.exec_command('ip service set api-ssl disabled=yes')
	stdin, stdout, stderr = Handler.exec_command('ip dns set allow-remote-requests=yes')
	stdin, stdout, stderr = Handler.exec_command('system ntp client set enabled=yes primary-ntp=196.4.160.4')
	stdin, stdout, stderr = Handler.exec_command('ip socks set enabled=no')
	stdin, stdout, stderr = Handler.exec_command('ip dns cache flush')
	Handler.close()

def MasqueradeMenu():
	global MasqueradeMenuToplevel
	MasqueradeMenuToplevel = tk.Toplevel(root)
	MasqueradeMenuToplevel.geometry("400x200")
	MasqueradeMenuToplevel.title("Masquerade Menu")
	MasqueradeMenuToplevel.configure(bg=fg3Black)
	MasqueradeMenuLabel1 = Label(MasqueradeMenuToplevel, image = Backdrop)
	MasqueradeMenuLabel1.place(x=0,y=0)
	MasqueradeMenuLabel2 = tk.Label(MasqueradeMenuToplevel, text="Options:", fg=fg5White, font=font1, bg=fg3Black)
	MasqueradeMenuLabel2.place(x=5,y=10,width=100,height=30)
	MasqueradeMenuExitButton = tk.Button(MasqueradeMenuToplevel, text="Back", font=font1, fg=fg1Red, command=MasqueradeMenuExit)
	MasqueradeMenuExitButton.place(x=250,y=10,width=150,height=30)
	RemoveMasquerade = tk.Button(MasqueradeMenuToplevel, text="Remove Masquerade", fg=fg3Black, font=font1, bg=fg6Grey)
	RemoveMasquerade.place(x=5,y=50,width=160,height=30)
	AddMasquerade = tk.Button(MasqueradeMenuToplevel, text="Add Masquerade", fg=fg3Black, font=font1, bg=fg6Grey)
	AddMasquerade.place(x=5,y=80,width=160,height=30)

def SendScript():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(TheBox1.get(), username=UsernameEntryBox.get(), password=PasswordEntryBox.get())
	stdin, stdout, stderr = Handler.exec_command(ScriptEntryBox.get())
	Handler.close()

def ScriptingMenu():
	global ScriptingMenuToplevel
	ScriptingMenuToplevel = tk.Toplevel(root)
	ScriptingMenuToplevel.geometry("614x335")
	ScriptingMenuToplevel.title("Scripting Menu")
	ScriptingMenuToplevel.configure(bg=fg3Black)
	Scriptinglabel = Label(ScriptingMenuToplevel, image = Backdrop)
	Scriptinglabel.place(x=0,y=0)
	ScriptEntryBox = tk.Entry(ScriptingMenuToplevel, textvariable='', font=font1)
	ScriptEntryBox.place(x=150,y=120,width=300,height=30)
	ScriptButton = tk.Button(ScriptingMenuToplevel, text='Run Script', font='Arial',fg=fg3Black, command=SendScript)
	ScriptButton.place(x=200,y=160,width=180,height=30)
	ScriptExitbutton = tk.Button(ScriptingMenuToplevel, text='back', font='Arial',fg=fg1Red, command=ScriptingMenuExit)
	ScriptExitbutton.place(x=200,y=200, width=180, height=30)

#------------------------------------------------------------------------------------------------------------------------------------------------------
def MainCommand(event):
	if clicked.get() == "Quickfix":
		QuickfixCommand()
	elif clicked.get() == "Masquerade":
		MasqueradeMenu()
	elif clicked.get() == "Security":
		SecurityMenu()
	elif clicked.get() == "Scripting":
		ScriptingMenu()

#Options for the tool (Command set)
options = [
"Quickfix",
"Masquerade",
"Security",
"Scripting",
]

#Clicked variable for the dropdown box
clicked = StringVar()
clicked.set("Choose Option")

#Username label and entry field for authentication to target
UsernameLabel = tk.Button(root, text="Username:", font=font1, fg=fg5White, bg=fg3Black)
UsernameLabel.place(x=5,y=10,width=150,height=30)
UsernameEntryBox = tk.Entry(root, textvariable="", font=font1, fg=fg3Black, bg=fg6Grey)
UsernameEntryBox.place(x=5,y=40,width=150,height=30)

#Password label and entry field for authentication to target
PasswordLabel = tk.Button(root, text="Password:", font=font1, fg=fg5White, bg=fg3Black)
PasswordLabel.place(x=5,y=70,width=150,height=30)
PasswordEntryBox = tk.Entry(root, textvariable="", font=font1, fg=fg3Black, bg=fg6Grey)
PasswordEntryBox.place(x=5,y=100,width=150,height=30)

drop = OptionMenu(root, clicked, *options, command=MainCommand)
drop.place(x=250,y=10,width=150,height=30)

class TheBox:
	def __init__(self, IPEntryBox, ScriptEntryBox, UsernameEntryBox, PasswordEntryBox):
		self.IPEntryBox = IPEntryBox
		self.ScriptEntryBox = ScriptEntryBox
		self.UsernameEntryBox = UsernameEntryBox
		self.PasswordEntryBox = PasswordEntryBox
#		self.SNTPIP = SNTPIP
#		self.MasqueradeIP = MasqueradeIP
#		self.ServiceRestrictionAddIP = ServiceRestrictionAddIP

root.mainloop()
