 //Full screen map view 
 var mapId= document.getElementById('map');
 function fullScreenView(){
    if(document.fullscreenElement){
         document.exitFullscreen()
    }else { 
        mapId.requestFullscreen();

    }
     
    
 }


//Leaflet browser print function
L.control.browserPrint({position:'topright'}).addTo(map);

 //Leaflet search
 L.Control.geocoder().addTo(map);

  //Zoom to layer
  $('.zoom-to-layer').click(function(){
    map.setView([-34.6131, -58.3772],7)

})

// Map measurement

L.control.measure({
    primaryLengthUnit: 'kilometer',
    secondaryLengthUnit:'meter',
    primaryAreaUnit:'sqmeters',
    secondaryAreaUnit:undefined

}).addTo(map);

