"""
Una implementaci�n m�s completa que raesimple.py. 
V�ase raesimple.py para m�s informaci�n.
"""

import android
import urllib2
import urllib
import time

# agregar funci�n que inserta lo necesario en html de rae y 
# tener la funcionalidad deseada

def busca_rae(termino):
    searchUrl = 'http://lema.rae.es/drae/srv/search?val=' \
		    + urllib.quote_plus(termino)
    response = urllib2.urlopen(searchUrl)
    html = response.read()
    # Llamar a la funcion que se agregara para acomodar html
    raeFileName = '/sdcard/doc/rae.html'
    fhtml = open(raeFileName, 'w')
    fhtml.write(html)
    fhtml.close()   

droid = android.Android()
ter = droid.dialogGetInput('Buscar', 'Ingrese palabra').result

if ter is not None and len(ter) > 0:
    droid.webViewShow(raeFileName)
else:
    droid.makeToast('Cancelado')
