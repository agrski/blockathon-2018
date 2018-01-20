
//writes function which computes centre of these places





function initMap(citymap) {
    
    
    var citymap = {
        place_one: {
              center: {lat: -9.38294817, lng: 148.40222161},
              population: 27148
            },
            place_two: {
              center: {lat: -9.10101191, lng: 147.71008294},
              population: 84058
            }
          };

          
      //we want initMap to take values from the ledger    
          

        // Create the map inside the div container with id map
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
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
        for (var city in citymap) {
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
          });
        }
             
     var location = {lat: -9.38294817, lng: 148.40222161};
        // Add the marker at the clicked location, and add the next-available label
        // from the array of alphabetical characters.
     var marker = new google.maps.Marker({
          position: location,
          label: '1',
          map: map
            });
    
     var marker = new google.maps.Marker({
      position: {lat: -9.10101191, lng: 147.71008294},
      label: '2',
         //icon: 'brown_markerA.png',
      map: map
        });


      }

// async defer
//     src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBkWDBpsOpoLnWCeJ00Hq27d2iuiFtLHh8&callback=initMap"