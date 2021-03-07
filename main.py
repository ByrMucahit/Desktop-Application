
import eel
import json

# Write @eel.expose before a python

@eel.expose
def hellopython(text):
    print(text["Kullanıcılar"].get("1id"))


   

eel.init('web')
eel.start('main.html')