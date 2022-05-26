import paramiko
import tkinter as tk
from tkinter import *
#import pygame |- not required in latest version. Keeping code for in case. 
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("608x555")
root.title("Admin Tool")
#Background image for menus
image2 = PhotoImage(file = "image1.png")

#Root menu image & pygame initializer
label1 = Label(root, image = image2)
label1.place(x=0,y=0)
root.configure(bg='black')
#pygame.mixer.init() |- not required in latest version. Keeping code for in case. 

#Root Interface
Label1 = tk.Label(root, text="Enter IP Address:", font="Arial", fg="black")
Label1.place(x=185,y=88,width=210,height=30)
TheBox1 = tk.Entry(root, textvariable='', font="Arial")
TheBox1.place(x=200,y=120,width=180,height=30)


#Credential boxes Security
Userlabel = tk.Label(root, text='Username', font="Arial", fg="black")
Userlabel.place(x=3,y=465, height=30)
Userbox = tk.Entry(root, textvariable='', font="Arial")
Userbox.place(x=90,y=465,width=180,height=30)
Passlabel = tk.Label(root, text='Password', font="Arial", fg="black")
Passlabel.place(x=3,y=500, height=30)
Passbox = tk.Entry(root, textvariable='', font="Arial")
Passbox.place(x=90,y=500,width=180,height=30)

# Quickfix
def CpeCommands():
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

#Destroy codes
def FireCancel():
	advfire.destroy()

def SecDestroy():
	SecMen2.destroy()

def masqmenudestroy():
	masqconfirmtop.destroy()

def RootMenuDestroy():
	global Root2Menu
	Root2Menu.destroy()

def PortknockDestroy():
	global portknockconfirm
	confirmport.destroy()

def ScriptMenDestroy():
	ScriptingMenu.destroy()

def HelpDestroy():
	Helpmen2.destroy()

#Masquerade setup commands
def masqRemoval():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(TheBox1.get(), username=Userbox.get(), password=Passbox.get())
	stdin, stdout, stderr = Handler.exec_command('ip firewall nat remove [find action=masquerade]')
	Handler.close()

def MasqSetup():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(TheBox1.get(), username=Userbox.get(), password=Passbox.get())
	stdin, stdout, stderr = Handler.exec_command('ip firewall nat add action=masquerade chain=srcnat')
	Handler.close()

#Nat firewall menu sub-content and confirmation
def MasqsetupConfirm():
	global masqconfirmtop
	masqconfirmtop = tk.Toplevel(root)
	masqconfirmtop.geometry("497x499")
	masqconfirmtop.title("Masquerade Fix")
	masqconfirmtop.configure(bg="black")
	masqconfirmtoplabel2 = Label(masqconfirmtop, image = image2)
	masqconfirmtoplabel2.place(x=0,y=0)
	masqconfirmlabel = tk.Label(masqconfirmtop, text="[Options:]", fg="black", font="Arial")
	masqconfirmlabel.place(x=50,y=35)
	masqconfirmexit = tk.Button(masqconfirmtop, text="Back", font="Arial", fg="red", command=masqmenudestroy)
	masqconfirmexit.place(x=50,y=155,width=110,height=30)
	masqremove = tk.Button(masqconfirmtop, text="Remove Masquerade",fg="green",font="Arial",command=masqRemoval)
	masqremove.place(x=50,y=75,width=165,height=30)
	masqcreate = tk.Button(masqconfirmtop, text="Add Masquerade", fg="green",font="Arial", command=MasqSetup)
	masqcreate.place(x=50,y=115,width=165,height=30)
	masqtoIP = tk.Button(masqconfirmtop, text="Masquerade Specific IP", fg="black", font="Airal")
	masqtoIP.place(x=50,y=155,width=165,height=30)

#Scripting command (Experimental)
def startScripting():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(TheBox1.get(), username=Userbox.get(), password=Passbox.get())
	stdin, stdout, stderr = Handler.exec_command(TheBox2.get())
	Handler.close()

