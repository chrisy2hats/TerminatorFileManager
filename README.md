# Terminator File Manager
[Terminator](https://gnome-terminator.org/) plugin to add an option to open the current directory in your default file manager

# Install
```
mkdir -p $HOME/.config/terminator/plugins/
mv plugin.py $HOME/.config/terminator/plugins/
```

# Enable
1. Start terminator
2. Click "Preferences"
3. Go to the "Plug-ins" tab
4. Check "TerminatorFileManager"
5. Restart terminator

Now when you right click on a terminator terminal it should have the option "Open /this/directory/ in file manager"
