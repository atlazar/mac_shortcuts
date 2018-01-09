import subprocess
import ast

result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.input-sources', 'xkb-options'], stdout=subprocess.PIPE)

if result.returncode != 0:
    exit(1)

xkbOptions = ast.literal_eval(result.stdout.decode('utf-8'))

swapOption = 'altwin:swap_lalt_lwin'
if swapOption in xkbOptions:
    xkbOptions.remove(swapOption)
else:
    xkbOptions.append(swapOption)

subprocess.run(['gsettings', 'set', 'org.gnome.desktop.input-sources', 'xkb-options', str(xkbOptions)])
