from terminatorlib import plugin, config
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from subprocess import Popen, check_output

AVAILABLE = ['TerminatorFileManager']


def _get_filemanager_name() -> str:
  command = ["xdg-mime", "query", "default", "inode/directory"]

  try:
    # Returns a fully qualified application name like "org.kde.dolphin.desktop"
    return check_output(command).decode().split(".")[-2].capitalize()

  # If xdg-mime doesn't exist in the user's path then FileNotFoundError is thrown
  except FileNotFoundError:
     return "file manager"

class TerminatorFileManager(plugin.MenuItem):
  capabilities = ['terminal_menu']

  def __init__(self):
    self.plugin_name = self.__class__.__name__
    self.pwd = os.path.expanduser("~")
    self.filemanager_name =  _get_filemanager_name()

  # This function is called whenever the user right clicks within Terminator
  # The function should set the value of pwd and add the option to the menu that appears when the user right clicks
  def callback(self, menuitems, menu, terminal):
    self.pwd = terminal.get_cwd()

    homedir = os.path.expanduser("~")
    shortPWD = self.pwd.replace(homedir, "~")
    if self.pwd == homedir:
        shortPWD = "home"

    prompt = f"Open {shortPWD} in {self.filemanager_name}"
    self.add_submenu(menu, prompt, terminal)

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
