##geotagpictures

###
import subprocess
import os
###

verzeichnis="/data/data/com.termux/files/home/storage/shared/plantmap/images/plants/"

jpg_verzeichnis=verzeichnis+"neu/"
gps_verzeichnis=jpg_verzeichnis+"gps/"

 
f=open(verzeichnis+"plantmap-tag.csv",'r')

####test if filename-pic has no gps info, if it has move

	####
	 
jpgl=[]
for file in os.listdir(jpg_verzeichnis):
	   endung=os.path.basename(file)[-3:]
	   if(endung=="JPG"):
	       
	       #filename=file
	       jpgl+=[file]
 
 ###
 
 
for line in f:
				 #print(line)
				 line=line.replace('"','')
				 l2=line.split(',')
				 #print(l2)
				 l3=l2[3:11]
		 
				 picname=l2[1]
				 #print(l3)
				 if picname in jpgl:
								 print(l3[0])
				 #fpr fotos mit gps
								 if l3[0]=="" or l3[0]=="GPS Latitude" or l3[0]=="16777215/1":
												 #print(line)
												 gps=False
								 else:
												 #print(line)
												 gps=True
			 
			 
								 if gps==True:
				 
				 ###move jpg
												 picname2=jpg_verzeichnis+picname
												 picname3=gps_verzeichnis+picname
								 
												 subprocess.run(['mv', picname2, picname3 ])				
								 ###move corresponding xmp
												 xmpname=picname.replace('JPG','xmp')
												 xmpname2=jpg_verzeichnis+xmpname
												 xmpname3=gps_verzeichnis+xmpname
												 
												 subprocess.run(['mv', xmpname2, xmpname3 ])				
										
								
###get list of gpx-filenames
track_verzeichnis="/data/data/com.termux/files/home/storage/shared/latinamerica.bike/tracks/"

gpxl=[]
for file in os.listdir(track_verzeichnis):
				endung=os.path.basename(file)[-3:]
				if(endung=="gpx"):
								
								#filename=file
								gpxl+=[file]
								
print(gpxl)
#gpxl=gpxl[67:]

###read info of gpx
for filename in gpxl:
				
				###!change to corresponding folder
				fn = track_verzeichnis+filename
				#~/storage/shared/latinamerica.bike/cg./"+filename
				print(filename)

				subprocess.run(["/data/data/com.termux/files/usr/bin/exiftool", "-geotag", fn, jpg_verzeichnis])
				
				
				
			