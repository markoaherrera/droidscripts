import android
import urllib2
import time

droid = android.Android()
termino = droid.dialogGetInput('Buscar', 'Ingrese palabra').result

if termino is not None and len(termino) > 0:
	searchUrl = 'http://lema.rae.es/drae/srv/search?val=' + termino
	response = urllib2.urlopen(searchUrl)
	html = response.read()
	raeFileName = '/sdcard/doc/rae.html'
	fhtml = open(raeFileName, 'w')
	fhtml.write(html)
	fhtml.close()
	droid.webViewShow(raeFileName)
	time.sleep(10)
else:
	droid.makeToast('Cancelado')
