#!/usr/bin/python
import sys #TODO import only required functions from these libraries
import os
from terminatorlib import plugin, config
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from subprocess import call

AVAILABLE = ['TerminatorFileManager']

class TerminatorFileManager(plugin.MenuItem):
  capabilities = ['terminal_menu']

  def __init__(self):
    self.plugin_name = self.__class__.__name__

  def callback(self, menuitems, menu, terminal):
    pwd = terminal.terminator.pid_cwd(terminal.pid)
    self.add_submenu(menu, ("Open "+pwd+" in file manager"), terminal)

  def add_submenu(self, submenu, name, terminal):
    # create menu item
    menu = Gtk.MenuItem(name)

    # call on_click method while Clicking on menu item
    menu.connect("activate", self.on_click, terminal)

    # append menu item to context menu
    submenu.append(menu)
    return menu

  def on_click(self, widget, event):
    pwd = '/home' #Works
    # pwd = " " +terminal.terminator.pid_cwd(terminal.pid)
    # os.system(command) 
    call(["xdg-open",pwd])
