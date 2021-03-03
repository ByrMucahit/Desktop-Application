
import eel

# Write @eel.expose before a python



@eel.expose
def hellopython(r):
    print(r)
    eel.show(r)

eel.init('web')
eel.start('main.html')