#Scripting function (Experimental)
def ScriptExp():
	global ScriptingMenu
	ScriptingMenu = tk.Toplevel(root)
	ScriptingMenu.geometry("718x537")
	ScriptingMenu.title("Scripting Menu")
	ScriptingMenu.configure(bg="black")
	Scriptinglabel = Label(ScriptingMenu, image = image2)
	Scriptinglabel.place(x=0,y=0)
	TheBox2 = tk.Entry(ScriptingMenu, textvariable='', font="Arial")
	TheBox2.place(x=150,y=120,width=300,height=30)
	ScriptButton = tk.Button(ScriptingMenu, text='Run Script', font='Arial',fg="black", command=startScripting)
	ScriptButton.place(x=200,y=160,width=180,height=30)
	ScriptExitbutton = tk.Button(ScriptingMenu, text='back', font='Arial',fg="red", command=ScriptMenDestroy)
	ScriptExitbutton.place(x=200,y=200, width=180, height=30)


#Nat firewall menu content
def AdvancedFirewall():
	global advfire
	advfire = tk.Toplevel(root)
	advfire.geometry("560x570")
	advfire.title("Firewalls")
	advfire.configure(bg="black")
	advfireLabel2 = Label(advfire, image = image2)
	advfireLabel2.place(x=0,y=0)
	Masquerade = tk.Button(advfire, text="Masquerade",font="Arial",fg="black", command=MasqsetupConfirm)
	Masquerade.place(x=50,y=200,width=250,height=30)	
	PortSec = tk.Button(advfire, text="Security",fg="black", command=SecurityA, font="Arial")
	PortSec.place(x=50,y=240,width=250,height=30)		
	advFireExit = tk.Button(advfire, text="Back", font="Arial", fg="red", command=FireCancel)
	advFireExit.place(x=50,y=280,width=70,height=30)

#Security Menu commands
def Secportknockset():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(TheBox1.get(), username=Userbox.get(), password=Passbox.get())
	stdin, stdout, stderr = Handler.exec_command('ip firewall address-list add list=Temporary')
	stdin, stdout, stderr = Handler.exec_command('ip firewall address-list add list=Secured')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=add-src-to-address-list address-list=Temporary address-list-timeout=25s chain=input comment="Temp Auth" disabled=yes dst-port=4444 protocol=tcp')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=add-src-to-address-list address-list=Secured address-list-timeout=6h chain=input comment="Move to Secured" disabled=yes dst-port=4443 protocol=tcp src-address-list=Temporary')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=accept chain=input comment="Accept Connection Secured" disabled=yes src-address-list=Secured')
	stdin, stdout, stderr = Handler.exec_command('ip firewall filter add action=drop chain=input comment="Drop All - Do not activate" disabled=yes')	
	Handler.close()	

#Portknock Menu
def Portknockconf():
	confirmport = tk.Toplevel(root)
	confirmport.geometry("460x200")
	prtknckconf = tk.Label(confirmport,font="Arial", text="The portknocker will be added and disabled by default.\n\nAre you sure you would like to continue?")
	prtknckconf.place(x=50,y=10)
	portknockconfirm = tk.Button(confirmport, text="Continue", font="Arial", fg="green", command=Secportknockset)
	portknockconfirm.place(x=150,y=100,width=70,height=30)
	portknockconfirm2exit = tk.Button(confirmport, text="Cancel", font="Arial", fg="red", command=PortknockDestroy)
	portknockconfirm2exit.place(x=235,y=100,width=70,height=30)

#Service restrict command
def SecserviceRestrict():
	Handler = paramiko.SSHClient()
	Handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	Handler.connect(TheBox1.get(), username=Userbox.get(), password=Passbox.get())
	stdin, stdout, stderr = Handler.exec_command('ip service set telnet address=10.0.0.0/8,165.165.128.127,165.165.128.128,192.168.0.0/16,196.25.88.226')
	stdin, stdout, stderr = Handler.exec_command('ip service set ftp address=10.0.0.0/8')
	stdin, stdout, stderr = Handler.exec_command('ip service set www address=10.0.0.0/8')
	stdin, stdout, stderr = Handler.exec_command('ip service set api address=10.0.0.0/8')
	stdin, stdout, stderr = Handler.exec_command('ip service set winbox address=10.0.0.0/8,165.165.128.127,165.165.128.128,192.168.0.0/16,196.25.88.226')
	stdin, stdout, stderr = Handler.exec_command('ip service set api-ssl address=10.0.0.0/8')
	Handler.close()

#PortForward command set
#def PortforwardCommand():


