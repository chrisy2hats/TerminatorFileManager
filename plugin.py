from terminatorlib import plugin, config
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from subprocess import Popen

AVAILABLE = ['TerminatorFileManager']

class TerminatorFileManager(plugin.MenuItem):
  capabilities = ['terminal_menu']

  def __init__(self):
    self.plugin_name = self.__class__.__name__
    self.pwd = os.path.expanduser("~")

  # This function is called whenever the user right clicks within Terminator
  # The function should set the value of pwd and add the option to the menu that appears when the user right clicks
  def callback(self, menuitems, menu, terminal):
    self.pwd = terminal.get_cwd()
    self.add_submenu(menu, (f"Open {self.pwd} in file manager"), terminal)

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
    # Spawn the user's default program for handling directory (their file manager) as a separate process'
    Popen(["xdg-open", self.pwd])
