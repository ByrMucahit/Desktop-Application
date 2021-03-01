
import eel,csv,json

# Write @eel.expose before a python

eel.init('web')
eel.adding('Running javascript function from python side ')

@eel.expose
def hellopython(r):
    print(r)

#my_options = {
 #   'mode': 'chrome-app',
  #  'host': 'localhost',
   # 'port': 8089,
    #'chromeFlags': ['--start-fullscreen']
#}

eel.start('main.html')