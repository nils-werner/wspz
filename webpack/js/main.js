require("bootstrap");
require("lightbox2");
var DarkReader = require('darkreader');
var anchorJS = require('anchor-js');

var anchors = new anchorJS({'placement': 'left'});
anchors.add('.text-block h2, .text-block h3');

if(window.matchMedia('(prefers-color-scheme: dark)').matches) {
  alert("baaa")
  DarkReader.enable({
      brightness: 100,
      contrast: 90,
      sepia: 10,
  });
}
