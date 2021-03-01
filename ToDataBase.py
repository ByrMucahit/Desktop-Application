from __future__ import unicode_literals
import io
import eel 
import youtube_dl

eel.init('web')
eel.start('main.html')
@eel.expose
def toDataBase(data):
    print("Name", data['date'])
