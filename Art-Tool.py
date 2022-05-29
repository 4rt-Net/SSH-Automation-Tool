#------------------------------------------------------------------------------------------------------------------------------------------------------
#Import required libraries
import paramiko
import tkinter as tk
from tkinter import *
from tkinter import ttk
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
	SecurityMenuTopLevel.destroy()

def SecurityRestrictMenuExit():
	SecurityRestrictIPToplevel.destroy()

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
	Handler.connect(targetIPAddress.get(), username=UsernameEntryBox.get(), password=PasswordEntryBox.get())
	stdin, stdout, stderr = Handler.exec_command('ip service set ftp disabled=yes')
	stdin, stdout, stderr = Handler.exec_command('ip service set api disabled=yes')
	stdin, stdout, stderr = Handler.exec_command('ip service set api-ssl disabled=yes')
	stdin, stdout, stderr = Handler.exec_command('ip dns set allow-remote-requests=yes')
	stdin, stdout, stderr = Handler.exec_command('system ntp client set enabled=yes primary-ntp=196.4.160.4')
	stdin, stdout, stderr = Handler.exec_command('ip socks set enabled=no')
	stdin, stdout, stderr = Handler.exec_command('ip dns cache flush')
	stdin, stdout, stderr = Handler.exec_command('ip proxy set enabled=no')
	Handler.close()

def SendScript():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(targetIPAddress.get(), username=UsernameEntryBox.get(), password=PasswordEntryBox.get())
	stdin, stdout, stderr = Handler.exec_command(ScriptEntryBox.get())
	Handler.close()

def SecurityPortKnocker():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(targetIPAddress.get(), username=UsernameEntryBox.get(), password=PasswordEntryBox.get())
	stdin, stdout, stderr = Handler.exec_command('ip firewall address-list add list=Temporary')
	stdin, stdout, stderr = Handler.exec_command('ip firewall address-list add list=Secured')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=add-src-to-address-list address-list=Temporary address-list-timeout=25s chain=input comment="Temp Auth" disabled=yes dst-port=4444 protocol=tcp')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=add-src-to-address-list address-list=Secured address-list-timeout=6h chain=input comment="Move to Secured" disabled=yes dst-port=4443 protocol=tcp src-address-list=Temporary')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=accept chain=input comment="Accept Connection Secured" disabled=yes src-address-list=Secured')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=drop chain=input comment="Drop All - Do not activate" disabled=yes')	
	Handler.close()	


def SecserviceRestrict():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(targetIPAddress.get(), username=UsernameEntryBox.get(), password=PasswordEntryBox.get())
	stdin, stdout, stderr = Handler.exec_command('ip service set telnet address='+RestrictionIP)
	stdin, stdout, stderr = Handler.exec_command('ip service set ftp address='+RestrictionIP)
	stdin, stdout, stderr = Handler.exec_command('ip service set www address='+RestrictionIP)
	stdin, stdout, stderr = Handler.exec_command('ip service set api address='+RestrictionIP)
	stdin, stdout, stderr = Handler.exec_command('ip service set winbox address='+RestrictionIP)
	stdin, stdout, stderr = Handler.exec_command('ip service set api-ssl address='+RestrictionIP)
	Handler.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Menus & Sub Menus (Not including root)
def SecurityRestrictIPMenu():
	global SecurityRestrictIPToplevel
	SecurityRestrictIPToplevel = tk.Toplevel(root)
	SecurityRestrictIPToplevel.geometry("400x200")
	SecurityRestrictIPToplevel.title("Security")
	SecurityRestrictIPlabel1 = Label(SecurityRestrictIPToplevel, image = Backdrop)
	SecurityRestrictIPlabel1.place(x=0,y=0)
	SecurityRestrictIPlabel2 = Label(SecurityRestrictIPToplevel, text="Enter Allowed IP Addresses: (Comma Seperated)", font=font1, fg=fg5White, bg=fg3Black)
	SecurityRestrictIPlabel2.place(x=5,y=10)
	RestrictionIP = tk.Entry(SecurityRestrictIPToplevel, textvariable="", font=font1, fg=fg3Black, bg=fg6Grey)
	RestrictionIP.place(x=5,y=50,width=200,height=30)
	SecurityRestrictIPButton = tk.Button(SecurityRestrictIPToplevel, text="Restrict", font=font1, fg=fg3Black, bg=fg6Grey, command=lambda:[SecserviceRestrict()][SecurityRestrictMenuExit()])
	SecurityRestrictIPButton.place(x=10,y=85,width=160,height=30)


