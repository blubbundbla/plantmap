---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
---
<div>
<!--include map
-->
    <div id="map" style="width:95%; height:500px !important"></div>
   
    <script type="text/javascript">

var map;


function initMap() {
var location = [

{% include mapmarker.csv %}

  ];

var center = new google.maps.LatLng(-43.4419, -70.1419);
var options = {
  'zoom': 4,
  'center': center,
  'mapTypeId': google.maps.MapTypeId.ROADMAP
};

var map = new google.maps.Map(document.getElementById("map"), options);

       
var markers = [];
var infowindow = null
     infowindow = new google.maps.InfoWindow({

       //content: info
           }); 
           
          
for (var i = 0; i < location.length; i++) {
    //var infocontent='The address name'+location[i][0];
      
    var plantinfo='<p>'
   // var imagealign = <IMG BORDER="0" ALIGN="Left" SRC=location[i][0]>
   // for (var p = 0; p < location[i][4].length; p++) {
    taglist=location[i][4]
   if (taglist[0]==="no info yet"){
        	plantinfo=taglist
        	}
        	 else if ( taglist.length===2){
        	plantinfo= "<p> Gattung: " + taglist[1] +"</p>"+ " Art: " + taglist[0] }
        	
        	else if ( taglist.length===1){
        	plantinfo= "<p>" + taglist[0] +"</p>" 
        	}
        	
        	var picdate='<p>'+ "date of picture: " +location[i][5] 	+'<br />'
        	var picid=  "picture ID: " + location[i][0] 	+'</p>'
        	var picinfo = '<h3>Image information</h3>'+ picdate+picid
        	
        	
        	plantinfo='<p>'+plantinfo +'</p>'+ picinfo
         
           	
        	
  //}  
    
    //	var plantinfo =location[i][4][p]
    //	plantinfo = plantinfo+"<b>"+location[i][4][p]+"</b>"+', '
      
      
    //  }
  //  plantinfo = plantinfo.replace(/,\s*$/, ""); 
 //   plantinfo="<p>"+plantinfo+"</p>"
         var image= {
            url: location[i][3],
            scaledSize: new google.maps.Size(50, 50)
         }
 
 
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(location[i][1], location[i][2]),
            map: map,
            icon:  image,
            title: location[i][0],
           // info: imagealign+plantinfo
            info: '<div><IMG style="width:80%" BORDER="0" ALIGN="Left" SRC="'
                  +location[i][3]+'"></div>'+
                  '<div style="clear:left;">'+
            
                  '<h2>Plant information</h2>'+ '</div>'+
                  '<div>'+'</p>'+'</div>'+
                  plantinfo
                  //'<div style="width: 650px; height 450px">
            
            
            
        });
//console.log('<IMG BORDER="0" ALIGN="Left" SRC="'+location[i][3]+'">'+plantinfo
//            );

        
        
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
        // center on marker
        map.setCenter(marker.getPosition());
        // open the infowindow
        infowindow.setContent(this.info);
        infowindow.open(map, this);
        }
        })(marker, i));
        
        markers.push(marker);  //push individual marker onto global array
        
        }


var mcOptions = {gridSize: 50, maxZoom: 12};


var markerCluster = new MarkerClusterer(map, markers, mcOptions, {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

};


    
  
//function AutoCenter() { 
//  Create a new viewpoint bound 
//var bounds = new google.maps.LatLngBounds(); 
//  Go through each... 
//$.each(markers, function (index, marker) { 
//bounds.extend(marker.position); 
//}); 
//  Fit these bounds to the map 
//map.fitBounds(bounds); 
//}
  
  
    


  </script>
   
  
  
  <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
  </script>
  
  <!-- mit key für plantmap-->
 <script async defer
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCUtGESjuDKUpyhlmag9CbYupSnbVYqWz8 	
&callback=initMap">
  </script>
  
 </div>