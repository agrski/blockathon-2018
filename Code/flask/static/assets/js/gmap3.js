
//writes function which computes centre of these places



function initMap() {



var citymap = {
  place_one: {
    center: {lat: -9.38294817, lng: 148.40222161},
    population: 27148,
    label:'1',
    id:1
  },
  place_two: {
    center: {lat: -9.10101191, lng: 147.71008294},
    population: 84058,
    label:'2',
    id:2

  }
};




      //we want initMap to take values from the ledger


        // Create the map inside the div container with id map
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 8,
          center: {lat: -8.92197506, lng: 147.946289},
          mapTypeId: 'terrain',
          styles: [
                      {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
                      {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
                      {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
                      {
                        featureType: 'administrative.locality',
                        elementType: 'labels.text.fill',
                        stylers: [{color: '#d59563'}]
                      },
                      {
                        featureType: 'poi',
                        elementType: 'labels.text.fill',
                        stylers: [{color: '#d59563'}]
                      },
                      {
                        featureType: 'poi.park',
                        elementType: 'geometry',
                        stylers: [{color: '#263c3f'}]
                      },
                      {
                        featureType: 'poi.park',
                        elementType: 'labels.text.fill',
                        stylers: [{color: '#6b9a76'}]
                      },
                      {
                        featureType: 'road',
                        elementType: 'geometry',
                        stylers: [{color: '#38414e'}]
                      },
                      {
                        featureType: 'road',
                        elementType: 'geometry.stroke',
                        stylers: [{color: '#212a37'}]
                      },
                      {
                        featureType: 'road',
                        elementType: 'labels.text.fill',
                        stylers: [{color: '#9ca5b3'}]
                      },
                      {
                        featureType: 'road.highway',
                        elementType: 'geometry',
                        stylers: [{color: '#746855'}]
                      },
                      {
                        featureType: 'road.highway',
                        elementType: 'geometry.stroke',
                        stylers: [{color: '#1f2835'}]
                      },
                      {
                        featureType: 'road.highway',
                        elementType: 'labels.text.fill',
                        stylers: [{color: '#f3d19c'}]
                      },
                      {
                        featureType: 'transit',
                        elementType: 'geometry',
                        stylers: [{color: '#2f3948'}]
                      },
                      {
                        featureType: 'transit.station',
                        elementType: 'labels.text.fill',
                        stylers: [{color: '#d59563'}]
                      },
                      {
                        featureType: 'water',
                        elementType: 'geometry',
                        stylers: [{color: '#17263c'}]
                      },
                      {
                        featureType: 'water',
                        elementType: 'labels.text.fill',
                        stylers: [{color: '#515c6d'}]
                      },
                      {
                        featureType: 'water',
                        elementType: 'labels.text.stroke',
                        stylers: [{color: '#17263c'}]
                      }
                    ]
        });

        // Construct the circle for each value in citymap.
        // Note: We scale the area of the circle based on the population.
         var infowindow = new google.maps.InfoWindow();


        for (var city in citymap) {
          var i = citymap[city].id
          // Add the circle for this city to the map.
          var cityCircle = new google.maps.Circle({
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#FF0000',
            fillOpacity: 0.35,
            map: map,
            center: citymap[city].center,
            radius: Math.sqrt(citymap[city].population) * 100
          })

            marker = new google.maps.Marker({
            position: citymap[city].center,
            label: citymap[city].label,
            map: map
              });


        google.maps.event.addListener(marker,'click',(function(marker, i) {
        return function() {
         map.setZoom(10);
         map.setCenter(marker.getPosition());
         var land_id=marker.getLabel()


         infowindow.setContent('fuck');
         infowindow.open(map, marker);

/*          document.write(land_id) */
        }
      })(marker, i));




      }

      }


//        function loadScript() {
//        var script = document.createElement('script');
//        script.type = 'text/javascript';
//        string = "hey it works";   //////////// here take the coordinates
//        script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCkUOdZ5y7hMm0yrcCQoCvLwzdM6M8s5qk&callback=initMap";
//        document.body.appendChild(script);
//    }
//
//loadScript()