def SecurityMenu():
	global SecurityMenuTopLevel
	SecurityMenuTopLevel = tk.Toplevel(root)
	SecurityMenuTopLevel.geometry("400x200")
	SecurityMenuTopLevel.title("Security")
	SecurityMenuLabel1 = Label(SecurityMenuTopLevel, image = Backdrop)
	SecurityMenuLabel1.place(x=0,y=0)
	SecurityMenuRestriction = tk.Button(SecurityMenuTopLevel, text="Service Restriction", fg=fg2Green,font=font1, command=SecurityRestrictIPMenu)
	SecurityMenuRestriction.place(x=5,y=50,width=150,height=30)
	SecurityMenuPortKnocking = tk.Button(SecurityMenuTopLevel, text="Port Knocker", font=font1, command=SecurityPortKnocker)
	SecurityMenuPortKnocking.place(x=5,y=80,width=150,height=30)
	SecMenExit = tk.Button(SecurityMenuTopLevel, text="Back", font=font1, fg=fg1Red, command=SecurityMenuExit)
	SecMenExit.place(x=250,y=10,width=150,height=30)

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
#Help menu command list and menu
def HelpMenu():
	global CHelpMenu
	global Helpdrop
	CHelpMenu = tk.Toplevel(root)
	CHelpMenu.geometry("400x200")
	CHelpMenu.title("Help Menu")
	CHelpMenu.configure(bg=fg3Black)
	HelpMLabel = Label(CHelpMenu, image = Backdrop)
	HelpMLabel.place(x=0,y=0)
	HelpMLabelOptions = tk.Label(CHelpMenu, text="Select an option to view information about its usage:", font=font1, fg=fg5White, bg=fg3Black)
	HelpMLabelOptions.place(x=15,y=50)

	#Combo box configuration (Drop down menu)
	Helpdrop = ttk.Combobox(CHelpMenu, value=options2)
	Helpdrop.current(0)
	Helpdrop.bind("<<ComboboxSelected>>", HelpCommand)
	Helpdrop.place(x=130,y=85,width=160,height=30)

def QuickfixHelp():
	QuickFixHelpMenu = tk.Toplevel(root)
	QuickFixHelpMenu.geometry("520x275")
	QuickFixHelpMenu.title("QuickFix Details")
	QuickFixHelpMenu.configure(bg=fg3Black)
	QuickFixBackground = Label(QuickFixHelpMenu, image = Backdrop)
	QuickFixBackground.place(x=0,y=0)
	QuickFixHelpLabel = tk.Label(QuickFixHelpMenu, fg=fg5White, bg=fg3Black,text="The Quickfix command can be used to fix common problems found while troubleshooting.\n\nCurrently the command does the following:\n\n- Disable FTP service\n- Disable API service\n- Disable API-SSL service\n- Enables DNS Allow Remote Requests\n- Flushes DNS Cache\n- Fixes SNTP IP address\n- Disables Socks if enabled\n- Disables Web Proxy\n\n\nNote:\nQuickfix can sometimes fail to execute fully\nThis happens because it pushes a large amount of commands to the routerboard simultaneously.\nIf the command throws an exception, just execute it again and it should execute properly.")
	QuickFixHelpLabel.place(x=1,y=1)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Main menu linked commands
def MainCommand(event):
	if drop.get() == "Quickfix":
		QuickfixCommand()
	elif drop.get() == "Masquerade":
		MasqueradeMenu()
	elif drop.get() == "Security":
		SecurityMenu()
	elif drop.get() == "Scripting":
		ScriptingMenu()
	elif drop.get() == "Help":
		HelpMenu()

def HelpCommand(event):
	if Helpdrop.get() == "Quickfix Details":
		QuickfixHelp()

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Options for the tool (Command set)
options2 = [
"Quickfix Details",
"Masquerade Usage",
"Security Usage",
"Scripting Usage",
]

options = [
"Quickfix",
"Masquerade",
"Security",
"Scripting",
"Help"
]

#Clicked variable for the dropdown box
#clicked = StringVar()
#clicked.set("Choose Option")

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

#IP address for target entry field and label
TargetIPLabel = tk.Button(root, text="Target IP:", font=font1, fg=fg5White, bg=fg3Black)
TargetIPLabel.place(x=5,y=150,width=150,height=30)
targetIPAddress = tk.Entry(root, textvariable="", font=font1, fg=fg3Black, bg=fg6Grey)
targetIPAddress.place(x=155,y=150,width=200,height=30)

#Combo box configuration (Drop down menu)
drop = ttk.Combobox(root, value=options)
drop.current(0)
drop.bind("<<ComboboxSelected>>", MainCommand)
drop.place(x=250,y=10,width=150,height=30)


class TheBox:
	def __init__(self,targetIPAddress ,ScriptEntryBox, UsernameEntryBox, PasswordEntryBox, RestrictionIP):
		self.ScriptEntryBox = ScriptEntryBox
		self.UsernameEntryBox = UsernameEntryBox
		self.PasswordEntryBox = PasswordEntryBox
		self.targetIPAddress = targetIPAddress
#		self.MasqueradeIP = MasqueradeIP
		self.RestrictionIP = RestrictionIP

root.mainloop()
