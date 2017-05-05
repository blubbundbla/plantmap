---
layout: page
title: About
permalink: /about/
---

## About the PlantMap

The plantmap is a tool to show images of plants at the location of their occurence on a map, currently in a very early stage. Additional information to the plants can also be shown. I came up with the idea for this map on my bicycle in Latin America. While I was traveling, I was often taking pictures of plants along the way. I thought it would be interesting not only to show them, but also the locations where I found the plants.

As next steps, a possibility to search for plants and further information per plant should be included. 


## Tools used for the Plantmap

Plantmap uses Google Maps API v3 to display all the information and create interactivity. The dataset of plants, location and information is automatically generated using a python script. 
To generate location information, the script reads the EXIF Tag information of images. If these do not contain GPS coordinates, it either uses the time of the image to extract location from GPS tracks I generated while cycling or it correlates them to GPS information of other images, that were taken in the same minute. 
Plant identification information is processed by the script based on tags that have to be manually created, using common gallery programs. If a
plant name is available, additional information is requested automatically from the [tropicos](www.tropicos.org) database and included.

Currently, everything (except hosting) is done using only an Android 5 device and [Termux](https://termux.com). 

 
## About me
 
I am a young botanist who travels by bicycle in Southern America at the moment. I enjoy the flora which I can discover every day. Being on the road the environment changes so fast, that every single day there are new plants to discover. Luckily, with the speed of the bike you can discover a lot. I came up with the idea of this website to share the fascinating plant world I discover.