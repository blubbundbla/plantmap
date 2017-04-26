# convert P1030570.JPG -resize 1024 -quality 80 P1030570.JPG


###
import subprocess
import os
###


###get list of image-filenames
image_verzeichnis="/data/data/com.termux/files/home/storage/shared/plantmap/images/plants/neu/"

l=[]
xmp=[]

for file in os.listdir(image_verzeichnis):
    endung=os.path.basename(file)[-3:]
    if(endung=="JPG"):
        
        filename=image_verzeichnis+file
        l+=[filename]

###read fikes
for filename in l:
				print(filename)
				#subprocess.run(["/data/data/com.termux/files/usr/bin/convert", filename, "-resize", "1024", "-quality", "80", filename], stdout=subprocess.PIPE)
				subprocess.run(["/data/data/com.termux/files/usr/bin/convert", filename, "-resize", "640", filename], stdout=subprocess.PIPE)

				#subprocess.run(["/data/data/com.termux/files/usr/bin/convert", filename, "-auto-orient", filename])
			