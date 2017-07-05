#Send remapped shortcut

def send(shortcut):
    keyboard.send_keys(shortcut)


def resolve(shortcut):
    windowClass = window.get_active_class()
    
    if windowClass == 'gnome-terminal-server.Gnome-terminal':
        return shortcut
      
    if shortcut == '<super>+q' and windowClass == 'chromium.Chromium':
        return '<alt>+<f4>'
        
    return shortcut.replace('<super>','<ctrl>')
    

send(resolve(shortcut))