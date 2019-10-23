This is a plugin for sublime text 3.  It lets you switch between the terminus terminal output panel and the current editor window.  

You also need to create a keybinding if you want this to work well.  To do that, go to Sublime Text -> Preferences -> Key Bindings and add this entry:


{
    "keys": ["option+tab"],
    "command": "panel_switch"
}
