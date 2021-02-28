from __future__ import unicode_literals
import io
import eel 
import youtube_dl

eel.init('web')

@eel.expose
def toDataBase(data):
    print("Name", data['date'])
eel.start('web/index.html', size=(1000, 600))