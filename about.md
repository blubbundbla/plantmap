---
layout: page
title: About
permalink: /about/
---

##About the Plantmap

The plantmap is a page to show plant images on a map. Based on gps information the pictures can be placed on the map. Additional information are displayed in the corresponding infowindows.


##About the technic used

To make the plantmap I used several python packages and the google api. The pictures come from different cameras, only one has the option of direct gps-coding. The other pictures got gps information based on gpx tracks. All scripts run on Android 5 using [termux](https://termux.com). A automated [tropicos](www.tropicos.org) request is used to get more information about the identified species. Finally, the google map api is used to place the pictures on the map and make the infowindows.


Python packages used
 * exifread (instead of Pillow which does not run on Android 5
 * subprocess
 * os
 * urllib.request
 * xml.etree.ElementTree
 *
 
##About me
 
I am a young botanist who travels by bicycle in Souhern America at the moment. I enjoy the flora which I can discover every day. The environment changes so fast, that every single day there are new plants to discover. Luckily, with the speed of the bike you can discover a lot. All the plants shown I found on my way cycling and there are even more to find. I came up with the idea of this website, to combine my love to understand how biodiversity is composed and for problem solving with the plants I discovered. 

In the future I plan to add more pictures, information, and a search option.