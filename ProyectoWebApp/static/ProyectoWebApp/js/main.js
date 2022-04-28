 //map class initialize
 var map = L.map('map').setView([ -34.6131, -58.3772], 5);
 map.zoomControl.setPosition('topright');
      
 //adding osm tileserver
 var osm= L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
 }).addTo(map);

 var watercolormap = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
 attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
 subdomains: 'abcd',
 minZoom: 1,
 maxZoom: 16,
 ext: 'jpg'
 });

 var esrimap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
 attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'

 });

 var opentopomap = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
 maxZoom: 17,
 attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
 });

 var esritopomap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}', {
 attribution: 'Tiles &copy; Esri &mdash; Source: USGS, Esri, TANA, DeLorme, and NPS',
 maxZoom: 13
 });

 //adding marken in the center of the map
 L.marker([-34.6131, -58.3772]).addTo(map)
     .bindPopup('BIENVENIDO!')
     .openPopup();

 //add scale 

 L.control.scale().addTo(map)

//Map coordinate display
 map.on('mousemove', function (e) {
     
     $('.coordinate').html(`Lat: ${e.latlng.lat} Long: ${e.latlng.lng}`)
 })

 //Geojson load
 var marker= L.markerClusterGroup();
 var eeuu =L.geoJSON(data, {
     onEachFeature:function(feature,layer) {
         layer.bindPopup(feature.properties.name)
     }
 });
 eeuu.addTo(marker);
 marker.addTo(map);
 

 //Geojson load 2nd example
 var marker2= L.markerClusterGroup();
 var data2= L.geoJson(data2,{
     onEachFeature:function(feature,layer) {
         layer.bindPopup(feature.properties.name)
     }
 })
 data2.addTo(marker2);
 marker2.addTo(map);



 //Leaflet layer control
 var baseMaps= {
     'OSM':osm,
     'Water Color Map':watercolormap,
     'Esri imagery Map':esrimap,
     'Topografic map':opentopomap,
     'World terrain':esritopomap,

 }

 var overlayMaps= {

     'GeoJSON Balnearios TESIS': marker2,
     'GeoJSON Polygons EEUU':marker,
 }

 L.control.layers(baseMaps,overlayMaps, {collapsed: false, position:'topleft'}).addTo(map);


