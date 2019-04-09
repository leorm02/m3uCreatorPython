import os
from tinytag import TinyTag 


def createPlayList(fileList,path):
	#flag to check if music exists
	musicCheck = "false"
	#name of current directory
	cDirName = path.split('\\')[-1]
	#name that playlist must have
	m3uName = path +"\\" +cDirName+".m3u"
	#creating m3u file
	fi = open(m3uName,"w")
	#writing m3u header
	fi.write("#EXTM3U\n")
	#declaring music format to research
	mFormat = ["aac","m4a","wav","mp3","flac","wma"]
	for fiName in fileList:
		#checking if extension is in the list of format
		fiPath= path+"\\" +fiName
		ext = fiName.split('.')[-1]
		if ext in mFormat:
			try:
				#setting flag state true
				musicCheck = "true"
				#getting song name
				song = TinyTag.get(fiPath)
				#getting song artist
				artist = str(song.artist)
				#getting song duration
				time = str(int(song.duration))
				#getting song title
				title = str(song.title)
				#writing data on file
				fi.write("#EXTINF:"+time+","+artist+" - "+title+"\n + fiName+"\n)
			except Exception as e:
				print("unable to add " + fiName)	
	#file stream closing
	fi.close()
	#if there isn't music delete playlist file
	if musicCheck == "false":
		os.remove(m3uName)

def createPlaylist(startpath):
	for path,dirName,fiList in os.walk(startpath):
		createPlayList(fiList,str(path))
		print("DONE")
		
message = input('Inserisci "0" per creare le playlist in tutte le sottocartelle a partire dalla posizione di questo programma,\n Inserisci "1" per inserire un altro percorso:')
if message == "0":
	cDirPhat = str(os.getcwd())
else:
	cDirPhat = str(input("inserisci il percorso: "))
createPlaylist(cDirPhat)


