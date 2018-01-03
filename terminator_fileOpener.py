#!/usr/bin/python
from terminatorlib import plugin, config #Terminators library. This is not accessible when this program is run standalone.
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from subprocess import Popen #Used to run Bash commands from Python

AVAILABLE = ['TerminatorFileManager']

class TerminatorFileManager(plugin.MenuItem):
  capabilities = ['terminal_menu']

  def __init__(self):
    self.plugin_name = self.__class__.__name__
    self.globalPWD = "/home"

  #This function is called whenever the user right clicks within Terminator
  #The function should set the value of globalPWD and add the option to the menu that appears when the user right clicks
  def callback(self, menuitems, menu, terminal):
    pwd = terminal.terminator.pid_cwd(terminal.pid)
    self.globalPWD = pwd
    self.add_submenu(menu, ("Open "+self.globalPWD+" in file manager"), terminal)

  #Function to add the option to open in file manager to the list spawned by the user right clicking
  def add_submenu(self, submenu, name, terminal):
    #Create a new menu item
    menu = Gtk.MenuItem(name)

    #Set the function to call when the user clicks on the open in file manager option
    menu.connect("activate", self.on_click, terminal)

    #Append the new menu item to the right click menu
    submenu.append(menu)
    return menu

  #Function called when the user clicks open in file manager.
  def on_click(self, widget, event):
    #Popen runs the Bash command as a seperate process uncall the "call" function from the subprocess library
    Popen(["xdg-open",self.globalPWD])#xdg-open should open the users default program for opening a directory
