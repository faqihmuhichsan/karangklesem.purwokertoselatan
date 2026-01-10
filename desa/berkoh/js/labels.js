var hideLabel = function(label) {
  if (!label || !label.labelObject) return;
  label.labelObject.style.opacity = '0';
  label.labelObject.style.transition = 'opacity 0.2s ease-out';
};

var showLabel = function(label) {
  if (!label || !label.labelObject) return;
  label.labelObject.style.opacity = '1';
  label.labelObject.style.transition = 'opacity 0.25s ease-in';
};

labelEngine = new labelgun.default(hideLabel, showLabel);
labelEngine.settings = labelEngine.settings || {};
labelEngine.settings.fontFamily = "'Inter', sans-serif";
labelEngine.settings.fontSize = 12;

var id = 0;
var labels = [];
var totalMarkers = 0;
var _labelUpdateTimeout = null;

function resetLabels(markers) {
  labelEngine.reset();
  var i = 0;
  for (var j = 0; j < markers.length; j++) {
    markers[j].eachLayer(function(label){
      addLabel(label, ++i);
    });
  }
  // small debounce to allow DOM updates
  clearTimeout(_labelUpdateTimeout);
  _labelUpdateTimeout = setTimeout(function(){ labelEngine.update(); }, 150);
}

function addLabel(layer, id) {
  if (!layer || !layer.getTooltip) return;
  var tt = layer.getTooltip();
  if (!tt) return;
  var label = tt._source && tt._source._tooltip && tt._source._tooltip._container;
  if (!label) return;

  var rect = label.getBoundingClientRect();
  var bottomLeft = map.containerPointToLatLng([rect.left, rect.bottom]);
  var topRight = map.containerPointToLatLng([rect.right, rect.top]);
  var boundingBox = {
    bottomLeft : [bottomLeft.lng, bottomLeft.lat],
    topRight   : [topRight.lng, topRight.lat]
  };

  labelEngine.ingestLabel(
    boundingBox,
    id,
    1 + Math.floor(Math.random()*4),
    label,
    "Label_" + id,
    false
  );

  if (!layer.added) {
    layer.addTo(map);
    layer.added = true;
  }
}

// update labels after map move/zoom with debounce
map && map.on && map.on('moveend', function(){
  clearTimeout(_labelUpdateTimeout);
  _labelUpdateTimeout = setTimeout(function(){ if (labelEngine) labelEngine.update(); }, 200);
});

map && map.on && map.on('zoomend', function(){
  clearTimeout(_labelUpdateTimeout);
  _labelUpdateTimeout = setTimeout(function(){ if (labelEngine) labelEngine.update(); }, 150);
});