import os
from tinytag import TinyTag 
import argparse


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
	for fiNames in fileList:
		#checking if extension is in the list of format
		fiName= path+"\\" +fiNames
		ext = fiName.split('.')[-1]
		if ext in mFormat:
			try:
				musicCheck = "true"
				song = TinyTag.get(fiName)

				artist = str(song.artist)

				time = str(int(song.duration))

				title = str(song.title)

				#writing data
				
				fi.write("#EXTINF:"+time+","+artist+" - "+title+"\n")
				fi.write(fiName+"\n")
			except Exception as e:
				print("unable to add " + fiNames)
			
			
	fi.close()
	#if there isn't music delete playlist
	if musicCheck == "false":
		os.remove(m3uName)

def list_file(startpath):
	for path,dirName,fiList in os.walk(startpath):
		createPlayList(fiList,str(path))
	print("DONE")

parser = argparse.ArgumentParser(description="Crea Playlist in tutte le sottocartelle del percorso dato")
parser.add_argument("-p","--path", type=str, help="Percorso di partenza per creazione playlist")
args = parser.parse_args()
path = str(args.path)
if path == "None":
	print('Inserisci il percorso con -p "percorso" o --path "percorso"')
else:
	list_file(path)



