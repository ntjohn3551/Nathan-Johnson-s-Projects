url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Get started by retrieving the data and plotting points
d3.json(url).then(function (earthquakes) {
  plot(earthquakes.features);
});

// Adjusting the plotted points
function plot(data) {
  // Add the popups
  function onEachFeature(point, popup) {
    popup.bindPopup(`<p>Coordinates: ${point.geometry.coordinates[1]}, ${point.geometry.coordinates[0]}
    <br>Magnitude: ${point.properties.mag}
    <br>Date/Time: ${new Date(point.properties.time)}
    <br>Depth: ${point.geometry.coordinates[2]} km</p>`);
  }
  
  coords = L.geoJSON(data, {
    pointToLayer: function (point, coordinates) {
      return L.circleMarker(coordinates, 
        {
          // Modify each point's size and color
          weight: 0.5,
          color: "black",
          opacity: 1,
          radius: (point.properties.mag) * 5,
          fillColor: colorScale(point.geometry.coordinates[2]),
          fillOpacity: 1
        }
        );
    },
    onEachFeature: onEachFeature
  });
  
  map(coords);
}

// Color by depth
function colorScale(depth) {
  
  if (depth <= 10 ) return "#068900";
  else if (depth <= 30) return "#7CFF00";
  else if (depth <= 50) return "#FFDC00";
  else if (depth <= 70) return "#FF9700";
  else if (depth <= 90) return "#FF5100";
  else return "#BD0000";
}

// Formatting how the map is displayed on load, as well as the legend
function map(pointData) {
  streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  // Starting position and zoom of the map
  theMap = L.map("map", {
    center: [
      0, 0
    ],
    zoom: 3,
    layers: [streetmap, pointData]
  });

  // Add the legend
  mapLegend = L.control({ position: "bottomright" });

// Add colored squares to the legend, and a title
mapLegend.onAdd = function() {
    legendSquares = L.DomUtil.create("div", "legend");
    legendSquares.innerHTML += '<h3>Depth (km)</h3><a style="background: #068900"></a><span>-10 - 10</span><br><a style="background: #7CFF00"></a><span>10 - 30</span><br><a style="background: #FFDC00"></a><span>30 - 50</span><br><a style="background: #FF9700"></a><span>50 - 70</span><br><a style="background: #FF5100"></a><span>70 - 90</span><br><a style="background: #BD0000"></a><span>90+</span><br>'
    return legendSquares;
  };

  mapLegend.addTo(theMap);      
}

  