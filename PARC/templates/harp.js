const map = new harp.MapView({
   canvas: document.getElementById('map'),
   theme: "https://unpkg.com/@here/harp-map-theme@latest/resources/berlin_tilezen_night_reduced.json",
});
map.setCameraGeolocationAndZoom(new harp.GeoCoordinates(1.278676, 103.850216),16);
const mapControls = new harp.MapControls(map);
const omvDataSource = new harp.OmvDataSource({
   baseUrl: "https://xyz.api.here.com/tiles/herebase.02",
   apiFormat: harp.APIFormat.XYZOMV,
   styleSetName: "tilezen",
   authenticationCode: 'YOUR-XYZ-TOKEN',
});
map.addDataSource(omvDataSource);
