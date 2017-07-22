#Send remapped shortcut

def send(shortcut):
    keyboard.send_keys(shortcut)


def resolve(shortcut):
    windowClass = window.get_active_class()
    
    if windowClass == 'gnome-terminal-server.Gnome-terminal':
        return shortcut
      
    if shortcut == '<super>+q':
       if windowClass == 'Focus-Proxy-Window.FocusProxy':
           # CLion and possible others Java apps 
           # lost <alt>+<f4> so we use custom shortcut for them
           return '<f10>'
       if windowClass == 'chromium.Chromium':
          return '<alt>+<f4>'
        
    return shortcut.replace('<super>','<ctrl>')
    

send(resolve(shortcut))