#Port forward menu in SecurityA
#def portfmenu1():
#	global portfport
#	global portfIP
#	portFMenu2 = tk.Toplevel(root)
#	portFMenu2.geometry("800x800")
#	portFMenu2.title("Port Forward")
#	portFMenu2label = Label(portFMenu2, image = image6)
#	portFMenu2label.place(x=0,y=0)
#	PortfLabel1 = tk.Label(portFMenu2, text="IP to port to:", font="Arial", fg="black")
#	PortfLabel1.place(x=,y=,height=30)
#	portfEntry1 = tk.Entry(portFMenu2, textvariable="", font="Arial")
#	portfEntry1.place(x=,y=,width=,height=)
#	PortFLabel2 = tk.Label(portFMenu2, text="Port to use:", font="Arial", fg="black")
#	PortFLabel2.place(x=,y=,height=30)
#	portfEntry2 = tk.Entry(portFMenu2, textvariable="", font="Arial")
#	portfEntry2.place(x=,y=,width=,height=)


#Security menu (Service restriction & port knocking)
def SecurityA():
	global SecMen2
	SecMen2 = tk.Toplevel(root)
	SecMen2.geometry("405x470")
	SecMen2.title("Security")
	SecMen2Label = Label(SecMen2, image = image2)
	SecMen2Label.place(x=0,y=0)
	RestrictServices = tk.Button(SecMen2, text="Service Restriction", fg="green",font="Arial", command=SecserviceRestrict)
	RestrictServices.place(x=15,y=200,width=150,height=30)
	PortKnockset = tk.Button(SecMen2, text="Port Knocker", font="Arial", command=Portknockconf)
	PortKnockset.place(x=15,y=240,width=150,height=30)
#	PortFmenu = tk.Button(SecMen2, text="Port Forwards", font="Arial", command=portfmenu1)
#	PortFmenu.place(x=15,y=280,width=150,height=30)	
	SecMenExit = tk.Button(SecMen2, text="Back", font="Arial", fg="red", command=SecDestroy)
	SecMenExit.place(x=15,y=280,width=150,height=30)

#Help Menu (information on tool)
def HelpMenuMain():
	global Helpmen2
	Helpmen2 = tk.Toplevel(root)
	Helpmen2.geometry("568x710")
	Helpmen2.title("Help")
	Helpmen2label = Label(Helpmen2, image = image2)
	Helpmen2label.place(x=0,y=0)
	HelpLabel2 = Label(Helpmen2, text="")
	HelpLabel2.place(x=0,y=375,width=568)
	Helpback = tk.Button(Helpmen2, text="back", fg="red", font="Arial", command=HelpDestroy)
	Helpback.place(x=2,y=2,width=180,height=30)
#Root menu 2 
def root2in():
	Root2Menu = tk.Toplevel(root)
	Root2Menu.geometry("900x675")
	Root2Menu.title("Menu")
	Root2label = Label(Root2Menu, image = image2)
	Root2label.place(x=0,y=0)
	#Scripting menu main page
	Portforwards = tk.Button(Root2Menu, text="Scripting",fg="Black", font="Arial", command=ScriptExp)
	Portforwards.place(x=150,y=580,width=180,height=30)
	#Quickfix button inside Root2in
	QuickfixButton = tk.Button(Root2Menu, text="Quickfix", font="Arial", fg="green", command=CpeCommands)
	QuickfixButton.place(x=150,y=500,width=180,height=30)
	#Firewall advanced menu button inside Root2in
	FirewallAdv = tk.Button(Root2Menu, text="Firewall Rules", fg="Black" ,font='Arial', command=AdvancedFirewall)
	FirewallAdv.place(x=150,y=540,width=180,height=30)
	#Help menu command in Root2in
	HelpMen1 = tk.Button(Root2Menu, text="Help", fg="black", font="Arial", command=HelpMenuMain)
	HelpMen1.place(x=350, y=580, width=180, height=30)
	
#Root2in button
NextMenu = tk.Button(root, text="Get started", font="Arial", fg="black", command=root2in)
NextMenu.place(x=200,y=158,width=180,height=30)

class TheBox:
	def __init__(self, TheBox1, TheBox2, userbox, passbox):
		self.TheBox1 = TheBox1
		self.TheBox2 = TheBox2
		self.Userbox = Userbox
		self.Passbox = Passbox
#		self.portfIP = portfIP	
#		self.portfport = portfport	

root.mainloop()
